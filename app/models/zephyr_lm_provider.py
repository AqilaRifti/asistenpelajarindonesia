import requests
from typing import Any, Optional
from app.constants import BASIC_MODEL_API_KEY, ZEPHYR_LM_ID

# Replace the empty string with your model id below
model_id = ZEPHYR_LM_ID
baseten_api_key = BASIC_MODEL_API_KEY

def zephyr_lm(content: str, role: Optional[str] = "student", max_new_tokens: Optional[int] = 128, temperature: Optional[int] = 0.9) -> Any: 
    messages = [
        {"role": role, "content": content}
    ]

    data = {
        "messages": messages,
        "stream": False,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature
    }

    # Call model endpoint
    res = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json=data
    )

    # Print the output of the model
    print(res.json())