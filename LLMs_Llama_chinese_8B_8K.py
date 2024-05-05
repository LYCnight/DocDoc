from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH, LLM_DEVICE, EMBED_DEVICE
device = LLM_DEVICE
embed_device = EMBED_DEVICE
# import torch
# device = torch.device("cuda:7") 

class ChatGLM():
    def __init__(self):
        self.tokenizer: object = None
        self.model: object = None

    def __call__(self, prompt: str) -> str:  # 模型响应
        messages = [
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ]
        input_ids = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)        
        outputs = self.model.generate(
            input_ids,
            max_new_tokens=8192,    # 8K
            do_sample=True,
            temperature=0.2,
            top_p=0.95,
        )
        response = outputs[0][input_ids.shape[-1]:]     
        response = self.tokenizer.decode(response, skip_special_tokens=True)
        return response

    def load_model(self, 
                MODEL_PATH: str = MODEL_PATH, 
                TOKENIZER_PATH: str = TOKENIZER_PATH):
        '''
        功能：加载模型
        示例：
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
        '''
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map=LLM_DEVICE)

def init_llm_and_embedding(MODEL_PATH=MODEL_PATH, TOKENIZER_PATH=TOKENIZER_PATH, EMBEDDING_PATH=EMBEDDING_PATH):
    llm = ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    print(llm("你好"))
    
    # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    # embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
    #                                 model_kwargs = {'device': "cuda"})   # 未来在这里进行拓展，支持更多 embeddings
    # print(f"embedding model: {EMBEDDING_PATH} loaded successfully!")
    return llm, embedding

if __name__ == "__main__":
    # LLM 测试
    from config import MODEL_PATH, TOKENIZER_PATH
    print(MODEL_PATH)
    print(TOKENIZER_PATH)
    llm = ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    print(llm("望春风"))

    # embbeding 测试
    # from config import EMBEDDING_PATH
    # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    # embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
    #                                 model_kwargs = {'device': "cuda"})   # 未来在这里进行拓展，支持更多 embeddings
    # print(f"embedding model: {EMBEDDING_PATH} loaded successfully!")