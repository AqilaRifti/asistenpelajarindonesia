import random
from langchain_ai21 import AI21Embeddings
from chromadb.utils import embedding_functions


DEFAULT_EMBEDDINGS_FUNCTION = embedding_functions.DefaultEmbeddingFunction()
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

INDONESIAN_PROMPT_TEMPLATE = """
Jawab pertanyaan berikut berdasarkan informasi berikut:

{context}

---

Jawab pertanyaan ini berdasarkan konteks diatas: {question}
"""

NEWS_CLASSIFIER_PATH = "models/news_model/news_classifier_model.model"
FAKE_NEWS_CLASSIFIER_MODEL_PATH = "models/news_modal/fake_news_classifier_model.model"


HUGGINGFACE_ACCESS_TOKEN = "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"

BASIC_MODEL_API_KEY = "sqH6bmGy.ApPcCan8KfuA9NtxpZxmRPaNJZV44wFR"

WIZARD_LM_ID = "03ym08n3"
STABLE_LM_ID = "4w77gz0w"
ZEPHYR_LM_ID = "5qe7x81w"
CAMEL_LM_ID = "4q9o910q"


AI21_API_KEYS = [
    "793msO1RiB97TlQBK0z1C0w0xuN74Pbi",
    "A640eIX26QoJvWbgGx0LEeYHYx5F68rg",
    "nCiGPqPAS8XekHtDAudmWT9dSBTM0Kga",
    "hRF4iHVFSDyNcxZZ7BOk979FQLWpDNbF",
    "4iPLDhlhpkZf5E2tTmWILNgH2upb3gqt",
]

AI21_API_KEY = random.choice(AI21_API_KEYS)

AI21_CHROMA_PATH = "chroma-ai21"

DEFAULT_MAX_NEW_TOKENS = 512

MAX_EMBEDDING_RESULT = 3

TYPE_EMBEDDING = ...

COLLECTION_NAME = "demo_docs"

USER_DATABASE_PATH = ""

AI21_EMBEDDING_FUNCTION = AI21Embeddings(api_key=AI21_API_KEY)
MINI_LM_L6_EMBEDDING_FUNCTION = embedding_functions.DefaultEmbeddingFunction()
MINI_LM_L12_EMBEDDING_FUNCTION = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L12-v2")
