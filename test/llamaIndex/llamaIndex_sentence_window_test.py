from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader( input_files=["./test/testPDF.pdf"] )
documents = reader.load_data()
print(f"Loaded {len(documents)} docs")

# from llama_index.core.llama_pack import download_llama_pack

# # download and install dependencies
# SentenceWindowRetrieverPack = download_llama_pack(
#     "SentenceWindowRetrieverPack", "./sentence_window_retriever_pack"
# )

# from llama_index.node_parser import SimpleNodeParser
# nodes = SimpleNodeParser.from_defaults().get_nodes_from_documents(documents)

# print(len(nodes))

# from llama_index.llama_pack import download_llama_pack
# import os
# os.environ['OPENAI_API_KEY'] = ""


# llama_pack = download_llama_pack(
#     "SentenceWindowRetrieverPack", "./sentence_window_retriever_pack"
# )

# # Pass documents to build the pack instance
# sentence_window_retriever_pack = llama_pack(documents)

# QUESTION = "What is the goal of validity rollup?"

# response = sentence_window_retriever_pack.run(QUESTION)

# print(response.response)