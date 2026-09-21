import os
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

warnings.filterwarnings("ignore")


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "data/insurance_claims.csv"
MODEL_PATH = "models/insurance_claim_model.pkl"
OUTPUT_DIR = "outputs"

os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


# ============================================================
# 1. LOAD DATASET
# ============================================================

print("=" * 70)
print("INSURANCE CLAIM PREDICTION & RISK ANALYSIS")
print("=" * 70)

print("\n[1] Loading dataset...")

if not os.path.exists(DATA_PATH):
    print("\nERROR: Dataset tidak ditemukan!")
    print(f"Pastikan file ada di: {DATA_PATH}")
    print("\nJalankan terlebih dahulu:")
    print("python generate_dataset.py")
    exit()

df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded successfully: {df.shape}")


# ============================================================
# 2. DATA EXPLORATION
# ============================================================

print("\n" + "=" * 70)
print("[2] DATA EXPLORATION")
print("=" * 70)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ============================================================
# 3. DATA CLEANING
# ============================================================

print("\n" + "=" * 70)
print("[3] DATA CLEANING")
print("=" * 70)

df = df.drop_duplicates()

print(f"Data after cleaning: {df.shape}")


# ============================================================
# 4. CLAIM DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("[4] CLAIM DISTRIBUTION")
print("=" * 70)

print(df["Claim"].value_counts())

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Claim"
)

plt.title("Insurance Claim Distribution")

plt.xlabel("Claim Status")

plt.ylabel("Number of Customers")

plt.xticks(
    [0, 1],
    ["No Claim", "Claim"]
)

plt.tight_layout()

plt.savefig(
    "outputs/claim_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 5. DEFINE FEATURES AND TARGET
# ============================================================

print("\n" + "=" * 70)
print("[5] FEATURE ENGINEERING")
print("=" * 70)

# Customer_ID tidak digunakan sebagai fitur.
#
# Claim adalah target prediction.
#
# Claim_Amount tidak digunakan sebagai fitur karena jumlah
# klaim hanya diketahui setelah claim terjadi.

X = df.drop(
    columns=[
        "Customer_ID",
        "Claim",
        "Claim_Amount"
    ]
)

y = df["Claim"]


print("\nTarget:")
print("Claim")

print("\nFeatures:")

for column in X.columns:
    print("-", column)


# ============================================================
# 6. IDENTIFY DATA TYPES
# ============================================================

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical features:")
print(categorical_features)

print("\nNumeric features:")
print(numeric_features)


# ============================================================
# 7. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(

    transformers=[

        (
            "categorical",

            OneHotEncoder(
                handle_unknown="ignore"
            ),

            categorical_features
        ),

        (
            "numeric",

            "passthrough",

            numeric_features
        )

    ]
)


# ============================================================
# 8. TRAIN TEST SPLIT
# ============================================================

print("\n" + "=" * 70)
print("[6] TRAIN TEST SPLIT")
print("=" * 70)

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)

print(
    f"Training data: {X_train.shape}"
)

print(
    f"Testing data : {X_test.shape}"
)


# ============================================================
# 9. LOGISTIC REGRESSION
# ============================================================

print("\n" + "=" * 70)
print("[7] TRAINING LOGISTIC REGRESSION")
print("=" * 70)

logistic_model = Pipeline(

    steps=[

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",

            LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            )
        )

    ]
)

logistic_model.fit(
    X_train,
    y_train
)

print(
    "Logistic Regression training completed."
)


# ============================================================
# 10. RANDOM FOREST
# ============================================================

print("\n" + "=" * 70)
print("[8] TRAINING RANDOM FOREST")
print("=" * 70)

random_forest_model = Pipeline(

    steps=[

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",

            RandomForestClassifier(

                n_estimators=300,

                random_state=42,

                class_weight="balanced",

                max_depth=None

            )
        )

    ]
)

