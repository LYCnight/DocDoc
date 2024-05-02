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