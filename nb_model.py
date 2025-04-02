import pickle
import streamlit as st
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer

# Load models
@st.cache_resource
def load_models():
    with open(r'https://github.com/Dawood006/Spam-Guard-APP/raw/0185e9fa34eee419d96b40da9ade39f1d5bcc21a/model_cv','rb') as file:
        gb = pickle.load(file)
    with open('model_cv','rb') as file:
        cv = pickle.load(file)
    return gb, cv

gb, cv = load_models()

def predict_spam(data):
    data = cv.transform([data])
    return gb.predict(data.toarray())

# Adorable UI
# st.set_page_config(
#     page_title="🐶 PuppyGuard - Email Spam Detector",
#     page_icon="🐾",
#     layout="centered"
# )

# Custom CSS for adorable styling
st.markdown("""
<style>
    .stApp {
        background-color: #FFF5F5;
    }
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

# Header with cute emoji
st.markdown("""
# 🐶 PuppyGuard 
### Your Friendly Email Spam Detector 🛡️
""")

st.image("https://media.istockphoto.com/id/1454135464/vector/shield-paw-print-dog-icon-silhouette.jpg?s=612x612&w=0&k=20&c=aDUUkZkBynuA-IIqGvW5vbkhOXDWPNdSGdHj8VU5Gdo=", width=100)

st.markdown("""
PuppyGuard will sniff out any suspicious content in your emails! 
Just paste the text below and we'll check it for you. 🐾
""")

# Text area with cute placeholder
user_input = st.text_area(
    "📝 Paste your email content here:", 
    height=200,
    placeholder="PuppyGuard is waiting to check your text... Woof! 🐕"
)

if st.button("🔍 Check for Spam!"):
    if not user_input:
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
                st.image("https://thumbs.dreamstime.com/b/angry-dog-mascot-cartoon-angry-dog-mascot-cartoon-illustration-100486272.jpg", width=100)
            else:
                st.success("""
                🎉 *YAY! NO SPAM DETECTED!* 🎉
                
                PuppyGuard gives this email a paws-up! 
                It looks safe to open! 🐶
                """)
                st.image("https://img.icons8.com/color/96/000000/dog.png", width=100)
                st.balloons()

# Cute footer
st.markdown("---")
st.markdown("""
<small>Made with ❤️🐾 /small>
""", unsafe_allow_html=True)
