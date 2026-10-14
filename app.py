import re
import string
import sys
from pathlib import Path

import joblib
import numpy as np
import streamlit as st


# ---------------------------------------------------------------------------
# Preprocessing function
# ---------------------------------------------------------------------------
# The saved pipeline stores a reference to a function named `wordopt`
# (it was the TfidfVectorizer's `preprocessor`). joblib needs it to exist when
# loading, and it must behave exactly as it did during training.
# If your training version differs, paste your original function here.
def wordopt(text):
    text = text.lower()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub(r"\n", "", text)
    text = re.sub(r"\w*\d\w*", "", text)
    return text


# The model was pickled from a notebook, so it looks for `wordopt` in __main__.
sys.modules["__main__"].wordopt = wordopt

MODEL_PATH = Path(__file__).parent / "imdb_sentiment_model.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def predict_sentiment(model, text):
    """Return (label, p_negative, p_positive).

    Probabilities are computed from decision_function + sigmoid instead of
    calling predict_proba(). This gives identical results for binary logistic
    regression and avoids scikit-learn version problems
    (e.g. "no attribute 'multi_class'").
    """
    vectorizer = model.steps[0][1]
    clf = model.steps[-1][1]

    X = vectorizer.transform([text])
    score = float(np.ravel(clf.decision_function(X))[0])
    p_pos = 1.0 / (1.0 + np.exp(-score))
    p_neg = 1.0 - p_pos
    label = 1 if score > 0 else 0
    return label, p_neg, p_pos


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
st.set_page_config(page_title="IMDB Sentiment Analyzer", page_icon="🎬")

st.title("🎬 IMDB Movie Review Sentiment")
st.write("Paste a movie review and the model will predict whether it's positive or negative.")

try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the model: {e}")
    st.stop()

EXAMPLES = {
    "Positive example": "An absolutely brilliant film. The acting was superb and the story kept me hooked until the very end.",
    "Negative example": "A dull, predictable mess. The plot made no sense and I nearly fell asleep halfway through.",
}

if "review" not in st.session_state:
    st.session_state["review"] = ""

cols = st.columns(len(EXAMPLES))
for col, (label, text) in zip(cols, EXAMPLES.items()):
    if col.button(label, use_container_width=True):
        st.session_state["review"] = text

review = st.text_area(
    "Your review", key="review", height=180, placeholder="Type or paste a review here..."
)

if st.button("Analyze", type="primary"):
    if not review.strip():
        st.warning("Please enter a review first.")
    else:
        pred, p_neg, p_pos = predict_sentiment(model, review)
        confidence = p_pos if pred == 1 else p_neg

        if pred == 1:
            st.success(f"😊 Positive ({confidence:.1%} confidence)")
        else:
            st.error(f"😞 Negative ({confidence:.1%} confidence)")

        st.progress(float(p_pos), text=f"Positive probability: {p_pos:.1%}")
        st.caption(f"Negative probability: {p_neg:.1%}")