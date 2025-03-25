from huggingface_hub import InferenceClient

client = InferenceClient(
    "google/gemma-3-4b-it",
    token=""
)

print(client.summarization("Today is a great day, I like the sun on my face. I wish there was a pool nearby. the mosquitos are starting to reall bother me. maybe I should look for som kind of bug spray. tommowrow might be rough i have a lot of work to do."))
