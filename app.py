"""News classifier web application.

Loads a pre-trained TF-IDF vectorizer and linear SVM (see train.py) and
serves predictions over a small Flask UI. The model and vectorizer are
loaded once at startup rather than per request.
"""
import os
from flask import Flask, render_template, request
import joblib
from helper import translate_category_name

# Category labels in the order the model predicts them (target index 0-19).
# These are the fixed 20 Newsgroups category names, so there is no need to
# download the dataset at runtime just to map a prediction to its label.
CATEGORY_NAMES = [
    'alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x',
    'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball',
    'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med',
    'sci.space', 'soc.religion.christian', 'talk.politics.guns',
    'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc',
]

MODEL_PATH = 'model.joblib'
VECTORIZER_PATH = 'vectorizer.joblib'

app = Flask(__name__)

if not (os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH)):
    raise FileNotFoundError(
        "Missing model.joblib or vectorizer.joblib. Run `python train.py` "
        "first to generate them."
    )

# Load the trained model and vectorizer once, at startup.
classifier = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render the input form (GET) or classify submitted text (POST)."""
    if request.method == 'POST':
        user_input = request.form['text']

        preprocessed_input = vectorizer.transform([user_input])
        predicted_index = classifier.predict(preprocessed_input)[0]

        category_label = translate_category_name(CATEGORY_NAMES[predicted_index])
        return render_template('result.html', category=category_label)

    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle the form submission from index.html."""
    return home()


if __name__ == '__main__':
    app.run()
