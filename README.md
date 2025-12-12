📧 Spam Email Classifier
A machine learning–based web application that detects whether a message is Spam or Ham (Not Spam) using TF-IDF vectorization and a Naive Bayes classifier.
The project also includes a clean, modern Streamlit UI for interactive predictions.

🚀 Features


🔍 Real-time Spam/Ham Message Classification


🧠 ML model trained using Multinomial Naive Bayes


✨ TF-IDF Vectorization for text feature extraction


📊 Spam probability score shown after prediction


🎨 Modern, responsive Streamlit interface


⚡ Sample Spam/Ham message autofill buttons


🧹 Clean preprocessing (lowercase, no punctuation, stopword removal)


📁 Organized project structure with trained model files



🧠 How It Works
This application uses a classical NLP + ML approach:


Text Preprocessing


Lowercasing


Removing punctuation


Removing stopwords




Feature Extraction


TF-IDF Vectorizer converts text into numerical vectors.




Model Training


Multinomial Naive Bayes classifier (best for text classification)


Trained on SMS Spam Collection dataset




Prediction


The vectorizer transforms user input


Model predicts Spam/Ham + probability score





📂 Project Structure
Spam-Email-Classifier/
│
├── app.py                   # Streamlit frontend application
├── train_model.ipynb        # Notebook used to train the ML model
├── README.md                # Documentation file
├── requirements.txt         # Dependencies
│
├── data/
│   └── spam.csv             # Dataset used for training
│
├── models/
│   ├── model.pkl            # Trained Naive Bayes model
│   └── vectorizer.pkl       # Trained TF-IDF vectorizer
│
└── .gitignore               # (optional)


▶️ Running the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit App
python -m streamlit run app.py

Your browser will open the app automatically at:
👉 http://localhost:8501

📊 Model Performance


Algorithm: Multinomial Naive Bayes


Dataset: SMS Spam Collection


Performance metrics printed inside train_model.ipynb


You can open the notebook to view:


Accuracy


Classification report


Confusion matrix



🎨 Streamlit UI Preview
(Add a screenshot here after running your app)
Example:
![Spam Classifier UI](images/app_preview.png)


🛠 Technologies Used


Python


Scikit-learn


Streamlit


Pandas


NumPy


NLTK



📌 Future Improvements


Add Logistic Regression & SVM comparison


Add dark mode toggle


Add email subject + body classification


Deploy app on Streamlit Cloud / HuggingFace


Add WordCloud / visualizations

Made by-Shivam Dongare



