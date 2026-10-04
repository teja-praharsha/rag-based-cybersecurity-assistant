from google import genai

from app.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


class GeminiGenerator:

    def __init__(self):

        if not GEMINI_API_KEY:
            self.client = None
        else:
            self.client = genai.Client(
                api_key=GEMINI_API_KEY
            )

    def generate(
        self,
        attack_prediction,
        confidence,
        feature_explanations,
        retrieved_documents
    ):

        context = "\n\n".join(
            [
                f"Source: {metadata.get('source')}\n"
                f"{document}"
                for document, metadata
                in retrieved_documents
            ]
        )

        features = "\n".join(
            [
                f"- {item['feature']}: "
                f"value={item['value']}, "
                f"importance={item['importance']:.4f}"
                for item in feature_explanations
            ]
        )

        prompt = f"""
You are a cybersecurity analysis assistant.

Analyze the following machine-learning detection.

Predicted attack:
{attack_prediction}

Prediction confidence:
{confidence:.2%}

Important features:
{features}

Retrieved cybersecurity knowledge:
{context}

Provide:

1. Threat explanation
2. Why the model produced this prediction
3. Important evidence
4. Recommended defensive actions
5. Relevant cybersecurity knowledge sources

Do not invent facts that are not supported by the supplied evidence.

Clearly state that the result is an AI-assisted analysis and should be validated by a cybersecurity professional.
"""

        if self.client is None:

            return (
                "Gemini API key is not configured. "
                "The ML prediction and retrieved evidence "
                "are still available."
            )

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text