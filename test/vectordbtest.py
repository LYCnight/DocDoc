# -- unitest for core/vectordb.py--

# -- using openaiembedding --------------
from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
# root_path 为 Poxis类型，可以转为字符串： str(root_path)
core_path = Path(__file__).parent    # 当前目录    
sys.path.append(str(core_path))
sys.path.append(str(root_path))

# from core.vectordb import Faiss

# from langchain_community.document_loaders import TextLoader
# from langchain_openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter

# # jupyter notebook 中翻墙
# import os
# os.environ['http_proxy'] = '127.0.0.1:7890'
# os.environ['https_proxy'] = '127.0.0.1:7890'

# # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
# os.environ["OPENAI_API_KEY"] = "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"

# # Load the document, split it into chunks, embed each chunk and load it into the vector store.
# raw_documents = TextLoader(str(root_path) + '/test/files/state_of_the_union.txt').load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# documents = text_splitter.split_documents(raw_documents)

# vectordb = Faiss()
# vectordb.store(documents, OpenAIEmbeddings())
# docs = vectordb.similarity_search("What did the president say about Ketanji Brown Jackson")
# print(docs)



# -- using loacalembedding --------------
from core.vectordb import Faiss
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

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