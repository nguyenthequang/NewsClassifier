"""Main Algorithm"""
import os
from flask import Flask, render_template, request
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Home route for the Flask application.
    Handles both GET and POST requests.
    If a POST request is made with a text input, it processes the input,
    makes predictions using a trained model, and renders the result page.
    If a GET request is made, it renders the index page with the text input form.
    """
    if request.method == 'POST':
        user_input = request.form['text']

        # Load and preprocess the 20 Newsgroups dataset
        categories = None  # Use all categories
        newsgroups_train = fetch_20newsgroups(subset='train',
                                              remove=('headers', 'footers', 'quotes'),
                                              categories=categories,
                                              shuffle=True, random_state=42)
        # newsgroups_test = fetch_20newsgroups(subset='test',
        #                                      remove=('headers', 'footers', 'quotes'),
        #                                      categories=categories,
        #                                      shuffle=True, random_state=42)

        if os.path.exists('model.joblib') and os.path.exists('vectorizer.joblib'):
            # Load the trained model and vectorizer
            loaded_classifier = joblib.load('model.joblib')
            loaded_vectorizer = joblib.load('vectorizer.joblib')
        else:
            vectorizer = TfidfVectorizer()
            X_train = vectorizer.fit_transform(newsgroups_train.data)
            y_train = newsgroups_train.target
            # X_test = vectorizer.transform(newsgroups_test.data)
            # y_test = newsgroups_test.target

            # Train an SVM classifier
            classifier = SVC(kernel='linear')
            classifier.fit(X_train, y_train)

            # Save the trained model and vectorizer
            joblib.dump(classifier, 'model.joblib')
            joblib.dump(vectorizer, 'vectorizer.joblib')

            loaded_classifier = classifier
            loaded_vectorizer = vectorizer

        # Preprocess the user input and make predictions
        preprocessed_input = loaded_vectorizer.transform([user_input])
        predicted_category = loaded_classifier.predict(preprocessed_input)

        # Get the predicted category label
        category_label = newsgroups_train.target_names[predicted_category[0]]

        return render_template('result.html', category=category_label)

    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Route handler for the '/predict' endpoint.
    Handles the POST request made from the form submission in index.html.
    """
    return home()

if __name__ == '__main__':
    app.run()
