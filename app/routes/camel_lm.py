from typing import Optional
from app.api_router import api_router
from app.models import camel_lm_provider
from app.constants import DEFAULT_MAX_NEW_TOKENS
from app.logger import primary_logger

primary_logger.name = __name__

@api_router.get("/camel/{query}", tags=["camel"])
async def camel_response(query: str, max_new_tokens: Optional[int] = DEFAULT_MAX_NEW_TOKENS):
    try:
        return {
            "answer": camel_lm_provider.camel_lm(query, max_new_tokens=max_new_tokens)
        }
    finally:
        primary_logger.info(query)
