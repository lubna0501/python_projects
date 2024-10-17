import torch
from transformers import pipeline
import time


t = time.time()
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

print("TIme taken to load the modeel : ", time.time()-t)
t = time.time()
# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds with few very creative captions for image description provided by the user.",
    },
    {"role": "user", "content": "A beautiful girl with long hair"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

print("Time taken for inference 1 : ", time.time() - t)
t = time.time()
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds with few very creative captions for image description provided by the user.",
    },
    {"role": "user", "content": "A beautiful girl with pink shirt"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

print("Time taken for inference 2 : ", time.time() - t)
t = time.time()