random_forest_model.fit(
    X_train,
    y_train
)

print(
    "Random Forest training completed."
)


# ============================================================
# 11. MODEL EVALUATION FUNCTION
# ============================================================

def evaluate_model(model, model_name):

    predictions = model.predict(
        X_test
    )

    probabilities = model.predict_proba(
        X_test
    )[:, 1]

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    auc = roc_auc_score(
        y_test,
        probabilities
    )

    print("\n" + "-" * 60)
    print(model_name)
    print("-" * 60)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC AUC  : {auc:.4f}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return {
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC AUC": auc
    }


# ============================================================
# 12. EVALUATE MODELS
# ============================================================

print("\n" + "=" * 70)
print("[9] MODEL EVALUATION")
print("=" * 70)

logistic_result = evaluate_model(
    logistic_model,
    "Logistic Regression"
)

random_forest_result = evaluate_model(
    random_forest_model,
    "Random Forest"
)


# ============================================================
# 13. MODEL COMPARISON
# ============================================================

results = pd.DataFrame([
    logistic_result,
    random_forest_result
])

print("\n" + "=" * 70)
print("[10] MODEL COMPARISON")
print("=" * 70)

print(
    results.to_string(
        index=False
    )
)

results.to_csv(
    "outputs/model_comparison.csv",
    index=False
)


# ============================================================
# 14. MODEL COMPARISON GRAPH
# ============================================================

results_melted = results.melt(

    id_vars="Model",

    value_vars=[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ],

    var_name="Metric",

    value_name="Score"

)

plt.figure(
    figsize=(11, 6)
)

sns.barplot(
    data=results_melted,
    x="Metric",
    y="Score",
    hue="Model"
)

plt.title(
    "Insurance Claim Prediction - Model Comparison"
)

plt.ylim(
    0,
    1
)

plt.tight_layout()

plt.savefig(
    "outputs/model_comparison.png",
    dpi=300
)

plt.close()


# ============================================================
# 15. SELECT BEST MODEL
# ============================================================

if (
    random_forest_result["ROC AUC"]
    >=
    logistic_result["ROC AUC"]
):

    best_model = random_forest_model

    best_model_name = "Random Forest"

    best_result = random_forest_result

else:

    best_model = logistic_model

    best_model_name = "Logistic Regression"

    best_result = logistic_result


print("\n" + "=" * 70)

print(
    f"BEST MODEL: {best_model_name}"
)

print("=" * 70)


# ============================================================
# 16. CONFUSION MATRIX
# ============================================================

best_predictions = best_model.predict(
    X_test
)

cm = confusion_matrix(
    y_test,
    best_predictions
)

plt.figure(
    figsize=(7, 5)
)

sns.heatmap(

    cm,

    annot=True,

    fmt="d",

    cmap="Blues",

    xticklabels=[
        "No Claim",
        "Claim"
    ],

    yticklabels=[
        "No Claim",
        "Claim"
    ]

)

