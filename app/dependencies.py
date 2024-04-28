from typing import Annotated

from fastapi import Header, HTTPException

X_HEADER_TOKEN = "57ee184b9d9bc689929e2c43c40bb18e"
QUERY_TOKEN = "cce16cfba8532c3b5605cabedef970a0"

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != X_HEADER_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(query_token: str):
    if query_token != QUERY_TOKEN:
        raise HTTPException(status_code=400, detail="No query token provided")
    