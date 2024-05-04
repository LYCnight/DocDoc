from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

from typing import List
from base import Vectordb

class Faiss(Vectordb):

    def __init__(self):
        self.vectordb = ""
        
    def store(self, documents, embeddings):
        '''
        功能：
            - 基于Fasis数据库的知识存储功能
        参数：
            - document : 要存储的知识   'documents' should be -> Lanchain Document | List[Document] 
            - embeddings ： embeddings模型
        '''
        self.vectordb = FAISS.from_documents(documents, embeddings)

    def similarity_search(self, query:str) -> List[Document]: 
        '''
        功能：
            - 基于Fasis数据库的知识检索（不使用 retriever）
        '''
        docs = self.vectordb.similarity_search(query)
        return docs


class Chroma(Vectordb):
    def store(self):
        print("I am Chroma")

class Lance(Vectordb):
    def store(self):
        print("I am lance")

if __name__ == "__main__":

    # --unitest--
    from langchain_community.document_loaders import TextLoader
    from langchain_openai import OpenAIEmbeddings
    from langchain.text_splitter import CharacterTextSplitter

    # jupyter notebook 中翻墙
    import os
    os.environ['http_proxy'] = '127.0.0.1:7890'
    os.environ['https_proxy'] = '127.0.0.1:7890'

    # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
    os.environ["OPENAI_API_KEY"] = "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"

    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    raw_documents = TextLoader(str(root_path) + '/test/files/state_of_the_union.txt').load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)

    vectordb = Faiss()
    vectordb.store(documents, OpenAIEmbeddings())
    docs = vectordb.similarity_search("What did the president say about Ketanji Brown Jackson")
    print(docs)



    from langchain_community.document_loaders import TextLoader
    from langchain_openai import OpenAIEmbeddings
    from langchain.text_splitter import CharacterTextSplitter
    from langchain_community.vectorstores import FAISS

    EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"
    from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    import numpy as np
    embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                        model_kwargs = {'device': "cuda"})

    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    raw_documents = TextLoader(str(root_path) + '/test/files/state_of_the_union.txt').load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)

    vectordb = Faiss()
    vectordb.store(documents, embeddings)
    docs = vectordb.similarity_search("What did the president say about Ketanji Brown Jackson")
    print(docs)