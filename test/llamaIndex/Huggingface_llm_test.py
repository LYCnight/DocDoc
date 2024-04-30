from llama_index.llms.huggingface import HuggingFaceLLM

def messages_to_prompt(messages):
    prompt = ""
    for message in messages:
        if message.role == 'system':
            prompt += f"<|system|>\n{message.content}</s>\n"
        elif message.role == 'user':
            prompt += f"<|user|>\n{message.content}</s>\n"
        elif message.role == 'assistant':
            prompt += f"<|assistant|>\n{message.content}</s>\n"

    # ensure we start with a system prompt, insert blank if needed
    if not prompt.startswith("<|system|>\n"):
        prompt = "<|system|>\n</s>\n" + prompt

    # add final assistant prompt
    prompt = prompt + "<|assistant|>\n"

    return prompt

def completion_to_prompt(completion):
    return f"<|system|>\n</s>\n<|user|>\n{completion}</s>\n<|assistant|>\n"

import torch
from transformers import BitsAndBytesConfig
from llama_index.core.prompts import PromptTemplate
from llama_index.llms.huggingface import HuggingFaceLLM

from transformers import AutoTokenizer, AutoModel
# model_name="/root/AI4E/share/Baichuan2-7B-Chat"
# tokenizer_name="/root/AI4E/share/Baichuan2-7B-Chat"
model_name="/root/AI4E/share/chatglm3-6b-128k"
tokenizer_name="/root/AI4E/share/chatglm3-6b-128k"
model = AutoModel.from_pretrained(model_name, trust_remote_code=True).eval()
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)

llm = HuggingFaceLLM(
    model=model,
    tokenizer = tokenizer,
    context_window=3900,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "top_k": 50, "do_sample": True, "top_p": 0.95},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    device_map="auto",
)

response = llm.complete("What is the meaning of life?")
print(str(response))