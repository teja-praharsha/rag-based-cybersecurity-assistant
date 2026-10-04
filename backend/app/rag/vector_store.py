import chromadb

from app.config import CHROMA_PATH


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_PATH)
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="cybersecurity_knowledge"
            )
        )

    def add_documents(
        self,
        documents,
        embeddings,
        metadatas,
        ids
    ):

        self.collection.add(
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            ids=ids
        )

    def search(
        self,
        embedding,
        top_k=5
    ):

        result = self.collection.query(
            query_embeddings=[
                embedding.tolist()
            ],
            n_results=top_k
        )

        documents = result.get(
            "documents",
            [[]]
        )[0]

        metadatas = result.get(
            "metadatas",
            [[]]
        )[0]

        return list(
            zip(
                documents,
                metadatas
            )
        )