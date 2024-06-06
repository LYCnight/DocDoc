from transformers import AutoTokenizer, AutoModel
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH, LLM_DEVICE, EMBED_DEVICE
device = LLM_DEVICE
embed_device = EMBED_DEVICE
# import torch
# device = torch.device("cuda:7") 

class ChatGLM():
    def __init__(self):
        import os
        os.environ["OPENAI_API_KEY"] = "sk-zojBY7XNiHrUW96X957dCc90889c47219a328173F20eA50d" #输入网站发给你的转发key
        os.environ["OPENAI_BASE_URL"] = "https://gtapi.xiaoerchaoren.com:8932/v1"
        self.tokenizer: object = None
        self.model: object = None

    def __call__(self, prompt: str) -> str:  # 模型响应
        # Key01：sk-o1DRfeJuLNNisw2VCeAbEfDf2b0c42Eb890eAd5fC0C3D92c
        # Key02: sk-WgLd2UkCvs5i95cRB8C67f7d773c4b1bBdEd9c4a2195B93f
        # key03: sk-FF1K83E40qOybOvBAeC6BfFf7262424e89Ca977337E0105d
        # Key04: sk-3mvPeWqNOhGpfgsUF2265bDe62Dd4028821a37575b3eBa15
        # key05: sk-QJUI3EgaSm07iRnv9b93B31a71C24c78972f96527a96824c      
        import os
        os.environ["OPENAI_API_KEY"] = "sk-o1DRfeJuLNNisw2VCeAbEfDf2b0c42Eb890eAd5fC0C3D92c" #输入网站发给你的转发key
        os.environ["OPENAI_BASE_URL"] = "https://api.gptapi.us/v1/chat/completions"
        from openai import OpenAI
        client = OpenAI()
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
            # {"role": "user", "content": prompt}
            # {"role": "user", "content": fake_history}
        ]
        )
        response = completion.choices[0].message.content
        return response
        
    def load_model(self, 
                MODEL_PATH: str = MODEL_PATH, 
                TOKENIZER_PATH: str = TOKENIZER_PATH):
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