"""Train and save the news classifier artifacts.

Trains a Complement Naive Bayes classifier on the 20 Newsgroups dataset
using TF-IDF features, then saves the model, vectorizer, and an evaluation
report. Run this whenever the scikit-learn version changes, since saved
models are not guaranteed to load across versions.

The TF-IDF settings (sublinear term frequency, English stop words, uni- and
bi-grams, min_df=2) and the Complement Naive Bayes classifier were chosen by
3-fold cross-validation on the training set. This reaches ~0.72 test accuracy,
up from ~0.66 for the original default-TF-IDF linear SVM.

Usage:
    python train.py
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import classification_report
import joblib

REMOVE = ('headers', 'footers', 'quotes')


def main():
    print("Loading the 20 Newsgroups dataset...")
    newsgroups_train = fetch_20newsgroups(subset='train', remove=REMOVE,
                                          shuffle=True, random_state=42)
    newsgroups_test = fetch_20newsgroups(subset='test', remove=REMOVE,
                                         shuffle=True, random_state=42)

    print("Vectorizing text with TF-IDF...")
    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english',
                                 ngram_range=(1, 2), min_df=2)
    x_train = vectorizer.fit_transform(newsgroups_train.data)
    x_test = vectorizer.transform(newsgroups_test.data)

    print("Training the Complement Naive Bayes classifier...")
    classifier = ComplementNB()
    classifier.fit(x_train, newsgroups_train.target)

    print("Saving model.joblib and vectorizer.joblib...")
    joblib.dump(classifier, 'model.joblib')
    joblib.dump(vectorizer, 'vectorizer.joblib')

    print("Evaluating on the test set...")
    y_pred = classifier.predict(x_test)
    report = classification_report(newsgroups_test.target, y_pred,
                                   target_names=newsgroups_train.target_names)
    with open('evaluation.txt', 'w', encoding='utf-8') as file:
        file.write(report)
    print(report)
    print("Done.")


if __name__ == '__main__':
    main()
