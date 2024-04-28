import random
from typing import Optional, List, Dict
from langchain_ai21 import ChatAI21
from langchain_ai21 import AI21Embeddings
from langchain.prompts import ChatPromptTemplate
from langchain_core.embeddings import Embeddings
from langchain.vectorstores.chroma import Chroma

from app.constants import (
    AI21_API_KEY,
    AI21_API_KEYS,
    PROMPT_TEMPLATE,
    AI21_CHROMA_PATH,
    AI21_EMBEDDING_FUNCTION
)


def ai21(query_text: str) -> str:
    MODEL = ChatAI21(api_key=random.choice(AI21_API_KEYS), model="j2-ultra", max_tokens=8191, min_tokens=100)
    return get_response(
        query_data(AI21_CHROMA_PATH, AI21_EMBEDDING_FUNCTION, query_text),
        MODEL,
        query_text
    )["text"]


def query_data(persist_directory: str, embedding_function: Embeddings, query_text: str, compare_embeddings: Optional[bool]=True, minimum_score: Optional[int]=0.7, k: Optional[int]=4) -> List[str]:
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_function)
    results = db.similarity_search_with_relevance_scores(query_text, k=k)
    if compare_embeddings:
        if len(results) == 0 or results[0][1] < minimum_score:
            return []
    return results

def get_response(
        context_results: List[str],
        model, 
        query_text: str, 
        get_sources: Optional[bool]=False, 
        context_text_template: Optional[str]="\n\n---\n\n",
        prompt_template: Optional[str]=PROMPT_TEMPLATE
    ) -> Dict[str, str]:
    response = {}
    context_text = context_text_template.join([doc.page_content for doc, _score in context_results])
    prompt_template = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt_template.format(context=context_text, question=query_text)
    response["text"] = model.invoke(prompt)

    if get_sources:
        sources = [doc.metadata.get("source", None) for doc, _score in context_results]
        response["sources"] = sources

    return response

