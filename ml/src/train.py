from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


ROOT_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = ROOT_DIR / "ml" / "data" / "raw" / "startup_ideas.csv"
MODEL_PATH = ROOT_DIR / "ml" / "models" / "ridge_baseline.joblib"
COEFFICIENT_PATH = ROOT_DIR / "ml" / "models" / "ridge_coefficients.csv"


FEATURES = [
    "problem_clarity",
    "customer_urgency",
    "technical_complexity",
    "monetization_clarity",
    "acquisition_difficulty",
    "competition_level",
    "validation_evidence",
    "mvp_complexity",
]

TARGET = "overall_uncertainty"


def main():
    df = pd.read_csv(DATASET_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = Ridge()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    coefficients = pd.DataFrame({
        "Feature": FEATURES,
        "Coefficient": model.coef_,
    })

    coefficients.to_csv(COEFFICIENT_PATH, index=False)

    print("Training complete.")
    print(f"Dataset shape: {df.shape}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Coefficients saved to: {COEFFICIENT_PATH}")


if __name__ == "__main__":
    main()n