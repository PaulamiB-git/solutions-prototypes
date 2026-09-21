# 🛡️ Insurance Claim Prediction & Risk Analysis

> A machine learning application for predicting insurance claim probability and analyzing customer risk levels through an interactive Streamlit dashboard.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 📌 Overview

**Insurance Claim Prediction & Risk Analysis** is an end-to-end machine learning project designed to predict the likelihood of an insurance claim and classify customers based on their predicted risk level.

The system analyzes customer, policy, vehicle, claim history, and driving behavior data to estimate the probability of a future insurance claim.

The prediction is converted into three risk categories:

| Claim Probability | Risk Level |
|---:|:---|
| < 30% | 🟢 LOW |
| 30% – 69% | 🟡 MEDIUM |
| ≥ 70% | 🔴 HIGH |

The project also includes an interactive **Streamlit dashboard** for prediction, risk analysis, dataset exploration, and machine learning model evaluation.

---

# 🎯 Business Problem

Insurance companies need efficient methods to evaluate customer risk and identify customers who may have a higher probability of submitting a claim.

Traditional risk assessment can involve manual analysis and may become difficult when dealing with large customer datasets.

This project demonstrates how machine learning can support insurance risk assessment by:

- Predicting insurance claim probability
- Identifying potentially high-risk customers
- Segmenting customers based on risk
- Analyzing factors associated with claim behavior
- Providing interactive decision-support analytics

> **Note:** This application is a machine learning prototype for educational and portfolio purposes and should not replace professional insurance underwriting decisions.

---

# 💡 Solution

The system follows an end-to-end machine learning workflow:

```text
Insurance Dataset
       │
       ▼
Data Preparation
       │
       ▼
Feature Engineering
       │
       ▼
Train / Test Split
       │
       ▼
Model Training
       │
       ├───────────────┐
       ▼               ▼
Logistic Regression  Random Forest
       │               │
       └───────┬───────┘
               ▼
       Model Evaluation
               │
               ▼
          Best Model
               │
       ┌───────┴────────┐
       ▼                ▼
Claim Prediction    Risk Analysis
       │                │
       ▼                ▼
Probability       LOW / MEDIUM / HIGH
       │
       ▼
Streamlit Dashboard