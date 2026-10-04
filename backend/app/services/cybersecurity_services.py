from app.ml.predictor import CybersecurityPredictor
from app.ml.preprocessing import preprocess_input
from app.ml.explain import explain_prediction

from app.rag.retriever import CybersecurityRetriever
from app.rag.generator import GeminiGenerator


class CybersecurityService:

    def __init__(self):

        self.predictor = CybersecurityPredictor()
        self.retriever = CybersecurityRetriever()
        self.generator = GeminiGenerator()

    def analyze(self, network_data):

        dataframe = preprocess_input(
            network_data,
            self.predictor.feature_names
        )

        prediction = self.predictor.predict(
            dataframe
        )

        explanations = explain_prediction(
            self.predictor.model,
            dataframe
        )

        query = (
            f"Cybersecurity threat analysis for "
            f"{prediction['prediction']} network traffic. "
            f"Important features: "
            f"{', '.join(item['feature'] for item in explanations[:5])}"
        )

        retrieved_documents = (
            self.retriever.retrieve(
                query
            )
        )

        explanation = self.generator.generate(
            attack_prediction=prediction["prediction"],
            confidence=prediction["confidence"],
            feature_explanations=explanations,
            retrieved_documents=retrieved_documents
        )

        sources = [
            {
                "source": metadata.get("source"),
                "file": metadata.get("file")
            }
            for _, metadata in retrieved_documents
        ]

        return {
            "prediction": prediction,
            "feature_explanations": explanations,
            "retrieved_sources": sources,
            "ai_explanation": explanation
        }