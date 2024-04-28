import chromadb
from typing import Optional, List
from langchain_ai21 import AI21Embeddings
from chromadb.utils import embedding_functions
from langchain_core.embeddings import Embeddings
from langchain.vectorstores.chroma import Chroma

MAX_EMBEDDING_RESULT = 10

AI21_EMBEDDING_DATABASE_PATH = "/home/aqilarifti/asistenpelajarindonesia/database/vector/chroma-ai21-v1"
MINI_LM_L6_EMBEDDING_DATABASE_PATH = "/home/aqilarifti/asistenpelajarindonesia/database/vector/chroma-mini-language-model-l6-v1"
MINI_LM_L12_EMBEDDING_DATABASE_PATH = "/home/aqilarifti/asistenpelajarindonesia/database/vector/chroma-mini-language-model-l12-v1"

DEFAULT_COLLECTION_NAME = "vector_collections"

MINI_LM_L6_EMBEDDINGS_FUNCTION = embedding_functions.DefaultEmbeddingFunction()
MINI_LM_L12_EMBEDDINGS_FUNCTION = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L12-v2")
AI21_DEFAULT_EMBEDDINGS_FUNCTION = AI21Embeddings(api_key="nCiGPqPAS8XekHtDAudmWT9dSBTM0Kga")

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

INDONESIAN_PROMPT_TEMPLATE = """
Jawab pertanyaan berdasarkan informasi berikut:

{context}

---

Jawab pertanyaan ini berdasarkan konteks diatas: {question}
"""

def get_context_ai21(
        query: str,
        embedding_database_path: Optional[str] = AI21_EMBEDDING_DATABASE_PATH,
        embedding_function: Optional[Embeddings] = AI21_DEFAULT_EMBEDDINGS_FUNCTION,
        k: Optional[int] = MAX_EMBEDDING_RESULT
    ) -> List[str]:
    client = Chroma(persist_directory=embedding_database_path, embedding_function=embedding_function)
    results = client.similarity_search(query=query, k=k)

    return "".join([result.page_content for result in results])


# TODO: fix return of documents being too short
def get_context_l6(
        query: str,
        collection_name: Optional[str] = DEFAULT_COLLECTION_NAME,
        embedding_database_path: str = MINI_LM_L6_EMBEDDING_DATABASE_PATH,
        embedding_function: Optional[Embeddings] = MINI_LM_L6_EMBEDDINGS_FUNCTION,
        k: Optional[int] = MAX_EMBEDDING_RESULT
    ) -> List[str]:
    client = chromadb.PersistentClient(path=embedding_database_path)
    collection = client.get_collection(
        name=collection_name,
        embedding_function=embedding_function,
    )
    query_results = collection.query(
        query_texts=[query],
        n_results=k,
    )
    return "".join([query_results["documents"][counter][counter] for counter in range(len(query_results["documents"]))])


# TODO: fix return of documents being too short
def get_context_l12(
        query: str,
        collection_name: Optional[str] = DEFAULT_COLLECTION_NAME,
        embedding_database_path: str = MINI_LM_L12_EMBEDDING_DATABASE_PATH,
        embedding_function: Optional[Embeddings] = MINI_LM_L12_EMBEDDINGS_FUNCTION,
        k: Optional[int] = MAX_EMBEDDING_RESULT
    ) -> List[str]:
    client = chromadb.PersistentClient(path=embedding_database_path)
    collection = client.get_collection(
        name=collection_name,
        embedding_function=embedding_function,
    )
    query_results = collection.query(
        query_texts=[query],
        n_results=k,
    )
    return "".join([query_results["documents"][counter][counter] for counter in range(len(query_results["documents"]))])


def generate_prompt_english(query: str) -> str:
    return PROMPT_TEMPLATE.format(
        context=get_context_ai21(query), 
        question=query
    )


def generate_prompt_indonesia(query: str) -> str:
    return INDONESIAN_PROMPT_TEMPLATE.format(
        context=get_context_ai21(query),
        question=query
    )
