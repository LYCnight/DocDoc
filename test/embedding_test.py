from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import numpy as np

# 0.config
ProjectPath = "/remote-home/yy/lzd/DocDoc" 
MODEL_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
TOKENIZER_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"


embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                    model_kwargs = {'device': "cuda"})

text = "北京大学"
query_result = embeddings.embed_query(text)

print(query_result)
print("结束")