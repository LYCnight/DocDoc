from llama_index.embeddings.huggingface import HuggingFaceEmbedding
embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh")

# embeddings = embed_model.get_text_embedding("Hello World!")
# print(len(embeddings))
# print(embeddings[:5])
