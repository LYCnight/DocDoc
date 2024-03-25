from pathlib import Path
import sys
root_path = Path(__file__).parent.parent  # /DocDoc 项目根目录
sys.path.append(str(root_path))

from fastapi import FastAPI
import uvicorn
from LLMs import ChatGLM
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH 

from AI.AIdoc import AIgen_chapter, AIgen_doc, AIContinue, AIImprove
from util import text2html


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

# PostRequest for AIimprove, AIcontinue
class Request(BaseModel):
    text: str 

# PostRequest for AIGendoc
class PostData(BaseModel):
    title: str
    information: str

@app.get("/") 
async def hello():
    response = "你好，我是后端的入口"
    return response

@app.get("/hello") 
async def hello():
    response = "你好，我是AI，运行在后端"
    return response

# 用于测试
@app.get("/AIHi") 
async def AIHi():
    # test
    from testTemplate import testMarkdown
    response:str = text2html(testMarkdown)
    print(response)

    return response

# 待开发功能
@app.post("/AIChat") 
async def AIChat():
    '''
    - 功能：AI对话
    '''
    pass

@app.post("/AIGendoc")
async def AIGen_doc(post_data: PostData):
    title = post_data.title
    information = post_data.information
    '''
    - 功能
        接受`标题`和`信息`，生成报告，并转换成html包装成JSON返回
    '''
    if title is None or title == "":
        title = "张靖皋长江大桥ZJG-A5标段绿色工地建设阶段性工作总结"    # 缺省值
        information = "张靖皋长江大桥ZJG-A5标段，于2021年12月1日开始施工，2023年3月2日竣工" # 缺省值

    # 生成文本，返回 str
    response:str = AIgen_doc(title, llm, information)
    print(response)
    response_html = text2html(response)
    print(response_html)

    return response_html

@app.get("/AIGendoc")
async def AIGen_doc(title:str=None, information:str=None):
    '''
    - 功能
        接受`标题`和`信息`，生成报告，并转换成html包装成JSON返回
    '''
    if title is None or title == "":
        title = "张靖皋长江大桥ZJG-A5标段绿色工地建设阶段性工作总结"    # 缺省值
        information = "张靖皋长江大桥ZJG-A5标段，于2021年12月1日开始施工，2023年3月2日竣工" # 缺省值

    # 生成文本，返回 str
    response:str = AIgen_doc(title, llm, information)
    print(response)
    response_html = text2html(response)
    print(response_html)

    return response_html

# 下个版本的方法：
# 问题：API方法可以重载吗？
# @app.post("/AIGendoc")
# async def AIGen_doc(request: Request):
#     title:str = request.text
#     if title is None or title == "":
#         title = "张靖皋长江大桥ZJG-A5标段绿色工地建设阶段性工作总结"   # 默认值
#     response:str = AIgen_doc(title, llm)
#     return response


@app.post("/AIContinue")
async def AI_Continue(request: Request) -> str: 
    '''
    - 功能：AI续写
    '''
    # 生成文本，返回 str
    text = request.text  # -> str
    response = AIContinue(text, llm)
    return response

@app.post("/AIImprove")
async def AI_Improve(request: Request) -> str: 
    '''
    - 功能：AI优化
    '''
    # 生成文本，返回 str
    text = request.text  # -> str
    response = AIImprove(text, llm)
    return response

if __name__ == "__main__":

    llm = ChatGLM()
    llm.load_model(MODEL_PATH = MODEL_PATH, TOKENIZER_PATH = TOKENIZER_PATH)

    # 这一行运行不了，原因不明
    # embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH, model_kwargs = {'device': "cuda"})  


    print("模型加载完成！正在启动后端服务 ---> ")
    print("API文档：http://localhost:8000/docs")

    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)


''' 测试方法

API 文档：http://localhost:8000/docs

/AIHi
curl -X 'GET' \
  'http://localhost:8000/AIHi' \
  -H 'accept: application/json'

/AIGen
curl -X 'GET' \
  'http://localhost:8000/AIGen' \
  -H 'accept: application/json'

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
