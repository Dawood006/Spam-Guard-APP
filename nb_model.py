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

# Streamlit UI remains unchanged...
