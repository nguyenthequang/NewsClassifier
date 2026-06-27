# Introduction

## News Classifier Web Application
This repository contains a Flask web application that uses a trained model to classify text into different categories. The application is designed to predict the category of user-inputted text using a pre-trained Complement Naive Bayes classifier. The model is trained on the 20 Newsgroups dataset, and it uses the TF-IDF vectorization technique to represent text data numerically. This could be used to allow inexerpienced writers to check is their work fit a certain topic or not.

The model achieves about **0.72 accuracy** on the 20 Newsgroups test set (with headers, footers, and quotes removed). The classifier and TF-IDF settings were selected by 3-fold cross-validation on the training set.
The website collects their text and:
1. Runs the saved predicting algorithm or train a new one if no saved algorithm is found

2. Directs the user to a different page where the answer will be given

3. Allows the user to see general informations about the website and to return to the home page to try another text

# Technical Overwiew
The web application is built using Python and Flask framework. Here's an overview of the key components:

1. app.py: This is the main Python file that contains the Flask application. It loads the pre-trained vectorizer and model once at startup, then handles GET and POST requests. The user's input text is preprocessed using the pre-trained TF-IDF vectorizer and classified using the pre-trained Complement Naive Bayes model. The predicted category is then rendered on the result page.

2. train.py: This script trains the model from scratch on the 20 Newsgroups dataset and saves model.joblib, vectorizer.joblib, and evaluation.txt. Run it once before first use, and again whenever you upgrade scikit-learn (saved models are not guaranteed to load across scikit-learn versions).

3. helper.py: This file contains a helper function translate_category_name that can be used to translate the category names into more user-friendly labels. You can customize this function to match your specific use case.

3. base.html: This HTML template file defines the overall design of the websites (layout, background, etc.). It includes a droplist for all 20 topics and an "About" button that give an overview about the page.

4. index.html: This HTML template file defines the index page of the web application. It includes a form where users can input their text for classification.

5. result.html: This HTML template file defines the result page of the web application. It displays the predicted category label for the user's input text.

6. evaluation.txt: This text file gives an overview about the model's evaluation metrics, like accuracy, precision, recall, etc.

6. model.joblib and vectorizer.joblib: These are pre-trained files that store the trained Complement Naive Bayes model and TF-IDF vectorizer, respectively. The application loads them at startup. If they are missing, run `python train.py` to generate them.

# Setup & Usage

## How to Install

To run this web application locally, follow these steps:

1. Clone this repository to your local machine or download the source code as a ZIP file.

2. Make sure you have Python 3.x installed on your system.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create and activate a virtual environment (recommended, so the project's packages stay isolated from your system Python):
```
python -m venv .venv
```
On Windows (PowerShell):
```
.\.venv\Scripts\Activate.ps1
```
On macOS / Linux:
```
source .venv/bin/activate
```

5. Install the required Python packages:
```
pip install -r requirements.txt
```

6. Generate the model and vectorizer (this downloads the 20 Newsgroups dataset and trains the classifier; only needed once, or after upgrading scikit-learn):
```
python train.py
```
## Usage
Once you have installed the necessary packages, you can start using the text classification web application. Follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the Flask application by executing the following command (or run with your IDE):
```
python app.py
```
3. By default, the Flask application will be running on http://localhost:5000.

4. Open a web browser and enter http://localhost:5000 in the address bar.

5. The index page of the web application will be displayed. Enter the text you want to classify into the input field and click the "Submit" button.

6. The application will process the input text, predict its category, and display the result on the result page.

7. You can continue to enter new text inputs and get predictions as desired.

## Customization
You can customize this web application to suit your specific requirements. Here are a few possible modifications you might consider:

1. Modify the HTML templates (index.html and result.html) to change the appearance and layout of the web pages.

2. Customize the translate_category_name function in helper.py to map the predicted category labels to your desired names.

3. Use your own dataset and modify the data preprocessing and model training steps in app.py to train a model on your specific data.

4. Update the routes and endpoints in app.py to add additional functionality or implement different features.