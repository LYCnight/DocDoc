from config import MODEL_PATH, TOKENIZER_PATH
print(MODEL_PATH)
print(TOKENIZER_PATH)

from LLMs import ChatGLM
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

from llama_index.core import SimpleDirectoryReader
from core.RAG import SentenceWindowRetrieverPack  
path_to_directory = "./UserUploadFiles" 
reader = SimpleDirectoryReader(input_dir = path_to_directory, recursive = True) 
documents = reader.load_data()

text = ""
for doc in documents:
    text += doc.get_text()

# text = "你好"

response = llm(text)
print(response)