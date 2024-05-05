from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
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
        messages = []
        messages.append({"role": "user", "content": prompt})
        response = self.model.chat(self.tokenizer, messages)
        return response

    def load_model(self, 
                MODEL_PATH: str = MODEL_PATH, 
                TOKENIZER_PATH: str = TOKENIZER_PATH):
        '''
        功能：加载模型
        示例：
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
        '''
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH,
            revision="v2.0",
            trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH,
            revision="v2.0",
            device_map=LLM_DEVICE,
            trust_remote_code=True)
        self.model.generation_config = GenerationConfig.from_pretrained(MODEL_PATH, revision="v2.0")

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