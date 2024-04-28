import os
import base64
import requests
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = "7qk4op2w"
baseten_api_key = "RMKbLOWX.LaS4jGB1VyfGPmqBCp0dhyDygAKmaxwZ"
BASE64_PREAMBLE = "data:image/png;base64,"

# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

data = {
  "prompt": "a map of the world in ancient theme with a compass"
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
output = res.get("data")

# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.png")
os.system("open output_image.png")