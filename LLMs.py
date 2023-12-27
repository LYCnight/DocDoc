from transformers import AutoTokenizer, AutoModel

class ChatGLM():
    tokenizer: object = None
    model: object = None

    def __init__(self):
        pass

    def __call__(self, prompt: str) -> str:  # 模型响应
        response, history = self.model.chat(   # 生成回答
            self.tokenizer,
            prompt,
        )
        return response

    def load_model(self, 
                MODEL_PATH: str = "THUDM/chatglm-6b", TOKENIZER_PATH: str = "THUDM/chatglm-6b"):
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()