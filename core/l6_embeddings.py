import chromadb
from typing import List, Optional, Callable, Dict
from langchain.schema import Document
from chromadb.utils import embedding_functions

DEFAULT_METADATA = {"hnsw:space": "cosine"}
DEFAULT_COLLECTION_NAME = "vector_collections"
DEFAULT_EMBEDDING_FUNCTION = embedding_functions.DefaultEmbeddingFunction()

def generate_l6_embeddings(
        chunks: List[Document], 
        chroma_path: str, 
        metadata: Optional[Dict[str, str]] = DEFAULT_METADATA,
        collection_name: Optional[str] = DEFAULT_COLLECTION_NAME,
        embedding_function: Optional[Callable] = DEFAULT_EMBEDDING_FUNCTION,
    ):
    client = chromadb.PersistentClient(path=chroma_path)
    collection = client.create_collection(
        name=collection_name,
        embedding_function=embedding_function,
        metadata=metadata,
    )

    collection.add(
        documents=[chunk.page_content for chunk in chunks],
        ids=[f"id{i}" for i in range(len(chunks))]
    )

