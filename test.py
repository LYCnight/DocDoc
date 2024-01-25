from utils import ToLangchainObject
contentlist = ["你好", "我是", "清华"]
Documentlist = ToLangchainObject(contentlist)
print(Documentlist)

EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import numpy as np
embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                    model_kwargs = {'device': "cuda"})

vs_path = "demo-vs"  # vector_db 存储地址
from langchain.vectorstores import FAISS # FASIS
# docs = embeddings.embed_documents(texts1) # -> list[向量]
vector_store = FAISS.from_documents(Documentlist, embeddings) # 建立 向量数据库
vector_store.save_local(vs_path)  # 存储到vsdb中
