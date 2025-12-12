

import streamlit as st
import pickle
import numpy as np

# ------------------------------
# Load vectorizer & model
# ------------------------------
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# ------------------------------
# Streamlit Page Config
# ------------------------------
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📧",
    layout="centered"
)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("📌 About This App")
st.sidebar.info("""
This is a **Machine Learning Spam Classifier** built using:
- TF-IDF Vectorizer  
- Naive Bayes Classifier  
- Streamlit UI  

It predicts whether a message is **Spam** or **Not Spam**.
""")

st.sidebar.title("📚 Model Info")
st.sidebar.write("Algorithm: **Multinomial Naive Bayes**")
st.sidebar.write("Training Data: **SMS Spam Dataset**")

st.sidebar.title("⚡ Quick Samples")
if st.sidebar.button("Insert Spam Example"):
    st.session_state["message"] = "Congratulations! You won a free lottery. Claim now!"
if st.sidebar.button("Insert Ham Example"):
    st.session_state["message"] = "Hey, are we still meeting tomorrow?"

# ------------------------------
# Main Title
# ------------------------------
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>📧 Spam Email Classifier</h1>", unsafe_allow_html=True)
st.write("Enter a message below and get an instant spam prediction.")

# ------------------------------
# Message Input Area
# ------------------------------
message = st.text_area("✏️ Enter your message:", key="message", height=180)

# Character count
st.write(f"**Character Count:** {len(message)}")

# ------------------------------
# Prediction Button
# ------------------------------
if st.button("🔍 Predict"):
    if message.strip() == "":
        st.warning("⚠️ Please type a message!")
    else:
        with st.spinner("Analyzing message... 🔍"):
            vector = vectorizer.transform([message])
            prediction = model.predict(vector)[0]
            probability = model.predict_proba(vector)[0][1]

        # --------------------------
        # Display Result in Styled Box
        # --------------------------
        if prediction == 1:
            st.markdown("""
                <div style='padding: 20px; border-radius: 12px; background-color:#ffdddd;'>
                    <h2 style='color:#cc0000;'>🚨 SPAM DETECTED!</h2>
                    <p style='font-size:18px;'>This message appears to be <b>Spam</b>.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='padding: 20px; border-radius: 12px; background-color:#ddffdd;'>
                    <h2 style='color:#008800;'>✅ Not Spam (Ham)</h2>
                    <p style='font-size:18px;'>This message appears to be <b>Safe</b>.</p>
                </div>
            """, unsafe_allow_html=True)

        # Probability Bar
        st.progress(probability)
        st.info(f"**Spam Probability:** {probability * 100:.2f}%")

# ------------------------------
# Footer
# ------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Built with ❤️ using Machine Learning & Streamlit.
</p>
""", unsafe_allow_html=True)