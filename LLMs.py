from transformers import AutoTokenizer, AutoModel
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH, LLM_DEVICE, EMBED_DEVICE
device = LLM_DEVICE
embed_device = EMBED_DEVICE
# import torch
# device = torch.device("cuda:7") 

class ChatGLM():
    def __init__(self):
        # import os
        # os.environ["OPENAI_API_KEY"] = "sk-zojBY7XNiHrUW96X957dCc90889c47219a328173F20eA50d" #输入网站发给你的转发key
        # os.environ["OPENAI_BASE_URL"] = "https://gtapi.xiaoerchaoren.com:8932/v1"
        self.tokenizer: object = None
        self.model: object = None

    def __call__(self, prompt: str) -> str:  # 模型响应
        error_key = "asdasd1"   #
        key01 = "sk-tMSfGKttGeCjHctQAd60DaE6D9E94d19B2C8818cD7De09E4"
        key02 = "sk-WgLd2UkCvs5i95cRB8C67f7d773c4b1bBdEd9c4a2195B93f"
        key03 = "sk-1qp2f5ytCgcvDeT1AfC31fC97282466c8037B5469242BbB7"
        key04 = "sk-QOOUOhcgCxWeH6qdCdF707C913Db40D1A0B7Ab883f30Ad17"
        key05 = "sk-ipaOsAopWa9pgBSq2fF73164A40f4d44Af4182781c3c6414"
        key_sequential = "sk-QzcxAPnhBlwptQHw4aAcB6D21a8446C492C3215c5e8d08F8"
        key_single = "sk-kTp5LPgGIHw09gWS142dB4F73cEa4480Bc1a345a879055B9"
        
        import os
        # -- us -- 
        # os.environ["OPENAI_API_KEY"] = error_key
        # os.environ["OPENAI_API_KEY"] = key01
        # os.environ["OPENAI_API_KEY"] = key02
        os.environ["OPENAI_API_KEY"] = key03
        # os.environ["OPENAI_API_KEY"] = key04
        # os.environ["OPENAI_API_KEY"] =  key05
        # os.environ["OPENAI_API_KEY"] =  key_sequential
        # os.environ["OPENAI_API_KEY"] =  key_single
        
        os.environ["OPENAI_BASE_URL"] = "https://api.gptapi.us/v1/chat/completions"
        # -------
        
        # # -- jc-- 
        # os.environ["OPENAI_API_KEY"] = "sk-zojBY7XNiHrUW96X957dCc90889c47219a328173F20eA50d"
        # os.environ["OPENAI_BASE_URL"] = "https://gtapi.xiaoerchaoren.com:8932/v1"
        # # -------
                
        # -- send request and get response-- 
        # from openai import OpenAI
        # client = OpenAI()
        # completion = client.chat.completions.create(
        # # model="gpt-4o",
        # # model="gpt-4o-2024-05-13",
        # model="gpt-4-turbo-preview",
        # # model="gpt-4-turbo",
        # messages=[
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": prompt}
        #     # {"role": "user", "content": prompt}
        #     # {"role": "user", "content": fake_history}
        # ]
        # )
        completion = self.get_completion_until_success(prompt)
        # -----------------------------------
        
        response = completion.choices[0].message.content
        return response
    
    @staticmethod
    def get_completion_until_success(prompt, delay=5):
        """
        获得请求。如遇到错误，则等待一段时间并重试。
            - delay：等待时间（单位: 秒）
        """
        from openai import OpenAI
        import time
        client = OpenAI()
        while True:
            try:
                # 发送请求并获取响应
                completion = client.chat.completions.create(
                model="gpt-4o",
                # model="gpt-4o-2024-05-13",
                # model="gpt-4-turbo-preview",
                # model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
                )
                return completion
            except Exception as e:  # 捕捉所有异常
                print(f"llm Request failed: {e}. Retrying...")
                time.sleep(delay)  # 等待一段时间后重试
        
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
    # from config import MODEL_PATH, TOKENIZER_PATH
    # print(MODEL_PATH)
    # print(TOKENIZER_PATH)
    # llm = ChatGLM()
    # llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    # print(llm("望春风"))

    # embbeding 测试
    # from config import EMBEDDING_PATH
    # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    # embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
    #                                 model_kwargs = {'device': "cuda"})   # 未来在这里进行拓展，支持更多 embeddings
    # print(f"embedding model: {EMBEDDING_PATH} loaded successfully!")
    
    # OpenAI 测试
    llm = ChatGLM()
    prompt = "德才兼备，知行合一"
    response = llm(prompt)
    print(response)
    