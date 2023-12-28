# -------------------------------------------------
# 1. ChineseSpiliter
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.docstore.document import Document
# from typing import Any, List
# class TextSpliter(CharacterTextSplitter):  # 用于文本分块的类（按 '\n' 换行符进行切割）
#     def __init__(self, separator: str = "\n\n", **kwargs: Any):
#         super().__init__(separator, **kwargs)
#     def split_text(self, text: str) -> List[str]:

#         texts = text.split("\n")
#         texts = [Document(page_content=text, metadata={"from": "filename or book.txt"}) for text in texts]
#         return texts    # -> List[Document]
# text_splitter = TextSpliter()
# texts = text_splitter.split_text(texts)     # -> List[Document]
# texts1 = [text.page_content for text in texts]  # -> List[str]
# print(texts1)
# print("step3 completed")


# -------------------------------------------------
# 2. NLTK
# 3.分割文档 spliter
from langchain.text_splitter import NLTKTextSplitter
from langchain.docstore.document import Document

text_splitter = NLTKTextSplitter(chunk_size=1000) # How the chunk size is measured: by number of characters.
texts_splited = text_splitter.split_text(texts)
# texts_splited -> list[str]

# 构造 langchain Document 对象
text_Document_list = [Document(page_content=text, metadata={"from": "filename or book.txt"}) for text in texts_splited]


# -------------------------------------------------
# 3. spacy
# !pip install spacy
# !pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz
# 3.分割文档 spliter
from langchain.text_splitter import SpacyTextSplitter
from langchain.docstore.document import Document

text_splitter = SpacyTextSplitter(chunk_size=1000) # How the chunk size is measured: by number of characters.
texts_splited = text_splitter.split_text(texts)
# texts_splited -> list[str]

# 构造 langchain Document 对象
text_Document_list = [Document(page_content=text, metadata={"from": "filename or book.txt"}) for text in texts_splited]