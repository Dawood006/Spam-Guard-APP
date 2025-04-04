# Spam-Guard-APP


---

# 🛡️ Spam Guard App

🔗 **Live App**: [https://puppyguard.streamlit.app/](https://puppyguard.streamlit.app/)

Spam Guard App (aka **PuppyGuard**) is a fun and user-friendly web app that helps detect email spam using machine learning. Built using **Streamlit** and **scikit-learn**, the app uses a pre-trained model to analyze message content and classify it as *Spam* or *Not Spam*.

---

## 🐾 Features

- 📥 Accepts user text input
- ⚙️ Uses CountVectorizer + Gaussian Naive Bayes for spam detection
- 🎨 Cute and playful UI themed around a "puppy guard"
- ⚡ Fast and interactive prediction using Streamlit
- 📦 Lightweight with minimal dependencies

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `nb_model.py` | Main Streamlit app script. Loads models and displays the adorable spam detection UI. |
| `model_nb.pkl` | Pickled trained Gaussian Naive Bayes classifier. |
| `model_cv.pkl` | Pickled `CountVectorizer` used to transform input text for prediction. |
| `Naivebayes_st.ipynb` | Jupyter notebook that explores data processing, model training, evaluation, and insights. |
| `spam.csv` | Dataset used to train and evaluate spam detection model. |
| `requirements.txt` | List of Python dependencies to run the app. |

---

## 🚀 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Dawood006/Spam-Guard-APP.git
   cd Spam-Guard-APP

2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run nb_model.py
   ```

---

## 💡 How It Works

- The user enters email content into a text box.
- The message is vectorized using a pre-trained `CountVectorizer` (`model_cv.pkl`).
- It is then passed through a trained `GaussianNB` model (`model_nb.pkl`).
- Prediction is shown along with a fun puppy-themed message 🐶.

---

## 📊 Dataset

We use the **SMS Spam Collection Dataset**, a public set of ~5,000 English SMS labeled messages, available in `spam.csv`.

---

## 🧠 Sample Prediction Code

If you want to try out the models in plain Python:

```python
import pickle

# Load models
with open('model_cv.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('model_nb.pkl', 'rb') as f:
    model = pickle.load(f)

msg = ["Congratulations! You won a prize. Call now!"]
msg_transformed = vectorizer.transform(msg).toarray()
pred = model.predict(msg_transformed)

print("Spam" if pred[0] == 1 else "Not Spam")
```

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

```
streamlit
numpy
scikit-learn
requests
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Made with ❤️ by [Dawood006](https://github.com/Dawood006)

---


---

## ⭐ Show Some Love

If you find this project helpful or fun, give it a ⭐ on GitHub or try out the [live app](https://puppyguard.streamlit.app/)! 🐾
```

---

Let me know if you want a Markdown download file or want to auto-create a `LICENSE` or `app.py` file too!
