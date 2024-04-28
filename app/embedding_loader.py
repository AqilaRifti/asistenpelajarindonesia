import chromadb
from typing import Optional, List
from chromadb.utils import embedding_functions
import pprint
from langchain.vectorstores.chroma import Chroma

from langchain_ai21 import AI21Embeddings
# from app.constants import (
#     TYPE_EMBEDDING,
#     COLLECTION_NAME,
#     MAX_EMBEDDING_RESULT,
#     DEFAULT_EMBEDDINGS_FUNCTION,
# )

MAX_EMBEDDING_RESULT = 10
EMBEDDING_DATABASE_PATH = "/home/aqilarifti/database/vector/chroma-ai21-v1"
TYPE_EMBEDDING = ...
DEFAULT_EMBED_MODEL = "sentence-transformers/all-MiniLM-L12-v2"

COLLECTION_NAME = "vector_collections"
DEFAULT_EMBEDDINGS_FUNCTION = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=DEFAULT_EMBED_MODEL)

USER_DATABASE_PATH = ""
DEFAULT_EMBEDDINGS_FUNCTION = AI21Embeddings(api_key="nCiGPqPAS8XekHtDAudmWT9dSBTM0Kga")


def get_context(
        query: str,
        embedding_database_path: str,
        default_embedding_function: Optional[TYPE_EMBEDDING] = DEFAULT_EMBEDDINGS_FUNCTION,
        k=MAX_EMBEDDING_RESULT
    ) -> List[str]:
    client = Chroma(persist_directory=embedding_database_path, embedding_function=default_embedding_function)

    #collection = client.get_collection(
    #    name=COLLECTION_NAME,
    #    embedding_function=default_embedding_function,
    #)
    #query_results = collection.query(
    #    query_texts=[query],
    #    n_results=k,
    #)
    result = client.similarity_search_with_score(query=query, k=k)
    data = [result[i][0] for i in range(len(result))]
    return data

results = get_context("apa itu puisi ", EMBEDDING_DATABASE_PATH)
pprint.pprint(results)