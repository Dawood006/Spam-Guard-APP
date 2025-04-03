import pickle
import streamlit as st
import numpy as np
import requests
import io
# Import scikit-learn modules explicitly
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB

# App title and configuration
st.set_page_config(page_title="PuppyGuard Spam Detector", page_icon="🐶")

# Function to load models directly from GitHub URLs
@st.cache_resource
def load_model_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return pickle.loads(response.content)
        else:
            st.error(f"Failed to load model. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load models
with st.spinner("Loading PuppyGuard's brain..."):
    # GitHub raw URLs for models
    model_url = "https://github.com/Dawood006/Spam-Guard-APP/raw/9dfaeb5a849af9a24e8cf80e103a5028b2f2c393/model_nb.pkl"
    cv_url = "https://github.com/Dawood006/Spam-Guard-APP/raw/9dfaeb5a849af9a24e8cf80e103a5028b2f2c393/model_cv.pkl"
    
    # Load models
    gb = load_model_from_url(model_url)
    cv = load_model_from_url(cv_url)

# Function for spam prediction
def predict_spam(data):
    if gb is None or cv is None:
        st.error("PuppyGuard couldn't load its detection tools. Please try again later.")
        return None
    try:
        transformed_data = cv.transform([data])  # Transform the input data
        prediction = gb.predict(transformed_data)  # Predict using Naive Bayes
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

# UI Styling
st.markdown("""
<style>
    .stApp { background-color: #FFF5F5; }
    .stTextArea>div>div>textarea {
        background-color: #FFF9F9;
        border-radius: 15px;
        padding: 15px;
    }
    .stButton>button {
        background-color: #FFB6C1 !important;
        color: white !important;
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF69B4 !important;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("# 🐶 PuppyGuard - Spam Detector 🛡️")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://media.istockphoto.com/id/1454135464/vector/shield-paw-print-dog-icon-silhouette.jpg", width=150)
st.markdown("PuppyGuard will sniff out any suspicious content in your emails! Just paste the text below and we'll check it for you. 🐾")

# Text input
user_input = st.text_area("📝 Paste your email content here:", height=200, placeholder="PuppyGuard is waiting to check your text... Woof! 🐕")

# Button to check spam
if st.button("🔍 Check for Spam!"):
    if not user_input.strip():
        st.warning("Please enter some text for PuppyGuard to check! 🐾")
    else:
        with st.spinner("PuppyGuard is sniffing your text... 🐾"):
            prediction = predict_spam(user_input)
            if prediction is not None:
                if prediction == 1:
                    st.error("🚨 WOOF! SPAM ALERT! 🚨\n\nPuppyGuard detected malicious content! Better not open this one! 🦴")
                    st.image("https://thumbs.dreamstime.com/b/angry-dog-mascot-cartoon-angry-dog-mascot-cartoon-illustration-100486272.jpg", width=150)
                else:
                    st.success("🎉 NO SPAM DETECTED! 🎉\n\nPuppyGuard gives this email a paws-up! It looks safe to open! 🐶")
                    st.image("https://img.icons8.com/color/96/000000/dog.png", width=150)
                    st.balloons()

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center'><small>Made with ❤️🐾</small></div>", unsafe_allow_html=True)
