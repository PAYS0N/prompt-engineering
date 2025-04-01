from huggingface_hub import InferenceClient
import os

hf_token = os.getenv("hf_prompt_engineering")

client = InferenceClient(
    "Qwen/Qwen2.5-0.5B-Instruct",
    token=hf_token,
)

context = f"""
Your job is to help create interesting fantasy worlds that \
players would love to play in.
Instructions:
- Only generate in plain text without formatting.
- Use simple clear language without being flowery.
- You must stay below 3-5 sentences for each description.
Generate a creative description for a unique fantasy world with an
interesting concept around cities build on the backs of massive beasts.

Output content in the form:
World Name: <WORLD NAME>
World Description: <WORLD DESCRIPTION>

World Name:"""
print(client.text_generation(prompt=context, max_new_tokens=200))
