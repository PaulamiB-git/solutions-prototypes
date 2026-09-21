import pandas as pd
import xgboost as xgb
from insurance_utils import load_and_preprocess_data
from sklearn.model_selection import train_test_split


def train_production_model():
    print("🚀 Starting Production Training...")

    # 1. Load data using our utility
    df = load_and_preprocess_data()

    # 2. Basic Preprocessing
    X = pd.get_dummies(df.drop(["ClaimNb", "Exposure"], axis=1), drop_first=True)
    y = df["ClaimNb"]
    exposure = df["Exposure"]

    # 3. Model Definition (using the parameters we found in NB 01)
    model = xgb.XGBRegressor(
        objective="count:poisson", n_estimators=100, learning_rate=0.1, max_depth=6
    )

    # 4. Fit
    print("Fitting XGBoost model...")
    model.fit(X, y, sample_weight=exposure)

    # 5. Save the model
    model.save_model("champion_model.json")
    print("✅ Model saved as champion_model.json")


if __name__ == "__main__":
    train_production_model()
