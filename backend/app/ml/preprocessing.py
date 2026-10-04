import pandas as pd
import numpy as np


def preprocess_input(data: dict, feature_names: list):

    row = {}

    for feature in feature_names:
        value = data.get(feature, 0)

        try:
            value = float(value)
        except (ValueError, TypeError):
            value = 0.0

        row[feature] = value

    df = pd.DataFrame(
        [row],
        columns=feature_names
    )

    df = df.replace(
        [np.inf, -np.inf],
        0
    )

    df = df.fillna(0)

    return df