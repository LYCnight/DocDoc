from pathlib import Path		
import sys
root_path = "/root/AI4E/lzd/DocDoc"
cur_path = "/root/AI4E/lzd/DocDoc/core"    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))
print(sys.path)

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
    SimpleDirectoryReader
)

# load index from disk
from llama_index.vector_stores.faiss import FaissVectorStore
vector_store = FaissVectorStore.from_persist_dir("/root/AI4E/lzd/DocDoc/core/storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="/root/AI4E/lzd/DocDoc/core/storage"
)
index = load_index_from_storage(storage_context=storage_context)

# load documents
path_to_directory = str(root_path) + "/UserUploadFiles"
reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
documents = reader.load_data()

# append new doc
for doc in documents:
    index.insert(doc)

# save index to disk
index.set_index_id("vector_index")      # 这样可以续写 index，而不是重写index
index.storage_context.persist(str(cur_path) + "/storage")
print("here")





