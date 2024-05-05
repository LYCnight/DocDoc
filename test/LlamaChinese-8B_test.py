from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc2
cur_path = Path(__file__).parent    # 当前目录    /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_PATH, TOKENIZER_PATH, LLM_DEVICE

model_id = MODEL_PATH

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map=LLM_DEVICE)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"},
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=2048,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))