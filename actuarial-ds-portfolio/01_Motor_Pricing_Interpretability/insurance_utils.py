import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
from tensorflow.keras import backend as K


def load_and_preprocess_data():
    """
    Fetches the French MTPL dataset and applies basic actuarial cleaning.
    Used across both XGBoost and Neural Network pipelines.
    """
    print("Fetching data from OpenML...")
    df = fetch_openml(data_id=41214, as_frame=True).frame

    # Actuarial clipping: common practice to handle outliers in frequency modeling
    df["Exposure"] = df["Exposure"].clip(upper=1)
    df["ClaimNb"] = df["ClaimNb"].clip(upper=4)

    # Feature selection - keeping it consistent for both models
    features = [
        "ClaimNb",
        "Exposure",
        "Area",
        "VehPower",
        "VehAge",
        "DrivAge",
        "BonusMalus",
        "VehBrand",
        "VehGas",
        "Density",
        "Region",
    ]

    return df[features]


def get_poisson_loss_stable(y_true, y_pred):
    """
    Custom Poisson Loss function for Keras to ensure numerical stability.
    Uses K.epsilon() to avoid log(0) errors during training.
    """
    return K.mean(y_pred - y_true * K.log(y_pred + K.epsilon()), axis=-1)


if __name__ == "__main__":
    print("--- Starting Data Verification ---")
    try:
        data = load_and_preprocess_data()
        print(f"✅ Success! Data Shape: {data.shape}")
        print(data.head())
    except Exception as e:
        print(f"❌ An error occurred: {e}")
