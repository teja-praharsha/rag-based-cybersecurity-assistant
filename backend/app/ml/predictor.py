import joblib

from app.config import (
    MODEL_PATH,
    ENCODER_PATH
)


class CybersecurityPredictor:

    def __init__(self):

        self.model = joblib.load(
            MODEL_PATH
        )

        self.encoder = joblib.load(
            ENCODER_PATH
        )

        self.feature_names = list(
            self.model.feature_names_in_
        )

    def predict(self, dataframe):

        prediction = self.model.predict(
            dataframe
        )[0]

        probabilities = self.model.predict_proba(
            dataframe
        )[0]

        label = self.encoder.inverse_transform(
            [prediction]
        )[0]

        confidence = float(
            max(probabilities)
        )

        return {
            "prediction": str(label),
            "confidence": confidence,
            "probabilities": {
                str(class_name): float(probability)
                for class_name, probability
                in zip(
                    self.encoder.classes_,
                    probabilities
                )
            }
        }