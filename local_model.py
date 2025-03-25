from transformers import pipeline

nlp = pipeline("sentiment-analysis")
print(nlp("I love AI!"))