from typing import Any

# from llama_index import ServiceContext, SimpleDirectoryReader, SummaryIndex
from llama_index.core import Settings, SimpleDirectoryReader
from llama_index.core.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)

from llama_index.core.llms.callbacks import (
    llm_chat_callback,
    llm_completion_callback,
)

from transformers import AutoTokenizer, AutoModel


# class LLM(CustomLLM):
#     context_window: int = 8192  # 上下文窗口大小
#     num_output: int = 128  # 输出的token数量
#     model_name: str = "Qwen-1_8B-Chat"  # 模型名称
#     tokenizer: object = None  # 分词器
#     model: object = None  # 模型

#     def __init__(self, pretrained_model_name_or_path):
#         super().__init__()

#         # GPU方式加载模型
#         self.model = AutoModel.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True).eval()
#         self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True)
#         # self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, device_map="cuda", trust_remote_code=True)
#         # self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path, device_map="cuda", trust_remote_code=True).eval()

#         # CPU方式加载模型
#         # self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, device_map="cpu", trust_remote_code=True)
#         # self.model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path, device_map="cpu", trust_remote_code=True)
#         # self.model = self.model.float()

#     @property
#     def metadata(self) -> LLMMetadata:
#         """Get LLM metadata."""
#         # 得到LLM的元数据
#         return LLMMetadata(
#             context_window=self.context_window,
#             num_output=self.num_output,
#             model_name=self.model_name,
#         )

#     @llm_completion_callback()  # 回调函数
#     def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
#         # 完成函数
#         print("完成函数")

#         inputs = self.tokenizer.encode(prompt, return_tensors='pt').cuda()  # GPU方式
#         # inputs = self.tokenizer.encode(prompt, return_tensors='pt')  # CPU方式
#         outputs = self.model.generate(inputs, max_length=self.num_output)
#         response = self.tokenizer.decode(outputs[0])
#         return CompletionResponse(text=response)

#     @llm_completion_callback()
#     def stream_complete(
#         self, prompt: str, **kwargs: Any
#     ) -> CompletionResponseGen:
#         # 流式完成函数
#         print("流式完成函数")

#         inputs = self.tokenizer.encode(prompt, return_tensors='pt').cuda()  # GPU方式
#         # inputs = self.tokenizer.encode(prompt, return_tensors='pt')  # CPU方式
#         outputs = self.model.generate(inputs, max_length=self.num_output)
#         response = self.tokenizer.decode(outputs[0])
#         for token in response:
#             yield CompletionResponse(text=token, delta=token)


# if __name__ == "__main__":
#     # 定义你的LLM
#     pretrained_model_name_or_path = "/root/AI4E/share/chatglm3-6b-128k"
#     llm = LLM(pretrained_model_name_or_path)

#     # 本地Embeddin
#     # from llama_index.embeddings.huggingface import HuggingFaceEmbedding
#     # embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh")
#     # EMBEDDING_PATH = "/root/AI4E/share/bge-large-zh"
#     # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
#     # embed_model = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
#     #                                 model_kwargs = {'device': "cuda"})  

#     # embeddings = embed_model.get_text_embedding("Hello World!")
#     # print(len(embeddings))
#     # print(embeddings[:5])

#     Settings.llm = llm
#     # Settings.embed_model = embed_model

#     # # 定义你的服务上下文
#     # service_context = ServiceContext.from_defaults(
#     #     llm=llm, embed_model="local:/root/AI4E/share/bge-large-zh"
#     # )

#     # 加载你的数据
#     # documents = SimpleDirectoryReader(input_files=["./testPDF.pdf"]).load_data()
#     # print(len(documents))
#     # index = SummaryIndex.from_documents(documents, service_context=service_context)

#     # 查询和打印结果
#     # query_engine = index.as_query_engine()
#     # response = query_engine.query("花未眠")
#     # print(response)
