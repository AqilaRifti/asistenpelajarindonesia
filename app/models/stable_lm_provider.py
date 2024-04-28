import requests
from typing import Any, Optional
from app.constants import BASIC_MODEL_API_KEY, STABLE_LM_ID

MODEL_ID = STABLE_LM_ID
BASETEN_API_KEY = BASIC_MODEL_API_KEY

def stable_lm(prompt: str, max_new_tokens: Optional[int] = 512, temperature: Optional[int] = 0.9) -> Any:
    data = {
        "prompt": prompt,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature
    }

    res = requests.post(
        f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
        json=data
    )

    return res.json()