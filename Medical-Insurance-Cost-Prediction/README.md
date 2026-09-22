<h1><p align = "center"> Medical Insurance Cost Prediction</p></h1>

## PROJECT OVERVIEW
Health insurance costs have risen dramatically over the past decade in response to the rising cost of health care services and are determined by a multitude of factors. Let's look at the cost of healthcare for a sample of the population given age, sex, bmi, number of children, smoking habits, and region.

The purpose of this project is to determine the contributing factors and predict health insurance cost by performing exploratory data analysis and predictive modeling on the Health Insurance dataset. This project makes use of Numpy, Pandas, Sci-kit learn, and Data Visualization libraries.

<b>Overview:</b> <br>
• Seek insight from the dataset with Exploratory Data Analysis <br>
• Performed Data Processing, Data Engineering and Feature Transformation to prepare data before modeling <br>
• Built a model to predict Insurance Cost based on the features <br>
• Evaluated the model using various Performance Metrics like RMSE, R2, Testing Accuracy, Training Accuracy and MAE <br>

## DATA DESCRIPTION
1. age: age of primary beneficiary
2. sex: insurance contractor gender, female, male
3. bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
4. children: Number of children covered by health insurance / Number of dependents
5. smoker: Smoking
6. region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest
7. charges: Individual medical costs billed by health insurance

Data source : https://www.kaggle.com/mirichoi0218/insurance

## EXPLORATORY DATA ANALYSIS (EDA)
• Feature sex, region has an almost balanced amount, meanwhile most people are non smoker & obese <br>
![image](https://user-images.githubusercontent.com/80570935/130601931-826570ec-df1d-4b85-918f-00eb740ed212.png)

• A person who smoke and have BMI above 30 tends to have a higher medical cost <br>
![image](https://user-images.githubusercontent.com/80570935/130602334-b62a7f7e-e1c8-45eb-be7d-ff752853d158.png)

• Older people who smoke have more expensive charges <br>
![image](https://user-images.githubusercontent.com/80570935/130602565-2cb73fa9-769b-4822-880e-c009d2fbef39.png)

• People who smoke and obese have the highest average charges compared to others <br>
![image](https://user-images.githubusercontent.com/80570935/130602770-c008fb2b-2041-440e-b92e-373e7cbed2ce.png)

## INSIGHTS
The insights drawn by performing `Exploratory Data Analysis` (EDA) are:

- Most people are a non smokers & obese.
- Feature sex, region has an almost balanced amount.
- People who smoke & have a higher BMI, has higher medical charges.
- Older people who smoke have more expensive charges.
- An obese person who smokes have higher charges.

## DATA PROCESSING 
1. Check missing value - there are none <br>
2. Check duplicate value - there are 1 duplicate, will be remove <br>
3. Feature engineering - make a new column `weight_status` based on BMI score <br>
4. Feature transformation: <br>
 A) Encoding `sex`, `region`, & `weight_status` attributes <br>
 B) Ordinal encoding `smoker` attribute <br>
5. Modeling: <br>
 A) Separating target & features <br>
 B) Splitting train & test data <br>
 C) Modeling using Linear Regression, Random Forest, Decision Tree, Ridge, & Lasso algorithm <br>
 D) Find the best algorithm <br>
 E) Tuning Hyperparameter <br>
 
## MODEL EVALUATION 
| Score | LinearRegression | DecisionTree | RandomForest | Ridge |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| R2 | 0.77 | 0.78 | 0.78 | 0.86 |
| Train Accuracy | 0.74 | 1.0 | 0.97 | 0.74 |
| MAE | 4305.20 | 2798.83 | 2608.55 | 4311.10 |
| Test Accuracy | 0.77 | 0.78 | 0.86 | 0.77 | 
| RMSE | 6209.88 | 6067.50 | 4841.88 | 6238.13 |
 
## CONCLUSION
Based on the predictive modeling, Linear Regression algorithm has the best score compared to the others, with MAE Score 4305.20, RMSE Score 6209.88, & R2 Score 0.77. <br>

Therefore, Linear Regression algorithm is the best fitted model based on the training and testing accuracy.
