from config import import_selecter
from utils import ToLangchainDocument
from langchain.docstore.document import Document
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH 
from typing import List

from pathlib import Path		
import sys
root_path = Path(__file__).parent    # 项目根目录    DocDoc2/

loader, spliter, retriever, vectordb = import_selecter("spacy", "simple", "faiss")

from LLMs import ChatGLM
llm= ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                    model_kwargs = {'device': "cuda"})   # 未来在这里进行拓展，支持更多 embeddings


filelist = ['汨罗江洪道治理报告书（2021）.docx', "长江湖南段三期河道整治工程环境影响报告书（2022）.docx"]
# filelist = ['testdocx1.docx', 'testdocx2.docx']
filelist = [(str(root_path)+"/test/files/"+file) for file in filelist]
print(filelist)

# loader
content: str = loader.load(filelist)

# spliter
content_split: List[str] = spliter.split(content)  # -> List[str]

# convert to langchain data format 
document_split: List[Document] = ToLangchainDocument(content_split)  # -> List[Document]

# vectordb
vector_store = vectordb.store(document_split, embeddings)

# retriever
vector_query = "地下水"
# content = retriever.query_search(vector_query)
knowledge = vectordb.similarity_search(vector_query)
print(knowledge)


# generate
query = "帮我撰写的“结论”章节。结构要求：1. 项目概况 2. 区域环境质量现状评价结论 3. 环境影响分析结论 4. 环境可行性分析结论  5. 公众参与结论  6. 综合结论"
prompt = f"""上下文：{knowledge} 
--------
请根据上下文结合你的知识，{query}"""

response:str = llm(prompt) 

print(response)

# ouput
from core.outputer import PdfOutputer
pdfOutputer = PdfOutputer()
pdfOutputer.output(response, '环评报告结论.pdf')



    
