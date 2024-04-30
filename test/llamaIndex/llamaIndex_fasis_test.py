import faiss

# dimensions of text-ada-embedding-002
d = 1536
faiss_index = faiss.IndexFlatL2(d)

from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore

# load documents
reader = SimpleDirectoryReader( input_files=["testPDF.pdf"] )
documents = reader.load_data()
print(f"Loaded {len(documents)} docs")

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

# # # save index to disk
# # index.storage_context.persist()

# # set Logging to DEBUG for more detailed outputs
# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")

# print(response)
