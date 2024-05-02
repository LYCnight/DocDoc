# from transformers import AutoTokenizer 
# tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large') 

def tokenCount(text:str):
    """输入字符串，返回token长度"""
    from transformers import AutoTokenizer
    from config import  TOKENIZER_PATH
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    # text = "中国人" 
    tokens = tokenizer.encode(text, add_special_tokens=False) 
    # print(len(tokens))
    return len(tokens)

if __name__ == "__main__":
    from llama_index.core import SimpleDirectoryReader
    from core.RAG import SentenceWindowRetrieverPack  
    path_to_directory = "./UserUploadFiles" 
    reader = SimpleDirectoryReader(input_dir = path_to_directory, recursive = True) 
    documents = reader.load_data()
    
    text = ""
    for doc in documents:
        text += doc.get_text()
    
    token_len = tokenCount(text)
    print(len(text))
    print(token_len)
    
    from config import MODEL_PATH, TOKENIZER_PATH
    from LLMs import ChatGLM
    llm = ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    
    response = llm(text)
    print(response)    