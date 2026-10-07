# PhishGuard AI

## Live Application

PhishGuard AI is deployed and available as a live Streamlit application.

Live Demo

https://phishguard-ai-ho5hql5sepq4dbwxgo2dod.streamlit.app/

## Project Overview

PhishGuard AI is a machine learning based phishing URL detection system designed to identify potentially malicious URLs and classify them as safe or phishing.

The system analyzes URL characteristics using six predefined features and applies machine learning models to determine whether a URL is likely to be legitimate or phishing.

The project combines data preprocessing, feature engineering, machine learning model development, model evaluation, and real time prediction through a Streamlit web application.

## Problem Statement

Phishing attacks commonly use deceptive and malicious URLs to trick users into visiting fraudulent websites and providing sensitive information.

The objective of this project is to develop a lightweight machine learning based solution that can analyze URL characteristics and classify URLs as safe or phishing without depending on external security APIs.

## Proposed Solution

PhishGuard AI follows a structured machine learning pipeline.

A labelled URL dataset is prepared and processed for model training.

Six URL based features are extracted from each URL.

The processed dataset is divided into training and testing data.

Decision Tree and Random Forest classification models are trained using the extracted features.

The models are evaluated using accuracy, precision, recall, F1 score, and confusion matrix.

The Random Forest model is integrated into a Streamlit application for real time URL classification.

## URL Features

The system uses exactly six features.

URL Length

Number of Dots

Presence of the At Symbol

HTTPS Usage

Presence of an IP Address

Suspicious Keyword Detection

These features are extracted consistently during both model training and real time prediction.

## Machine Learning Models

The project implements two classification algorithms.

Decision Tree

Random Forest

Both models are trained using the same six URL based features and evaluated on the same test dataset.

Random Forest is selected for the final application because it achieved slightly better overall performance during evaluation.

## Model Performance

Decision Tree

Accuracy: 82.52 percent

Precision: 76.77 percent

Recall: 93.21 percent

F1 Score: 84.19 percent

Confusion Matrix: 24425, 9575, 2305, 31640

Random Forest

Accuracy: 82.54 percent

Precision: 76.77 percent

Recall: 93.27 percent

F1 Score: 84.22 percent

Confusion Matrix: 24420, 9580, 2285, 31660

The Random Forest model is used by the deployed Streamlit application.

## Dataset

The project uses the URL Phishing Detection Dataset from Hassan Albattra.

The final dataset contains approximately 340000 URLs with legitimate and phishing URL samples.

The dataset is processed using Python and pandas before feature extraction and model training.

## Application Workflow

The user enters a URL into the Streamlit application.

The application extracts the six predefined URL features.

The extracted features are converted into the required model input format.

The trained Random Forest model analyzes the feature vector.

The model generates a classification result.

The application displays the prediction as Safe or Phishing.

The extracted feature values can also be viewed by the user.

## Technology Stack

Python

Pandas

Scikit learn

Streamlit

Git

GitHub

## Project Structure

PhishGuard AI

app.py

feature_extraction.py

requirements.txt

models

decision_tree.pkl

random_forest.pkl

MODEL_REPORT.md

data

phishing_url_dataset.csv

README.md

## Installation

Clone the repository.

Open the project directory.

Create and activate a Python virtual environment.

Install the required dependencies using the requirements file.

Example installation commands

git clone https://github.com/PrajwalGN-35/PhishGuard-AI.git

cd PhishGuard-AI

pip install -r requirements.txt

## Running Locally

Start the Streamlit application using the following command.

streamlit run app.py

The application will open in the browser and provide an interface for entering URLs and obtaining predictions.

## Live Demo

The trained Random Forest model is deployed using Streamlit Community Cloud.

Live Application

https://phishguard-ai-ho5hql5sepq4dbwxgo2dod.streamlit.app/

Users can enter a URL directly into the application and view the model prediction.

## Example Predictions

A legitimate website such as a standard HTTPS website can be classified as Safe.

A URL containing an IP address, suspicious keywords, or other phishing related characteristics can be classified as Phishing.

The prediction is based only on the six features used by the trained model.

## Key Project Highlights

Machine learning based cybersecurity solution

Two classification models implemented and compared

Six interpretable URL based features

Model evaluation using multiple classification metrics

Real time URL prediction

Streamlit based user interface

Live cloud deployment

GitHub based project management

## Project Objective

The primary objective of PhishGuard AI is to demonstrate how machine learning and feature engineering can be applied to a practical cybersecurity problem.

The project focuses on building an understandable and lightweight phishing detection pipeline that connects dataset preparation, feature extraction, machine learning, evaluation, and real time deployment.

## Future Scope

The system can be extended in future with additional URL and webpage characteristics, larger and continuously updated datasets, advanced machine learning models, automated threat intelligence integration, and browser based protection mechanisms.

These improvements are outside the current project scope and are not required for the present implementation.

## Contributors

PRAJWAL G N

MANOJ M N

LIKHITH GOWDA P

S KUNDHAN RAO PAWAR

## Disclaimer

PhishGuard AI is an academic and demonstration project.

The system makes predictions based only on the URL features used during model training. A Safe prediction does not guarantee that a website is completely secure, and a Phishing prediction should be treated as a warning rather than a definitive security verdict.

The project should not be considered a replacement for professional cybersecurity tools or security analysis.
