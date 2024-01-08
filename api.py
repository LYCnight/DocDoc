#  http://127.0.0.1:8000/docs  # 文档

from fastapi import FastAPI
from util import DocGenerate 
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
    knowledge: str
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

@app.post("/WriteContent")  # 生成目录
async def WriteConetnt(data: Request):
    global model, tokenizer
    prompt = "现有信息：/n" + data.knowledge + "/n/n" + "--------------------/n"  + "请根据现有信息和你的知识，帮我生成一下这份报告的目录"
    response, history = model.chat(tokenizer, data.prompt, history=[])
    return response

@app.post("/WriteAll")  # 生成全文
async def WriteAll(data: Request):
    global model, tokenizer
    prompt = "现有目录：/n" + data.knowledge + "/n/n" + "--------------------/n" + "请根据现有目录，生成这份报告的全文"
    ## 生成文章的方法
    response = DocGenerate(model, prompt)  # -> response: txt
    return response

@app.post("/Continue") # 续写文本
async def Continue(data: Request):
    global model, tokenizer
    prompt = "上下文：/n" + data.knowledge + "/n/n" + "--------------------/n" + "请根据上下文，续写一些内容"
    response, history = model.chat(tokenizer, data.prompt, history=[])
    return response

@app.post("/Continue") # 优化文本
async def Continue(data: Request):
    global model, tokenizer
    prompt = "上下文：/n" + data.knowledge + "/n/n" + "--------------------/n" + "请优化这段上下文的内容"
    response, history = model.chat(tokenizer, data.prompt, history=[])
    return response

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()

    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)