# PhishGuard AI

Machine Learning Based Phishing URL Detection

PhishGuard AI analyzes URLs using exactly six features and predicts Safe or Phishing.

## Features

1. URL length
2. Number of dots
3. Presence of @
4. HTTPS usage
5. IP address in URL
6. Suspicious keyword presence

## Models

- Decision Tree
- Random Forest

## Dataset

Source: Hassan-Albattra/URL_Phishing_Detection_Dataset

Final dataset: data/phishing_url_dataset.csv

340,000 URLs: 170,000 legitimate and 170,000 phishing.

## Results

### Decision Tree

- Accuracy: 82.52%
- Precision: 76.77%
- Recall: 93.21%
- F1 Score: 84.19%

Confusion Matrix: [[24425, 9575], [2305, 31640]]

### Random Forest

- Accuracy: 82.54%
- Precision: 76.77%
- Recall: 93.27%
- F1 Score: 84.22%

Confusion Matrix: [[24420, 9580], [2285, 31660]]

Random Forest is used by the Streamlit demo.

## Demo

Enter a URL, extract the six features, run the Random Forest model, and display Safe or Phishing.

## Run Locally

streamlit run app.py

## Technology Stack

Python, Pandas, Scikit-learn, Streamlit, Decision Tree, Random Forest

## Disclaimer

PhishGuard AI is an academic/hackathon demonstration and should not be treated as a replacement for professional cybersecurity systems.
