#  http://127.0.0.1:8000/docs  # 文档

from fastapi import FastAPI
import uvicorn

app = FastAPI()

# -----------------------------------------
# 结合LLM
import os
from transformers import AutoTokenizer, AutoModel
MODEL_PATH = os.environ.get('MODEL_PATH', '/remote-home/share/LLM_model/chatglm3-6b')
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)

from pydantic import BaseModel
class Request(BaseModel):
    prompt: str


@app.get("/hello") 
async def hello():
    global model, tokenizer # 使用全局变量
    response, history = model.chat(tokenizer, "你好", history=[])
    return response

@app.post("/chat") 
async def chat(data: Request):
    global model, tokenizer # 使用全局变量
    response, history = model.chat(tokenizer, data.prompt, history=[])
    return response


if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()

    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)