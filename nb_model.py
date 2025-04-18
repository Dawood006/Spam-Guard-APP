import pickle
import streamlit as st
import numpy as np
import requests
import os
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer

# URLs for the models on GitHub
MODEL_NB_URL = "https://github.com/Dawood006/Spam-Guard-APP/raw/0926bb6db1776627b7ffd98c0f638110ef3ee0b8/model2_gb.pkl"
MODEL_CV_URL = "https://github.com/Dawood006/Spam-Guard-APP/raw/0926bb6db1776627b7ffd98c0f638110ef3ee0b8/model1_cv.pkl"

# Download function
def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

# Load models
@st.cache_resource
def load_models():
    if not os.path.exists("model_nb.pkl"):
        download_file(MODEL_NB_URL, "model_nb.pkl")
    if not os.path.exists("model_cv.pkl"):
        download_file(MODEL_CV_URL, "model_cv.pkl")
    
    with open("model_nb.pkl", "rb") as file:
        gb = pickle.load(file)
    with open("model_cv.pkl", "rb") as file:
        cv = pickle.load(file)
    
    return gb, cv

gb, cv = load_models()

def predict_spam(data):
    data = cv.transform([data])
    return gb.predict(data.toarray())

# ---------- Streamlit UI Starts Here ---------- #

# Page settings
# st.set_page_config(page_title="🐶 PuppyGuard", page_icon="🐾", layout="centered")

# Custom CSS styling
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
        color: white !important;
    }
    .css-1aumxhk {
        background-color: #FFD1DC;
        border-radius: 15px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
# 🐶 PuppyGuard 
### Your Friendly Email Spam Detector 🛡️
""")

st.image("https://media.istockphoto.com/id/1454135464/vector/shield-paw-print-dog-icon-silhouette.jpg?s=612x612&w=0&k=20&c=aDUUkZkBynuA-IIqGvW5vbkhOXDWPNdSGdHj8VU5Gdo=", width=100)

st.markdown("""
PuppyGuard will sniff out any suspicious content in your emails!  
Just paste the text below and we'll check it for you. 🐾
""")

# Text input
user_input = st.text_area(
    "📝 Paste your email content here:", 
    height=200,
    placeholder="PuppyGuard is waiting to check your text... Woof! 🐕   (Enter 10 min. character)"
)

if st.button("🔍 Check for Spam!"):
    if not user_input.strip():
        st.warning("Please enter some text for PuppyGuard to check! 🐾")
    else:
        with st.spinner("PuppyGuard is sniffing your text... 🐾"):
            prediction = predict_spam(user_input)
            
            if prediction == 1:
                st.error("""
                🚨 *WOOF WOOF! SPAM ALERT!* 🚨  
                PuppyGuard detected malicious content!  
                Better not open this one! 🦴
                """)
                st.image("https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/96/external-warning-signs-kiranshastry-lineal-color-kiranshastry.png", width=120)  # angry dog
            else:
                st.success("""
                🎉 *YAY! NO SPAM DETECTED!* 🎉  
                PuppyGuard gives this email a paws-up!  
                It looks safe to open! 🐶
                """)
                st.image("https://img.icons8.com/color/452/dog.png", width=120)  # happy dog
                st.balloons()

# Footer
st.markdown("---")
st.markdown("<small>Made with ❤️ by Dawood 🐾</small>", unsafe_allow_html=True)
