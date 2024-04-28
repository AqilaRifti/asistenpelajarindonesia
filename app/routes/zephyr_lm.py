from typing import Optional
from app.models import zephyr_lm_provider
from app.api_router import api_router
from app.constants import DEFAULT_MAX_NEW_TOKENS


@api_router.get("/zephyr/{query}", tags=["zephyr"])
async def zephyr_response(query: str, max_new_tokens: Optional[int] = DEFAULT_MAX_NEW_TOKENS):
    return {
        "answer": zephyr_lm_provider.zephyr_lm(query, max_new_tokens=max_new_tokens)
    }

