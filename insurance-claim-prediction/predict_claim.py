import joblib
import pandas as pd


# ============================================================
# INSURANCE CLAIM PREDICTION & RISK ANALYSIS
# PREDICTION SYSTEM
# ============================================================

MODEL_PATH = "models/insurance_claim_model.pkl"


# ============================================================
# LOAD MODEL
# ============================================================

try:

    model_package = joblib.load(
        MODEL_PATH
    )

    model = model_package["model"]

    model_name = model_package["model_name"]

except FileNotFoundError:

    print("ERROR: Model belum ditemukan.")

    print(
        "Jalankan terlebih dahulu:"
    )

    print(
        "python train_model.py"
    )

    exit()


# ============================================================
# FUNCTION INPUT
# ============================================================

def get_integer(
    message,
    minimum=None,
    maximum=None
):

    while True:

        try:

            value = int(
                input(message)
            )

            if minimum is not None:
                if value < minimum:
                    print(
                        f"Nilai minimal adalah {minimum}."
                    )
                    continue

            if maximum is not None:
                if value > maximum:
                    print(
                        f"Nilai maksimal adalah {maximum}."
                    )
                    continue

            return value

        except ValueError:

            print(
                "Masukkan angka yang valid."
            )


def get_float(
    message,
    minimum=None,
    maximum=None
):

    while True:

        try:

            value = float(
                input(message)
            )

            if minimum is not None:
                if value < minimum:
                    print(
                        f"Nilai minimal adalah {minimum}."
                    )
                    continue

            if maximum is not None:
                if value > maximum:
                    print(
                        f"Nilai maksimal adalah {maximum}."
                    )
                    continue

            return value

        except ValueError:

            print(
                "Masukkan angka yang valid."
            )


def get_choice(
    message,
    choices
):

    while True:

        value = input(
            message
        ).strip()

        if value in choices:
            return value

        print(
            "Pilihan tidak valid."
        )

        print(
            "Pilihan:",
            ", ".join(choices)
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

print("\n")

print("=" * 70)

print(
    "INSURANCE CLAIM PREDICTION & RISK ANALYSIS"
)

print("=" * 70)

print(
    f"Model: {model_name}"
)

print()


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

print("-" * 70)

print("CUSTOMER INFORMATION")

print("-" * 70)

age = get_integer(
    "Age (18-70): ",
    18,
    70
)

gender = get_choice(
    "Gender (Male/Female): ",
    [
        "Male",
        "Female"
    ]
)

annual_income = get_integer(
    "Annual Income (IDR): ",
    25000000,
    250000000
)


# ============================================================
# POLICY INFORMATION
# ============================================================

print("\n" + "-" * 70)

print("POLICY INFORMATION")

print("-" * 70)

policy_type = get_choice(
    "Policy Type (Basic/Standard/Premium): ",
    [
        "Basic",
        "Standard",
        "Premium"
    ]
)

policy_tenure = get_integer(
    "Policy Tenure (years): ",
    1,
    10
)

premium_amount = get_integer(
    "Premium Amount (IDR): ",
    1000000,
    15000000
)


# ============================================================
# VEHICLE INFORMATION
# ============================================================

print("\n" + "-" * 70)

print("VEHICLE INFORMATION")

print("-" * 70)

vehicle_type = get_choice(
    "Vehicle Type "
    "(Sedan/SUV/Hatchback/Pickup/Motorcycle): ",
    [
        "Sedan",
        "SUV",
        "Hatchback",
        "Pickup",
        "Motorcycle"
    ]
)

vehicle_age = get_integer(
    "Vehicle Age (0-15): ",
    0,
    15
)


# ============================================================
# CLAIM HISTORY
# ============================================================

print("\n" + "-" * 70)

print("CLAIM HISTORY")

print("-" * 70)

previous_claims = get_integer(
    "Previous Claims (0-6): ",
    0,
    6
)

accident_history = get_choice(
    "Accident History (Yes/No): ",
    [
        "Yes",
        "No"
    ]
)


# ============================================================
# DRIVING BEHAVIOR
# ============================================================

print("\n" + "-" * 70)

print("DRIVING BEHAVIOR")

print("-" * 70)

annual_mileage = get_integer(
    "Annual Mileage (3000-50000 km): ",
    3000,
    50000
)

traffic_violations = get_integer(
    "Traffic Violations (0-7): ",
    0,
    7
)


# ============================================================
# OCCUPATION
# ============================================================

print("\n" + "-" * 70)

print("PERSONAL INFORMATION")

print("-" * 70)

occupation = get_choice(
    "Occupation "
    "(Office Worker/Business Owner/Student/Driver/Engineer/Teacher): ",
    [
        "Office Worker",
        "Business Owner",
        "Student",
        "Driver",
        "Engineer",
        "Teacher"
    ]
)


# ============================================================
# CREATE INPUT DATA
# ============================================================

customer_data = pd.DataFrame({

    "Age": [
        age
    ],

    "Gender": [
        gender
    ],

    "Annual_Income": [
        annual_income
    ],

    "Policy_Type": [
        policy_type
    ],

    "Policy_Tenure": [
        policy_tenure
    ],

    "Premium_Amount": [
        premium_amount
    ],

    "Vehicle_Type": [
        vehicle_type
    ],

    "Vehicle_Age": [
        vehicle_age
    ],

    "Previous_Claims": [
        previous_claims
    ],

    "Accident_History": [
        accident_history
    ],

    "Annual_Mileage": [
        annual_mileage
    ],

    "Traffic_Violations": [
        traffic_violations
    ],

    "Occupation": [
        occupation
    ]

})


# ============================================================
# PREDICTION
# ============================================================

prediction = model.predict(
    customer_data
)[0]

probability = model.predict_proba(
    customer_data
)[0][1]

claim_probability = (
    probability * 100
)


# ============================================================
# RISK LEVEL
# ============================================================

if claim_probability < 30:

    risk_level = "LOW"

elif claim_probability < 70:

    risk_level = "MEDIUM"

else:

    risk_level = "HIGH"


# ============================================================
# RECOMMENDATION
# ============================================================

if risk_level == "LOW":

    recommendation = (
        "Customer memiliki risiko klaim rendah. "
        "Policy dapat dipertimbangkan dengan monitoring standar."
    )

elif risk_level == "MEDIUM":

    recommendation = (
        "Customer memiliki risiko klaim sedang. "
        "Disarankan melakukan review tambahan sebelum approval."
    )

else:

    recommendation = (
        "Customer memiliki risiko klaim tinggi. "
        "Disarankan melakukan risk assessment lebih mendalam."
    )


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n")

print("=" * 70)

print("INSURANCE CLAIM PREDICTION RESULT")

print("=" * 70)

print()

if prediction == 1:

    print(
        "CLAIM PREDICTION : YES"
    )

else:

    print(
        "CLAIM PREDICTION : NO"
    )

print(
    f"CLAIM PROBABILITY: {claim_probability:.2f}%"
)

print(
    f"RISK SCORE       : {claim_probability:.2f}"
)

print(
    f"RISK LEVEL       : {risk_level}"
)

print()

print(
    "RECOMMENDATION:"
)

print(
    recommendation
)

print()

print("=" * 70)

print(
    "Prediction completed."
)

print("=" * 70)