# 🎬 IMDB Movie Review Sentiment Analyzer

## 📌 Project Overview

The **IMDB Movie Review Sentiment Analyzer** is a machine learning project that analyzes movie reviews and predicts whether a review expresses a **Positive** or **Negative** sentiment.

Built using Python and Streamlit, this application allows users to enter a movie review and receive a sentiment prediction along with estimated sentiment probabilities.

## 🌐 Demo Links

- **Live Demo:** https://gr3lc248z3rhy7rbgy9n88.streamlit.app/
- **Local Demo:** http://localhost:8501

**Note:** The localhost link works only when the application is running on your computer. It is not a public link.

## 🎯 Objectives

- Analyze the sentiment of movie reviews.
- Classify reviews as positive or negative.
- Apply Natural Language Processing (NLP) techniques to text data.
- Build an interactive web application using Streamlit.
- Display prediction confidence and sentiment probabilities.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Streamlit** – Web application interface
- **Scikit-learn** – Machine learning pipeline
- **TF-IDF Vectorizer** – Converts text into numerical features
- **Logistic Regression** – Sentiment classification
- **NumPy** – Numerical calculations
- **Joblib** – Loading the saved machine learning model
- **Regular Expressions (Regex)** – Text preprocessing

## ✨ Features

- Simple and user-friendly interface.
- Text input for movie reviews.
- Predefined positive and negative review examples.
- Automatic sentiment prediction.
- Positive and negative probability display.
- Visual progress bar for positive sentiment.
- Prediction confidence percentage.
- Error handling when the model cannot be loaded.

## 📂 Project Structure

```text
IMDB-Sentiment-Analyzer/
│
├── app.py
├── imdb_sentiment_model.joblib
└── README.md
```

**Note:** The `imdb_sentiment_model.joblib` file must be in the same folder as `app.py`. It contains the trained machine learning pipeline.

## 🚀 Installation and Setup

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Install Required Libraries

Open the terminal in your project folder and run:

```bash
pip install streamlit scikit-learn numpy joblib
```

### Step 3: Keep the Model File Ready

Make sure `imdb_sentiment_model.joblib` is available in the same folder as `app.py`.

The application requires a compatible saved model pipeline containing the text vectorizer and trained classifier.

### Step 4: Run the Application

Execute the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your web browser. The local address is usually:

http://localhost:8501

## 🧠 How It Works

1. **Input:** The user enters or pastes a movie review.
2. **Text Preprocessing:** The `wordopt()` function cleans the review text.
3. **Feature Extraction:** The TF-IDF vectorizer converts the text into numerical features.
4. **Prediction:** The trained Logistic Regression classifier calculates a sentiment score.
5. **Classification:** The application classifies the review as positive or negative.
6. **Result Display:** Streamlit displays the predicted sentiment and estimated probabilities.

## 💻 Example

### Positive Review

> An absolutely brilliant film. The acting was superb and the story kept me hooked until the very end.

**Expected Output:** Positive 😊

### Negative Review

> A dull, predictable mess. The plot made no sense and I nearly fell asleep halfway through.

**Expected Output:** Negative 😞

*Note: Actual predictions depend on the trained machine learning model.*

## 📊 Output

The application displays:

- Predicted sentiment: Positive or Negative
- Prediction confidence percentage
- Positive sentiment probability
- Negative sentiment probability

## 🔮 Future Enhancements

- Support additional sentiment categories, such as neutral.
- Improve prediction accuracy using a larger dataset.
- Add a review history feature.
- Deploy the application online.
- Compare different machine learning algorithms.

## 🏁 Conclusion

The IMDB Movie Review Sentiment Analyzer demonstrates how Natural Language Processing and machine learning can be used to classify text sentiment. It combines Python, TF-IDF, Logistic Regression, and Streamlit to create an interactive application for analyzing movie reviews.

---

**Developed using Python, Machine Learning, NLP, and Streamlit.**
