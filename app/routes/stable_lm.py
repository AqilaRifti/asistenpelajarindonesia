from typing import Optional
from app.api_router import api_router
from app.models import stable_lm_provider
from app.constants import DEFAULT_MAX_NEW_TOKENS
from app.logger import primary_logger

primary_logger.name = __name__

@api_router.get("/stable/{query}", tags=["stable"])
async def stable_response(query: str, max_new_tokens: Optional[int] = DEFAULT_MAX_NEW_TOKENS):
    try:
        return {
            "answer": stable_lm_provider.stable_lm(query, max_new_tokens=max_new_tokens)
        }
    finally:
        primary_logger.info(query)
