from transformers import AutoTokenizer, AutoModel
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH
import torch
device = torch.device("cuda:0") 

class ChatGLM():
    def __init__(self):
        self.tokenizer: object = None
        self.model: object = None

    def __call__(self, prompt: str) -> str:  # 模型响应

        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = self.tokenizer([text], return_tensors="pt").to(device)
        generated_ids = self.model.generate(model_inputs.input_ids, max_new_tokens=512)
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

    def load_model(self, 
                MODEL_PATH: str = "/root/AI4E/share/Qwen1.5-14B-Chat", 
                TOKENIZER_PATH: str = "/root/AI4E/share/Qwen1.5-14B-Chat"):
        '''
        功能：加载模型
        示例：
            llm.load_model(MODEL_PATH, TOKENIZER_PATH)
        '''
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map=device)
        self.tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

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