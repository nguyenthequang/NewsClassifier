from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import os

print("START!!!")
# Load and preprocess the 20 Newsgroups dataset
categories = None  # Use all categories
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), 
                                      categories=categories, shuffle=True, random_state=42)
newsgroups_test = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'), 
                                     categories=categories, shuffle=True, random_state=42)

if os.path.exists('model.joblib') and os.path.exists('vectorizer.joblib'):
    # Load the trained model and vectorizer
    loaded_classifier = joblib.load('model.joblib')
    loaded_vectorizer = joblib.load('vectorizer.joblib')
else:
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(newsgroups_train.data)
    X_test = vectorizer.transform(newsgroups_test.data)
    y_train = newsgroups_train.target
    y_test = newsgroups_test.target

    # Train an SVM classifier
    classifier = SVC(kernel='linear')
    classifier.fit(X_train, y_train)

    # Save the trained model and vectorizer
    joblib.dump(classifier, 'model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')

    loaded_classifier = classifier
    loaded_vectorizer = vectorizer

# Make predictions on user input
cont = "Y"
while cont == "Y":
    user_input = input("Enter your text: ")
    preprocessed_input = loaded_vectorizer.transform([user_input])
    predicted_category = loaded_classifier.predict(preprocessed_input)
    # Get the predicted category label
    category_label = newsgroups_train.target_names[predicted_category[0]]

    print(f"Predicted category: {category_label}")
    cont = input("Try another text? Y or N: ")
