from pathlib import Path		
import sys
cur3_path = Path(__file__).parent.parent.parent    # 目录    DocDoc2
cur2_path = Path(__file__).parent.parent    # 目录    DocDoc2/test
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/test/llamaIndex
sys.path.append(str(cur_path))
sys.path.append(str(cur2_path))
sys.path.append(str(cur3_path))

from llama_index.core.llama_pack import download_llama_pack

# # download and install dependencies
# SentenceWindowRetrieverPack = download_llama_pack(
#     "SentenceWindowRetrieverPack", "./sentence_window_retriever_pack"
# )


# 加载你的数据
from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader(input_files=["./岳飞语料.pdf"]).load_data()

# create the pack
# get documents from any data loader
sentence_window_retriever_pack = SentenceWindowRetrieverPack(
    documents
)

# response = sentence_window_retriever_pack.run(
#     "岳飞的作品有哪些？"
# )

# # get the sentence vector index
# index = sentence_window_retriever_pack.sentence_index

# # get the node parser
# node_parser = sentence_window_retriever_pack.node_parser

# # get the metadata replacement postprocessor
# postprocessor = sentence_window_retriever_pack.postprocessor

# # get the query engine
# query_engine = sentence_window_retriever_pack.query_engine