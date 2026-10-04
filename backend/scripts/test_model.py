import joblib
import pandas as pd

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "cybersecurity_model.joblib"
)

ENCODER_PATH = (
    BASE_DIR
    / "models"
    / "label_encoder.joblib"
)

FEATURE_PATH = (
    BASE_DIR
    / "models"
    / "feature_names.joblib"
)


def main():

    model = joblib.load(
        MODEL_PATH
    )

    encoder = joblib.load(
        ENCODER_PATH
    )

    features = joblib.load(
        FEATURE_PATH
    )

    sample = {
        feature: 0.0
        for feature in features
    }

    dataframe = pd.DataFrame(
        [sample],
        columns=features
    )

    prediction = model.predict(
        dataframe
    )[0]

    label = encoder.inverse_transform(
        [prediction]
    )[0]

    print(
        "Predicted class:",
        label
    )


if __name__ == "__main__":
    main()