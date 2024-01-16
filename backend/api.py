from pathlib import Path
import sys
root_path = Path(__file__).parent.parent  # /DocDoc 项目根目录
sys.path.append(str(root_path))

from fastapi import FastAPI
import uvicorn
from LLMs import ChatGLM
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH 


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

# request body config
from pydantic import BaseModel
class Request(BaseModel):
    text: str 

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
    response = LLM("你好")
    return response

@app.post("/AIChat") 
async def AIChat():
    response = "你好，我是AI，运行在后端"
    return response

@app.get("/AIGen")
async def AIGen():
    # 生成文本，返回 str
    from utils import DocGenerate
    response = DocGenerate(LLM, embeddings)
    return response

@app.post("/AIContinue")
async def AIContinue(request: Request) -> str: 
    # 生成文本，返回 str
    from utils import AIContinue
    contents = request.text  # -> str
    response = AIContinue(LLM, embeddings, contents = contents)
    return response

@app.post("/AIImprove")
async def AIImprove(request: Request) -> str: 
    # 生成文本，返回 str
    from utils import AIImprove
    contents = request.text  # -> str
    response = AIImprove(LLM, embeddings, contents = contents)
    return response

if __name__ == "__main__":

    LLM = ChatGLM()
    LLM.load_model(MODEL_PATH = MODEL_PATH, TOKENIZER_PATH = TOKENIZER_PATH)

    embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                    model_kwargs = {'device': "cuda"})

    uvicorn.run(app, host='127.0.0.1', port=8000, workers=1)

''' 测试方法
/AIGen
curl -X 'GET' \
  'http://localhost:8000/AIGen' \
  -H 'accept: application/json'

/AIContinue
curl -X 'POST' \
  'http://localhost:8000/AIContinue' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{                               
  "text": "但是原神是一款" 
}'

/AIImprove
curl -X 'POST' \
  'http://localhost:8000/AIImprove' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": " 我用了一个月，搭建了 DocDoc 前后端代码架构"
}'
'''