plt.title(
    f"Confusion Matrix - {best_model_name}"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.tight_layout()

plt.savefig(
    "outputs/confusion_matrix.png",
    dpi=300
)

plt.close()


# ============================================================
# 17. CLAIM PROBABILITY
# ============================================================

print("\n" + "=" * 70)
print("[11] CLAIM PROBABILITY")
print("=" * 70)

all_probability = best_model.predict_proba(
    X
)[:, 1]

df["Claim_Probability"] = (
    all_probability * 100
).round(2)


# ============================================================
# 18. RISK SCORE
# ============================================================

df["Risk_Score"] = (
    df["Claim_Probability"]
)


def determine_risk(score):

    if score < 30:
        return "LOW"

    elif score < 70:
        return "MEDIUM"

    else:
        return "HIGH"


df["Risk_Level"] = (
    df["Risk_Score"]
    .apply(determine_risk)
)


# ============================================================
# 19. RISK DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("[12] RISK ANALYSIS")
print("=" * 70)

print("\nRisk distribution:")

print(
    df["Risk_Level"].value_counts()
)

plt.figure(
    figsize=(8, 5)
)

sns.countplot(

    data=df,

    x="Risk_Level",

    order=[
        "LOW",
        "MEDIUM",
        "HIGH"
    ]

)

plt.title(
    "Insurance Risk Distribution"
)

plt.xlabel(
    "Risk Level"
)

plt.ylabel(
    "Number of Customers"
)

plt.tight_layout()

plt.savefig(
    "outputs/risk_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 20. FEATURE IMPORTANCE
# ============================================================

if best_model_name == "Random Forest":

    classifier = (
        best_model
        .named_steps["classifier"]
    )

    fitted_preprocessor = (
        best_model
        .named_steps["preprocessor"]
    )

    feature_names = (
        fitted_preprocessor
        .get_feature_names_out()
    )

    importances = (
        classifier.feature_importances_
    )

    feature_importance = pd.DataFrame({

        "Feature": feature_names,

        "Importance": importances

    })

    feature_importance = (
        feature_importance
        .sort_values(
            by="Importance",
            ascending=False
        )
    )

    print("\n" + "=" * 70)
    print("TOP 15 RISK FACTORS")
    print("=" * 70)

    print(
        feature_importance
        .head(15)
        .to_string(
            index=False
        )
    )

    feature_importance.to_csv(
        "outputs/feature_importance.csv",
        index=False
    )

    plt.figure(
        figsize=(10, 7)
    )

    sns.barplot(

        data=feature_importance.head(15),

        x="Importance",

        y="Feature"

    )

    plt.title(
        "Top 15 Insurance Claim Risk Factors"
    )

    plt.xlabel(
        "Importance"
    )

    plt.ylabel(
        "Feature"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/feature_importance.png",
        dpi=300
    )

    plt.close()


# ============================================================
# 21. SAVE RISK ANALYSIS
# ============================================================

risk_columns = [

    "Customer_ID",
    "Age",
    "Gender",
    "Annual_Income",
    "Policy_Type",
    "Policy_Tenure",
    "Premium_Amount",
    "Vehicle_Type",
    "Vehicle_Age",
    "Previous_Claims",
    "Accident_History",
    "Annual_Mileage",
    "Traffic_Violations",
    "Occupation",
    "Claim",
    "Claim_Probability",
    "Risk_Score",
    "Risk_Level"

]

risk_analysis = df[
    risk_columns
]

risk_analysis.to_csv(
    "outputs/risk_analysis.csv",
    index=False
)


# ============================================================
# 22. SAVE MODEL
# ============================================================

model_package = {

    "model": best_model,

    "model_name": best_model_name,

    "features": X.columns.tolist(),

    "risk_rules": {

        "LOW": "< 30",

        "MEDIUM": "30 - 69.99",

        "HIGH": ">= 70"

    }

}

joblib.dump(
    model_package,
    MODEL_PATH
)


# ============================================================
# 23. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FINAL PROJECT SUMMARY")
print("=" * 70)

print(
    f"""
Total Customers       : {len(df):,}

Best Model            : {best_model_name}

Accuracy              : {best_result["Accuracy"]:.2%}

Precision             : {best_result["Precision"]:.2%}

Recall                : {best_result["Recall"]:.2%}

F1 Score              : {best_result["F1 Score"]:.2%}

ROC AUC               : {best_result["ROC AUC"]:.2%}

Low Risk              : {(df["Risk_Level"] == "LOW").sum():,}

Medium Risk           : {(df["Risk_Level"] == "MEDIUM").sum():,}

High Risk             : {(df["Risk_Level"] == "HIGH").sum():,}

Model File            : {MODEL_PATH}

Risk Analysis         : outputs/risk_analysis.csv
"""
)

print("=" * 70)

print("TRAINING SELESAI!")

print("=" * 70)