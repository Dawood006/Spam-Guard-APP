import pickle
import streamlit as st
import numpy as np
import urllib.request

# Load models
def load_model(url, filename):
    urllib.request.urlretrieve(url, filename)
    with open(filename, "rb") as file:
        return pickle.load(file)

# Publicly accessible model URLs
model_url = "https://github.com/Dawood006/Spam-Guard-APP/raw/9dfaeb5a849af9a24e8cf80e103a5028b2f2c393/model_nb.pkl"
cv_url = "https://github.com/Dawood006/Spam-Guard-APP/raw/9dfaeb5a849af9a24e8cf80e103a5028b2f2c393/model_cv.pkl"

# Load models safely
try:
    gb = load_model(model_url, "model_nb.pkl")
    cv = load_model(cv_url, "model_cv.pkl")
except Exception as e:
    st.error(f"Error loading models: {e}")

# Function for spam prediction
def predict_spam(data):
    try:
        transformed_data = cv.transform([data])
        prediction = gb.predict(transformed_data)  # Avoid forcing to dense array
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
st.image("https://media.istockphoto.com/id/1454135464/vector/shield-paw-print-dog-icon-silhouette.jpg", width=100)

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
                    st.image("https://thumbs.dreamstime.com/b/angry-dog-mascot-cartoon-angry-dog-mascot-cartoon-illustration-100486272.jpg", width=100)
                else:
                    st.success("🎉 NO SPAM DETECTED! 🎉\n\nPuppyGuard gives this email a paws-up! It looks safe to open! 🐶")
                    st.image("https://img.icons8.com/color/96/000000/dog.png", width=100)
                    st.balloons()

# Footer
st.markdown("---")
st.markdown("<small>Made with ❤️🐾</small>", unsafe_allow_html=True)
