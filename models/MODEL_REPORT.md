# PhishGuard AI Model Report

## Dataset

Dataset: URL Phishing Detection Dataset

Source:
Hassan-Albattra/URL_Phishing_Detection_Dataset

Dataset composition:
- Legitimate URLs: 170,000
- Phishing URLs: 170,000
- Total: 340,000

After cleaning and duplicate removal:
- Rows: 339,723

## Features

Exactly six required features were used:

1. URL length
2. Number of dots
3. Presence of @
4. HTTPS usage
5. IP address presence
6. Suspicious keyword presence

No additional URL features were used.

## Train/Test Split

- Train: 271,778
- Test: 67,945
- Test size: 20%
- Random state: 42
- Stratified: yes

## Decision Tree

Accuracy: 0.825153
Precision: 0.767682
Recall: 0.932096
F1-score: 0.841937

Confusion matrix:

[[24425  9575]
 [ 2305 31640]]

## Random Forest

Accuracy: 0.825373
Precision: 0.767701
Recall: 0.932685
F1-score: 0.842189

Confusion matrix:

[[24420  9580]
 [ 2285 31660]]

## Selected Demo Model

Random Forest.

## Sanity Tests

Normal legitimate URLs classified Safe:
7/7

IP/login test:
Phishing

Secure-bank phishing test:
Phishing

The candidate model passed the practical sanity gate before promotion.
