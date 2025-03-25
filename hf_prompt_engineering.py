import requests
import os

hf_token = os.getenv("hf_prompt_engineering")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {hf_token}"}
payload = {
    "inputs": "Today is a great day",
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json())