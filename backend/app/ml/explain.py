import pandas as pd


def explain_prediction(
    model,
    dataframe,
    top_n=10
):

    importances = model.feature_importances_

    features = dataframe.columns

    explanation = pd.DataFrame({
        "feature": features,
        "importance": importances,
        "value": dataframe.iloc[0].values
    })

    explanation = explanation.sort_values(
        by="importance",
        ascending=False
    )

    explanation = explanation.head(top_n)

    return explanation.to_dict(
        orient="records"
    )