from fastapi import FastAPI
import uvicorn 

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Enable CORS (允许前端后端可以跨域请求)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://127.0.0.1:8080"],  # 允许的前端地址
    allow_origins=["*"],  # 允许所有来源的访问（仅在开发时使用）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LLM config
import os
from transformers import AutoTokenizer, AutoModel
MODEL_PATH = os.environ.get('MODEL_PATH', '/remote-home/share/LLM_model/chatglm3-6b')
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)


@app.get("/") 
async def hello():
    response = "你好，我是后端的入口"
    return response


@app.get("/hello") 
async def hello():
    response = "你好，我是AI，运行在后端"
    return response

@app.get("/AIHi") 
async def AIHi():
    global model, tokenizer # 使用全局变量
    response, history = model.chat(tokenizer, "你好", history=[])
    return response

@app.post("/AIChat") 
async def AIChat():
    response = "你好，我是AI，运行在后端"
    return response

@app.get("/AIGen")
async def AIGen():
    response = "你好，我是AI，运行在后端"
    return response

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()

    uvicorn.run(app, host='127.0.0.1', port=8001, workers=1)