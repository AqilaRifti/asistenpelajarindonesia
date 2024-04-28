import os
from typing import List, Optional
from langchain.schema import Document
from langchain_ai21 import AI21Embeddings
from langchain.vectorstores.chroma import Chroma

DEFAULT_API_KEY = "4iPLDhlhpkZf5E2tTmWILNgH2upb3gqt"

def generate_ai21_embeddings(
        chunks: List[Document],
        chroma_path: str,
        api_key: Optional[str] = DEFAULT_API_KEY
    ) -> None:
    if os.path.exists(chroma_path):
        print("[ERROR] Directory Already Exist!")
        exit()

    db = Chroma.from_documents(
        chunks, AI21Embeddings(api_key=api_key), persist_directory=chroma_path
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {chroma_path}.")
