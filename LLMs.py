from transformers import AutoTokenizer, AutoModel
import torch

class ChatGLM():
    tokenizer: object = None
    model: object = None

    def __init__(self):
        pass

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
                MODEL_PATH: str = "THUDM/chatglm-6b", 
                TOKENIZER_PATH: str = "THUDM/chatglm-6b"):
        '''
        功能：加载模型
        示例：
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
        '''
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()
        device = torch.device("cuda:0")  # 使用0号GPU
        self.model.to(device)   # 指定模型运行的显卡