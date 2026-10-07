# PhishGuard AI

## Project Overview

PhishGuard AI is a machine learning based phishing URL detection system designed to identify potentially malicious URLs and classify them as safe or phishing.

The system uses six URL based features including URL length, number of dots, presence of the at symbol, HTTPS usage, presence of an IP address, and suspicious keyword detection.

Two machine learning models, Decision Tree and Random Forest, are trained and evaluated using the same feature set. The models are compared using accuracy, precision, recall, F1 score, and confusion matrix.

The Random Forest model is integrated into a Streamlit application that allows users to enter a URL and receive a real time prediction.

## Problem Statement

Phishing attacks use deceptive URLs to trick users into visiting malicious websites and revealing sensitive information. Traditional detection methods may require external services or complex security infrastructure.

PhishGuard AI provides a lightweight machine learning based approach that analyzes URL characteristics and identifies potentially phishing URLs.

## Solution

The system follows a structured machine learning pipeline.

The dataset is cleaned and prepared for training.

Six relevant URL features are extracted from every URL.

The dataset is divided into training and testing sets.

Decision Tree and Random Forest models are trained using the extracted features.

Both models are evaluated using standard classification metrics.

The Random Forest model is integrated into the Streamlit application for real time prediction.

## Features

URL length

Number of dots

Presence of the at symbol

HTTPS usage

Presence of an IP address

Suspicious keyword detection

## Machine Learning Models

Decision Tree

Random Forest

The Random Forest model is used for the final Streamlit demonstration because it provides slightly better overall evaluation results than the Decision Tree model on the selected dataset.

## Dataset

The project uses the URL Phishing Detection Dataset from Hassan Albattra.

The final dataset contains approximately 340000 URLs with balanced legitimate and phishing classes.

The dataset is processed using Python and pandas before model training.

## Model Performance

Decision Tree achieved an accuracy of 82.52 percent with an F1 score of 84.19 percent.

Random Forest achieved an accuracy of 82.54 percent with an F1 score of 84.22 percent.

The Random Forest model achieved slightly better overall performance and is therefore used in the application.

## Technology Stack

Python

Pandas

Scikit learn

Streamlit

Git and GitHub

## Project Structure

PhishGuard AI

app.py

feature extraction.py

requirements.txt

models

decision tree.pkl

random forest.pkl

MODEL REPORT.md

data

phishing URL dataset.csv

README.md

## Installation

Clone the repository.

Open the project directory.

Create and activate a Python virtual environment if required.

Install the required dependencies using the requirements file.

## Running the Application

Run the Streamlit application using the following command.

streamlit run app.py

The application opens in the browser and allows the user to enter a URL for analysis.

## Prediction Process

The user enters a URL into the application.

The system extracts the six predefined URL features.

The features are passed to the trained Random Forest model.

The model predicts whether the URL is safe or phishing.

The prediction and extracted features are displayed in the application.

## Project Objective

The objective of PhishGuard AI is to demonstrate how machine learning can be applied to cybersecurity problems using interpretable URL based features and a simple real time prediction interface.

## Contributors

PRAJWAL GN

MANOJ M N

LIKHITH GOWDA P

S KUNDHAN RAO PAWAR

## Disclaimer

PhishGuard AI is an academic and demonstration project. The predictions are based only on the URL features used during model training and should not be considered a complete cybersecurity solution.
