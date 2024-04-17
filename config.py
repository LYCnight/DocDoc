# LOADER = ('txt', 'word', 'pdf')
# SPLITER = ('NLTK', 'spacy', 'CharacterText', "tiktoken")
# RETRIEVER = ("simple", "multivector", "parentdoc")
# VECTORDB = ("faiss", "chroma", "lance")

# print("hi, I am config.py")

# 对一个内容的最大审核次数
MAX_REVIEW_TURNS = 0  

# --------算法组模型接口---------
ProjectPath = "/root/AI4E/lzd/DocDoc" 
# MODEL_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
# MODEL_PATH = "/remote-home/yy/lzd/ljc/ChatGLM3/finetune_demo/pku-6B"
MODEL_PATH = "/root/AI4E/share/chatglm3-6b-128k" 
TOKENIZER_PATH = "/root/AI4E/share/chatglm3-6b-128k"
EMBEDDING_PATH = "/root/AI4E/share/bge-large-zh"
# --------算法组模型接口---------

from pathlib import Path		
import sys
root_path = Path(__file__).parent    # 项目根目录

from typing import Tuple
from core.base import Loader, Spliter, Retriever, Vectordb


def import_selecter(spliter_config:str = "NLTK",
                    retriever_config:str = "multivector",
                    vectordb_config:str = "faiss"
                    ) -> Tuple[Loader, Spliter, Retriever, Vectordb]:
    from core.loader import Loader_adapter
    loader = Loader_adapter()
    print("loader loaded")

    match spliter_config:
        case 'NLTK':
            from core.spliter import NLTK_spliter
            spliter = NLTK_spliter()
            print("NLTK_spliter loadeed")
        case 'spacy':
            from core.spliter import spacy_spliter
            spliter = spacy_spliter()
            print("spacy_spliter loadeed")
        case 'CharacterText':
            from core.spliter import CharacterText_spliter
            spliter = CharacterText_spliter() 
            print("CharacterText_spliter loadeed")
        case 'tiktoken':
            from core.spliter import tiktoken_spliter
            spliter = tiktoken_spliter()
            print("tiktoken_spliter loadeed")
        case _: # 未匹配上的默认情况
            spliter = None
            print("No spliter loaded")

    match retriever_config:
        case 'simple':
            from core.retriever import Simple_retriever
            retriever = Simple_retriever()
            print("simple_retriever loadeed")
        case 'multivector':
            from core.retriever import Multivector_retriever
            retriever = Multivector_retriever()
            print("multivector_retriever loadeed")
        case 'parentdoc':
            from core.retriever import ParentDoc_retriever
            retriever = ParentDoc_retriever() 
            print("CharacterText_spliter loadeed")
        case _: # 未匹配上的默认情况
            print("No retriever loaded")

    match vectordb_config:
        case 'faiss':
            from core.vectordb import Faiss
            vectordb = Faiss()
            print("faiss vectordb loadeed")
        case 'chroma':
            from core.vectordb import Chroma
            vectordb = Chroma()
            print("chroma vectordb loadeed")
        case 'lance':
            from core.vectordb import Lance
            vectordb = Lance()
            print("lance vectordb loadeed")
        case _: # 未匹配上的默认情况
            print("No vectordb loaded")

    return loader, spliter, retriever, vectordb

if __name__ == "__main__":
    # test
    loader, spliter, retriever, vectordb = import_selecter("spacy", "simple", "faiss")
    loader.load("")
    spliter.split()
    retriever.query_search()

    print("*"*60)
    print(loader.load(""))
    print("*"*60)
    print(loader.load("file.docx"))


    # ---------------- vectordb test --------------------
    # from langchain_community.document_loaders import TextLoader
    # from langchain_openai import OpenAIEmbeddings
    # from langchain.text_splitter import CharacterTextSplitter

    # # jupyter notebook 中翻墙
    import os
    os.environ['http_proxy'] = '127.0.0.1:7890'
    os.environ['https_proxy'] = '127.0.0.1:7890'

    # os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')
    os.environ["OPENAI_API_KEY"] = "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"

    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    raw_documents = TextLoader(str(root_path) + '/test/files/state_of_the_union.txt').load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(raw_documents)

    vectordb.store(documents, OpenAIEmbeddings())
    docs = vectordb.similarity_search("What did the president say about Ketanji Brown Jackson")
    print(docs)
    print()
    print("*" * 100)
    print(vectordb.similarity_search("hello"))