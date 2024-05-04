from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

#
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# 本地 embedding
from config import EMBED_DEVICE, LLM_DEVICE
device = LLM_DEVICE
embed_device = EMBED_DEVICE
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh", device=embed_device)

# 全局设置
from llama_index.core import Settings
Settings.embed_model = embed_model
Settings.llm = None

# 
import faiss

# dimensions of bge-large-zh
d = 1024
faiss_index = faiss.IndexFlatL2(d)


from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore

# load documents
path_to_directory = str(root_path) + "/UserUploadFiles"
reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
documents = reader.load_data()

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, show_progress=True
)


# save index to disk
index.storage_context.persist(str(cur_path) + "/storage")
print("here")
# # set Logging to DEBUG for more detailed outputs
# query_engine = index.as_query_engine()
# response = query_engine.retrieve("这份环境报告的研究区域是哪里？")
# print(response)

