import os
import numpy as np
import pandas as pd

# ============================================================
# INSURANCE CLAIM PREDICTION
# DATASET GENERATOR
# ============================================================

np.random.seed(42)

# Jumlah data
N = 3000

# ============================================================
# CUSTOMER INFORMATION
# ============================================================

customer_id = np.arange(100001, 100001 + N)

age = np.random.randint(18, 71, N)

gender = np.random.choice(
    ["Male", "Female"],
    N
)

annual_income = np.random.randint(
    25000000,
    250000001,
    N
)

# ============================================================
# POLICY INFORMATION
# ============================================================

policy_type = np.random.choice(
    ["Basic", "Standard", "Premium"],
    N,
    p=[0.35, 0.45, 0.20]
)

policy_tenure = np.random.randint(
    1,
    11,
    N
)

premium_amount = np.random.randint(
    1000000,
    15000001,
    N
)

# ============================================================
# VEHICLE INFORMATION
# ============================================================

vehicle_type = np.random.choice(
    ["Sedan", "SUV", "Hatchback", "Pickup", "Motorcycle"],
    N
)

vehicle_age = np.random.randint(
    0,
    16,
    N
)

# ============================================================
# CLAIM HISTORY
# ============================================================

previous_claims = np.random.poisson(
    1.2,
    N
)

previous_claims = np.clip(
    previous_claims,
    0,
    6
)

accident_history = np.random.choice(
    ["Yes", "No"],
    N,
    p=[0.30, 0.70]
)

# ============================================================
# DRIVING BEHAVIOR
# ============================================================

annual_mileage = np.random.randint(
    3000,
    50001,
    N
)

traffic_violations = np.random.poisson(
    1.0,
    N
)

traffic_violations = np.clip(
    traffic_violations,
    0,
    7
)

# ============================================================
# OCCUPATION
# ============================================================

occupation = np.random.choice(
    [
        "Office Worker",
        "Business Owner",
        "Student",
        "Driver",
        "Engineer",
        "Teacher"
    ],
    N
)

# ============================================================
# CREATE CLAIM PROBABILITY
# ============================================================

risk_score = (
    0.45
    + (previous_claims * 0.08)
    + (vehicle_age * 0.015)
    + (annual_mileage / 100000 * 0.10)
    + (traffic_violations * 0.04)
    + (np.array(accident_history) == "Yes") * 0.18
    + (age < 25) * 0.08
)

# Policy effect
risk_score += np.where(
    np.array(policy_type) == "Premium",
    -0.04,
    0
)

risk_score += np.where(
    np.array(policy_type) == "Basic",
    0.04,
    0
)

# Random noise
risk_score += np.random.normal(
    0,
    0.08,
    N
)

# Probability antara 0.05 - 0.95
claim_probability = np.clip(
    risk_score,
    0.05,
    0.95
)

# Generate claim
claim = np.random.binomial(
    1,
    claim_probability
)

# ============================================================
# CLAIM AMOUNT
# ============================================================

claim_amount = np.where(
    claim == 1,
    np.random.randint(
        1000000,
        100000001,
        N
    ),
    0
)

# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({

    "Customer_ID": customer_id,

    "Age": age,

    "Gender": gender,

    "Annual_Income": annual_income,

    "Policy_Type": policy_type,

    "Policy_Tenure": policy_tenure,

    "Premium_Amount": premium_amount,

    "Vehicle_Type": vehicle_type,

    "Vehicle_Age": vehicle_age,

    "Previous_Claims": previous_claims,

    "Accident_History": accident_history,

    "Annual_Mileage": annual_mileage,

    "Traffic_Violations": traffic_violations,

    "Occupation": occupation,

    "Claim": claim,

    "Claim_Amount": claim_amount

})

# ============================================================
# SAVE DATASET
# ============================================================

os.makedirs(
    "data",
    exist_ok=True
)

file_path = "data/insurance_claims.csv"

df.to_csv(
    file_path,
    index=False
)

# ============================================================
# DISPLAY RESULT
# ============================================================

print("=" * 60)
print("INSURANCE CLAIM DATASET GENERATOR")
print("=" * 60)

print()

print(
    f"Dataset berhasil dibuat: {file_path}"
)

print(
    f"Jumlah data: {len(df)}"
)

print(
    f"Jumlah kolom: {len(df.columns)}"
)

print()

print("5 data pertama:")

print(
    df.head()
)

print()

print("Distribusi Claim:")

print(
    df["Claim"].value_counts()
)

print()

print("Dataset selesai.")