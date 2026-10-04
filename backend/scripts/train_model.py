from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "CIC-IDS2017-cleaned-combined.csv"
)

MODEL_DIR = BASE_DIR / "models"

MODEL_FILE = MODEL_DIR / "cybersecurity_model.joblib"
ENCODER_FILE = MODEL_DIR / "label_encoder.joblib"


def main():

    MODEL_DIR.mkdir(exist_ok=True)

    print("Loading dataset...")

    df = pd.read_csv(
        DATA_FILE,
        low_memory=False
    )

    df.columns = df.columns.str.strip()

    if "Label" not in df.columns:
        raise ValueError("Label column not found.")

    df = df.replace(
        [float("inf"), float("-inf")],
        pd.NA
    )

    df = df.dropna()

    y = df["Label"]

    X = df.drop(columns=["Label"])

    # Convert feature columns to numeric
    X = X.apply(
        pd.to_numeric,
        errors="coerce"
    )

    X = X.replace(
        [float("inf"), float("-inf")],
        pd.NA
    )

    valid_rows = X.notna().all(axis=1)

    X = X.loc[valid_rows]
    y = y.loc[valid_rows]

    # Encode target labels
    encoder = LabelEncoder()

    y_encoded = encoder.fit_transform(y)

    print("\nClasses:")
    for index, label in enumerate(encoder.classes_):
        print(index, "->", label)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.20,
        random_state=42,
        stratify=y_encoded
    )

    print("\nTraining Random Forest...")

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced"
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nAccuracy:")
    print(accuracy)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=encoder.classes_,
            zero_division=0
        )
    )

    print("\nConfusion Matrix:")
    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    # Save model
    joblib.dump(
        model,
        MODEL_FILE
    )

    joblib.dump(
        encoder,
        ENCODER_FILE
    )

    # Save feature names
    feature_file = MODEL_DIR / "feature_names.joblib"

    joblib.dump(
        list(X.columns),
        feature_file
    )

    print("\nModel saved:")
    print(MODEL_FILE)

    print("\nEncoder saved:")
    print(ENCODER_FILE)

    print("\nFeature names saved:")
    print(feature_file)


if __name__ == "__main__":
    main()