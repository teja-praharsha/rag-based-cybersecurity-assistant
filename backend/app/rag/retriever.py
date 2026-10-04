from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


class CybersecurityRetriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query,
        top_k=5
    ):

        embedding = self.embedding_model.encode(
            [query]
        )[0]

        return self.vector_store.search(
            embedding,
            top_k
        )