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

class LLM(CustomLLM):
    context_window: int = 8192  # 上下文窗口大小
    num_output: int = 128  # 输出的token数量
    model_name: str = "Qwen-1_8B-Chat"  # 模型名称
    tokenizer: object = None  # 分词器
    model: object = None  # 模型

    def __init__(self, pretrained_model_name_or_path):
        super().__init__()
        # 加载模型
        from transformers import AutoTokenizer, AutoModel
        self.model = AutoModel.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True).eval()
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True)
        import torch
        device = torch.device("cuda:0")  # 使用0号GPU
        self.model.to(device)   # 指定模型运行的显卡

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        # 得到LLM的元数据
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()  # 回调函数
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        # 完成函数
        response, history = self.model.chat(   # 生成回答
            self.tokenizer,
            prompt,
        )
        return CompletionResponse(text=response)

    @llm_completion_callback()
    def stream_complete(
        self, prompt: str, **kwargs: Any
    ) -> CompletionResponseGen:
        # 流式完成函数
        print("流式完成函数")

        inputs = self.tokenizer.encode(prompt, return_tensors='pt').cuda()  # GPU方式
        # inputs = self.tokenizer.encode(prompt, return_tensors='pt')  # CPU方式
        outputs = self.model.generate(inputs, max_length=self.num_output)
        response = self.tokenizer.decode(outputs[0])
        for token in response:
            yield CompletionResponse(text=token, delta=token)


if __name__ == "__main__":
    # 本地LLM
    pretrained_model_name_or_path = "/root/AI4E/share/chatglm3-6b-128k"
    llm = LLM(pretrained_model_name_or_path)
    # print(llm.complete("你好"))
    # 本地 embedding
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh")
    # embeddings = embed_model.get_text_embedding("Hello World!")
    # print(len(embeddings))
    # print(embeddings[:5])

    Settings.llm = llm
    Settings.embed_model = embed_model

    import faiss

    # dimensions of text-ada-embedding-002
    d = 1024    # 不能改！！！
    faiss_index = faiss.IndexFlatL2(d)

    from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
    )
    from llama_index.vector_stores.faiss import FaissVectorStore

    # --------------faiss ---------------
    # 加载你的数据
    documents = SimpleDirectoryReader(input_files=["./岳飞语料.pdf"]).load_data()
    # print(len(documents))
    
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )
    
    # save index to disk
    index.storage_context.persist()
    
    # load index from disk
    vector_store = FaissVectorStore.from_persist_dir("./storage")
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store, persist_dir="./storage"
    )
    index = load_index_from_storage(storage_context=storage_context)

    # set Logging to DEBUG for more detailed outputs
    query_engine = index.as_query_engine()
    response = query_engine.query("岳飞有什么作品吗？") 
    print(response)     # 岳飞的作品有《满江红·怒发冲冠》。
