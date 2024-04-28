import requests
from typing import Any, Optional
from app.constants import BASIC_MODEL_API_KEY, WIZARD_LM_ID, INDONESIAN_PROMPT_TEMPLATE
from app.embedding_loader import get_context

MODEL_ID = WIZARD_LM_ID
BASETEN_API_KEY = BASIC_MODEL_API_KEY

def wizard_lm(prompt: str, max_new_tokens: Optional[int] = 512) -> Any:
    query = INDONESIAN_PROMPT_TEMPLATE.format(context=get_context(prompt, "/Users/aqila/BIA/backend/models/chroma-mini-gtr-t5-4800-200"), question=prompt)
    data = {
        "prompt": query,
        "max_new_tokens": max_new_tokens
    }

    res = requests.post(
        f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
        json=data
    )

    return res.json()