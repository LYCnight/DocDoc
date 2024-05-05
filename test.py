import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
from config import MODEL_PATH,TOKENIZER_PATH, LLM_DEVICE
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH,
    revision="v2.0",
    use_fast=False,
    trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH,
    revision="v2.0",
    device_map=LLM_DEVICE,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained(MODEL_PATH, revision="v2.0")
messages = []
messages.append({"role": "user", "content": "解释一下“温故而知新”"})
response = model.chat(tokenizer, messages)
print(response)
