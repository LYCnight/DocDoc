from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))


"""define local LLM"""
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

    # def __init__(self, pretrained_model_name_or_path):
    #     super().__init__()
    #     # 加载模型
    #     from transformers import AutoTokenizer, AutoModel
    #     self.model = AutoModel.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True).eval()
    #     self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True)
    #     import torch
    #     device = torch.device("cuda:0")  # 使用0号GPU
    #     self.model.to(device)   # 指定模型运行的显卡
        
    def __init__(self, llm):
        super().__init__()
        # 加载模型
        from transformers import AutoTokenizer, AutoModel
        self.model = llm.model
        self.tokenizer = llm.tokenizer

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


"""Sentence window retriever."""

from typing import Any, Dict, List

from llama_index.core import ServiceContext
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core.llama_pack.base import BaseLlamaPack
from llama_index.core.node_parser import (
    SentenceWindowNodeParser,
)
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI


class SentenceWindowRetrieverPack(BaseLlamaPack):
    """Sentence Window Retriever pack.

    Build input nodes from a text file by inserting metadata,
    build a vector index over the input nodes,
    then after retrieval insert the text into the output nodes
    before synthesis.

    """

    def __init__(
        self,
        llm,
        docs: List[Document] = None,
        **kwargs: Any,
    ) -> None:
        """Init params."""
        # create the sentence window node parser w/ default settings
        self.node_parser = SentenceWindowNodeParser.from_defaults(
            window_size=5,
            window_metadata_key="window",
            original_text_metadata_key="original_text",
        )
        
        # # llama_index接口的本地LLM
        # pretrained_model_name_or_path = "/root/AI4E/share/chatglm3-6b-128k"
        # llm = LLM(pretrained_model_name_or_path)
        # self.llm = llm
        
        # llama_index接口的本地LLM
        llama_index_Customllm = LLM(llm)
        self.llm = llama_index_Customllm
        
        # 本地 embedding
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
        embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh")
        self.embed_model = embed_model

        # 全局会话设置
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        # self.Settings = Settings

        # local 会话设置
        # self.service_context = ServiceContext.from_defaults(
        #     llm=self.llm,
        #     embed_model=self.embed_model,
        # )
        
        # extract nodes
        nodes = self.node_parser.get_nodes_from_documents(docs)
        
        # create vectorDB
        self.sentence_index = VectorStoreIndex(
            nodes
        )
        
        # self.sentence_index = VectorStoreIndex(
        #     nodes, service_context=self.service_context
        # )
        
        self.postprocessor = MetadataReplacementPostProcessor(
            target_metadata_key="window"
        )
        self.query_engine = self.sentence_index.as_query_engine(
            similarity_top_k=2,
            # the target key defaults to `window` to match the node_parser's default
            node_postprocessors=[self.postprocessor],
        )

    def get_modules(self) -> Dict[str, Any]:
        """Get modules."""
        return {
            "sentence_index": self.sentence_index,
            "node_parser": self.node_parser,
            "postprocessor": self.postprocessor,
            "llm": self.llm,
            "embed_model": self.embed_model,
            "query_engine": self.query_engine,
            "Settings": self.Settings,
        }

    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Run the pipeline."""
        return self.query_engine.query(*args, **kwargs)
    
if __name__ == "__main__":
    # 测试
    from LLMs import ChatGLM
    from config import MODEL_PATH, TOKENIZER_PATH
    print(MODEL_PATH)
    print(TOKENIZER_PATH)
    llm = ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    print(llm("望春风"))
    
    from llama_index.core import SimpleDirectoryReader
    path_to_directory = str(root_path) + "/UserUploadFiles"
    reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
    documents = reader.load_data()
    print(len(documents))
    # retriever = SentenceWindowRetrieverPack(llm, documents)
    # response = retriever.run("说说水环境保护")
    # print(response)
    
    
    
    # 测试
    # from llama_index.core import SimpleDirectoryReader
    
    # path_to_directory = str(cur_path) + "/files"
    # reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
    # # reader = SimpleDirectoryReader(input_files=["./北京大学语料.pdf"])
    
    # documents = reader.load_data()
    # retriever = SentenceWindowRetrieverPack(documents)
    # response = retriever.run("华盛顿在哪里")
    # print(response)
    # # print(retriever.get_modules())
    
    
