from app.config import KNOWLEDGE_BASE_PATH
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


def load_documents():

    documents = []

    for file in KNOWLEDGE_BASE_PATH.rglob("*.txt"):

        text = file.read_text(
            encoding="utf-8"
        )

        chunks = [
            text[i:i + 1000]
            for i in range(
                0,
                len(text),
                1000
            )
        ]

        for index, chunk in enumerate(chunks):

            documents.append({
                "text": chunk,
                "source": file.parent.name,
                "file": file.name,
                "id": f"{file.stem}_{index}"
            })

    return documents


def main():

    print("Loading cybersecurity knowledge base...")

    documents = load_documents()

    if not documents:
        raise ValueError(
            "No .txt files found in the knowledge base."
        )

    print(
        f"Found {len(documents)} document chunks."
    )

    print("Loading embedding model...")

    embedding_model = EmbeddingModel()

    print("Loading ChromaDB...")

    vector_store = VectorStore()

    texts = [
        document["text"]
        for document in documents
    ]

    print("Creating embeddings...")

    embeddings = embedding_model.encode(
        texts
    )

    metadatas = [
        {
            "source": document["source"],
            "file": document["file"]
        }
        for document in documents
    ]

    ids = [
        document["id"]
        for document in documents
    ]

    print("Adding documents to ChromaDB...")

    vector_store.add_documents(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    print()
    print("===================================")
    print("Knowledge base built successfully!")
    print("===================================")
    print(
        f"Documents added: {len(documents)}"
    )


if __name__ == "__main__":
    main()