from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

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


from llama_index.core import (
    load_index_from_storage,
    StorageContext,
)

# load index from disk
from llama_index.vector_stores.faiss import FaissVectorStore
vector_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="./storage"
)
index = load_index_from_storage(storage_context=storage_context)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.retrieve("这份环境报告的研究区域是哪里？")
print(response[0].get_text())
print(len(response))
