from typing import List
from langchain.docstore.document import Document
from pathlib import Path		
import sys
root_path = Path(__file__).parent    # 项目根目录    DocDoc2/

def ToLangchainDocument(content_split:List[str]) -> List[Document]:
    '''
    功能：
        - convert List[str] -> List[Document]，用以适配 langchain 的方法
        - Document 是 Langchain 里的文档对象，可以被Langchain操作
        - str 是 python 内置的字符串对象，不可以被Langchain操作
    示例:
        str_list = ["hello", "word"]
        document_list = ToLangchainDocument(str_list)
    '''
    Documentlist = [Document(page_content=text, metadata={"from": "book.txt"}) for text in content_split]
    return Documentlist

# 从 Excel 文件读取数据
def read_content(file_path, min_level, max_level):
    import pandas as pd
    df = pd.read_excel(file_path)
    content = []

    class Heading:
        def __init__(self, id, heading, dep, level):
            self.id = id
            self.heading = heading
            self.dep = dep
            self.level = level
            self.text = None
            self.dep_text = []

    # 根据 Excel 中的数据构造 Heading 对象的列表
    for index, row in df.iterrows():
        if min_level <= row['level'] <= max_level:
            heading_obj = Heading(row['id'], row['heading'], [row['dep']], row['level'])
            content.append(heading_obj)
    return content

def print_content(content):
    # 打印构造的 content 列表
    for heading_obj in content:
        print(f"ID: {heading_obj.id}, Heading: {heading_obj.heading}, Dep: {heading_obj.dep}, Level: {heading_obj.level}")
    print(f"本次共返回{len(content)}个heading")

# 获取 Excel 文件中 heading 的数量、最小 level 和最大 level
def get_stats(file_path):
    import pandas as pd
    df = pd.read_excel(file_path)
    num_headings = len(df)
    min_level = df['level'].min()
    max_level = df['level'].max()
    return num_headings, min_level, max_level

if __name__ == "__main__":
    # 测试 content_reader
    # 测试读取 level 范围在 1 到 2 之间的内容
    file_path = 'test/content.xlsx'
    content = read_content(file_path, 0, 4)
    print_content(content)
    
    
    
    # -- 简单测试 --
    # contentlist = ["你好", "我是", "清华"]
    # Documentlist = ToLangchainObject(contentlist)
    # print(Documentlist)

    # EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"
    # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    # import numpy as np
    # embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
    #                                     model_kwargs = {'device': "cuda"})

    # vs_path = "demo-vs"  # vector_db 存储地址
    # from langchain.vectorstores import FAISS # FASIS
    # # docs = embeddings.embed_documents(texts1) # -> list[向量]
    # vector_store = FAISS.from_documents(Documentlist, embeddings) # 建立 向量数据库
    # vector_store.save_local(vs_path)  # 存储到vsdb中


    # # ------------- test2 -------------
    # from config import import_selecter
    # from utils import ToLangchainDocument
    # loader, spliter, retriever, vectordb = import_selecter("spacy", "simple", "faiss")
    # loader.load("")
    # spliter.info()
    # retriever.query_search()

    # filelist = ['汨罗江洪道治理报告书（2021）.docx', "长江湖南段三期河道整治工程环境影响报告书（2022）.docx"]
    # # filelist = ['testdocx1.docx', 'testdocx2.docx']
    # filelist = [(str(root_path)+"/test/files/"+file) for file in filelist]
    # print(filelist)
    
    # content:str = loader.load(filelist)
    # # print(content)

    # content_split: List[str] = spliter.split(content)
    # # print(content_split)

    # document_split: List[Document] = ToLangchainDocument(content_split)
    # print(document_split)

    

    