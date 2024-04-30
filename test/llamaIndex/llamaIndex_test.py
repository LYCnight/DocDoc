from llama_index.core.llama_pack import download_llama_pack

# download and install dependencies
SentenceWindowRetrieverPack = download_llama_pack(
    "SentenceWindowRetrieverPack", "./sentence_window_retriever_pack"
)

# create the pack
# get documents from any data loader
sentence_window_retriever_pack = SentenceWindowRetrieverPack(
    documents,
)

response = sentence_window_retriever_pack.run(
    "Tell me a bout a Music celebritiy."
)

# get the sentence vector index
index = sentence_window_retriever_pack.sentence_index

# get the node parser
node_parser = sentence_window_retriever_pack.node_parser

# get the metadata replacement postprocessor
postprocessor = sentence_window_retriever_pack.postprocessor

# get the query engine
query_engine = sentence_window_retriever_pack.query_engine