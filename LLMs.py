from transformers import AutoTokenizer, AutoModel
import torch
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH

class ChatGLM():
    def __init__(self):
        self.tokenizer: object = None
        self.model: object = None

    def __call__(self, prompt: str) -> str:  # 模型响应
        '''
        功能：传入prompt，返回AI的回答
        示例：
            llm = ChatGLM()
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
            response = CHatGLM("你好")
            print(response)
        '''
        response, history = self.model.chat(   # 生成回答
            self.tokenizer,
            prompt,
        )
        return response

    def load_model(self, 
                MODEL_PATH: str = "THUDM/chatglm3-6b-128k", 
                TOKENIZER_PATH: str = "THUDM/chatglm3-6b-128k"):
        '''
        功能：加载模型
        示例：
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
        '''
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
        # self.model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()  # 多卡推理
        self.model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).eval()
        device = torch.device("cuda:0")  # 使用0号GPU
        self.model.to(device)   # 指定模型运行的显卡

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