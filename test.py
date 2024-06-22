class ChatGLM:

    def __call__(self, prompt: str) -> str:  # 模型响应
        completion = self.get_completion_until_success(prompt)
        # -----------------------------------
        
        response = completion.choices[0].message.content
        return response

    @staticmethod
    def get_completion_until_success(prompt, delay=2):
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
                    # {"role": "user", "content": prompt}
                    # {"role": "user", "content": fake_history}
                ]
                )
                return completion
            except Exception as e:  # 捕捉所有异常
                print(f"Request failed: {e}. Retrying...")
                time.sleep(delay)  # 等待一段时间后重试
                
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