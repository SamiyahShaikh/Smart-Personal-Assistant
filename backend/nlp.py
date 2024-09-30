from transformers import pipeline

nlp = pipeline('text-generation', model='gpt2')

def process_nlp(command):
    response = nlp(command, max_length=50, num_return_sequences=1)[0]['generated_text']
    return response
