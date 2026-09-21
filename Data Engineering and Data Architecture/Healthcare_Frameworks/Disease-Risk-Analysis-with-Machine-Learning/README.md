# Disease-Risk-Analysis-with-Machine-Learning

## Project Overview
This project aims to enhance disease risk prediction using a comprehensive dataset. The dataset includes clinical, demographic, and medication data. Various data mining and machine learning techniques were employed to develop robust predictive models.

## Table of Contents
- [Introduction](#introduction)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Model Development and Training](#model-development-and-training)
- [Model Evaluation and Selection](#model-evaluation-and-selection)
- [Unsupervised Learning and Cluster Analysis](#unsupervised-learning-and-cluster-analysis)
- [Achievements and Impact](#achievements-and-impact)
- [Files Included](#files-included)


## Introduction
This project integrates various data mining techniques to predict disease risk levels accurately. It involves extensive data cleaning, feature engineering, model training, and evaluation to ensure the reliability and precision of predictive models.

## Data Cleaning and Preprocessing
- Addressed missing values using KNN imputation and mode/mean imputation.
- Managed outliers with DBSCAN, Isolation Forest, and Local Outlier Factor (LOF) techniques.
- Standardized numerical variables to ensure uniformity in scale.

## Feature Engineering
- Developed new features such as 'age group' to enhance model inputs.
- Removed non-contributive columns and applied One-Hot and Ordinal Encoding to categorical variables.

## Model Development and Training
- Implemented multiple machine learning models: k-Nearest Neighbors, Support Vector Machine, Decision Tree, and Random Forest.
- Used grid search and cross-validation for hyperparameter tuning.
- Compared models using both full and refined feature sets.

## Model Evaluation and Selection
- Evaluated models using accuracy, precision, recall, and F1-score.
- Decision Tree model achieved the highest accuracy of 99%, making it the optimal choice.
- Analyzed confusion matrices to assess model performance across different risk categories.

## Unsupervised Learning and Cluster Analysis
- Applied KMeans and Hierarchical Clustering to identify natural groupings within the data.
- Validated the optimal number of clusters using the elbow method and silhouette scores.
- Compared clustering results with supervised learning outcomes for deeper insights.

## Achievements and Impact
- Enhanced disease risk classification accuracy, with the Decision Tree model achieving 99%.
- Balanced the dataset using manual upsampling and SMOTE techniques, ensuring robust model training and validation.
- Conducted extensive exploratory data analysis, providing insightful visualizations that aided in understanding the dataset's structure and relationships.
- Developed a robust feature engineering pipeline, improving model inputs and resulting in more accurate predictions.
- Successfully implemented and evaluated multiple machine learning models, showcasing versatility in handling healthcare data.
- Applied rigorous statistical analysis to ensure the integrity and reliability of the data, addressing outliers and ensuring proper scaling.
- Demonstrated the potential of data-driven approaches in healthcare analytics, contributing to improved patient care and decision-making processes.
- Shared detailed documentation and a comprehensive report, facilitating reproducibility and transparency of the project findings.
- Highlighted the importance of handling imbalanced datasets and provided practical solutions, benefiting future research and applications.
- Utilized advanced clustering techniques to uncover natural groupings within the data, offering new insights into disease risk factors.

## Files Included
- `Disease_Risk_Analysis.ipynb`: Jupyter notebook containing the code for data cleaning, feature engineering, model training, and evaluation.
- `DATA_MINING_REPORT.pdf`: Detailed report of the project, including methodologies, results, and insights.
- `predictions.csv`: CSV file containing the predictions made by the trained model.
- `disease_train.csv`: CSV file containing the training dataset used for model training.
- `disease_test.csv`: CSV file containing the test dataset used for model evaluation.

