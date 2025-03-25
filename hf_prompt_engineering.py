import requests

API_URL = "https://api-inference.huggingface.co/models/google/gemma-3-4b-it"

headers = {"Authorization": "Bearer "}

payload = {
    "inputs": "Summarize the following: Today is a great day, I like the sun on my face. I wish there was a pool nearby. the mosquitos are starting to reall bother me. maybe I should look for som kind of bug spray. tommowrow might be rough i have a lot of work to do.",
}

response = requests.post(API_URL, headers=headers, json=payload)

print(response.status_code)
print(response.json())