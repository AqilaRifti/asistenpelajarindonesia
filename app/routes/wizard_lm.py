from typing import Optional
from app.api_router import api_router
from app.models import wizard_lm_provider
from app.constants import DEFAULT_MAX_NEW_TOKENS


@api_router.get("/wizard/{query}", tags=["wizard"])
async def wizard_response(query: str, max_new_tokens: Optional[int] = DEFAULT_MAX_NEW_TOKENS):
    return {
        "answer": wizard_lm_provider.wizard_lm(query, max_new_tokens=max_new_tokens)
    }

