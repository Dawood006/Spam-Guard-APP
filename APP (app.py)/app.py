import streamlit as st
import pickle

# Load trained model and vectorizer
with open('model_cv.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('model_nb.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page configuration
st.set_page_config(
    page_title="Spam Guard 🛡️",
    page_icon="🐶",
    layout="centered"
)

# App title
st.title("🐶 Spam Guard App")
st.markdown("Protecting you from spam, one bark at a time!")

# Text input from user
user_input = st.text_area("✉️ Enter your message here:")

if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        # Vectorize and predict
        vectorized_msg = vectorizer.transform([user_input]).toarray()
        prediction = model.predict(vectorized_msg)

        # Display result
        if prediction[0] == 1:
            st.error("🚨 This looks like SPAM!")
        else:
            st.success("✅ This message is NOT spam.")

# Footer
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ by <a href='https://github.com/Dawood006' target='_blank'>Dawood006</a></center>",
    unsafe_allow_html=True
)
