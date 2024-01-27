from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

from base import Spliter
from typing import List, NoReturn

class NLTK_spliter(Spliter):
    def info(self) -> NoReturn:
        print("I am NLTK_spliter")

    def split(self) -> List[str]:
        print("I am NLTK_spliter")
 

class spacy_spliter(Spliter):
    def info(self) -> NoReturn:
        print("I am spacy_spliter")

    def split(self, texts:str) -> List[str]:
        '''
        功能：基于spacy技术的文本分割
        '''
        # print("I am spacy_spliter")
        from langchain.text_splitter import SpacyTextSplitter
        self.text_splitter = SpacyTextSplitter(
                separator = "\n\n",
                pipeline = "zh_core_web_sm",  # 加载 spacy 的中文模型
                max_length = 1_000_000,
                chunk_size=1000,    # 最大切割字符：1000个
                chunk_overlap = 200)
        # texts -> str
        # texts_splited -> List[str]
        texts_splited = self.text_splitter.split_text(texts)
        return texts_splited

class CharacterText_spliter(Spliter):
    def split(self) -> str:
        print("I am CharacterText_spliter")

class tiktoken_spliter(Spliter):
    def split(self) -> str:
        print("I am tiktoken_spliter")

if __name__ == "__main__":
    from config import import_selecter
    loader, spliter, retriever, vectordb = import_selecter("spacy", "simple", "faiss")
    loader.load("")
    spliter.info()
    retriever.query_search()

    filename = '汨罗江洪道治理报告书（2021）.docx'
    filepath = str(root_path) + "/test/files/" + filename   
    print(filepath)   # /remote-home/yy/lzd/DocDoc2/test/files/汨罗江洪道治理报告书（2021）.docx
    from loader import Word_loader
    word_loader = Word_loader()
    content :str = word_loader.load(filepath)

    content_split: List[str] = spliter.split(content)
    print(content_split) 
    print(len(content_split))   
