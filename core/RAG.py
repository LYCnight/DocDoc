from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))
from config import (EMBED_DEVICE, LLM_DEVICE, 
                    INDEX_PATH, KNOWLEDGE_BASE_PATH, 
                    EMBEDDING_PATH)
device = LLM_DEVICE
embed_device = EMBED_DEVICE
# import torch
# embed_device = torch.device("cuda:7") 

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
    model_name: str = "Qwen-1.5-14B-Chat"  # 模型名称
    tokenizer: object = None  # 分词器
    model: object = None  # 模型
        
    def __init__(self, llm):
        super().__init__()
        # 加载模型
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
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = self.tokenizer([text], return_tensors="pt").to(device)
        generated_ids = self.model.generate(model_inputs.input_ids, max_new_tokens=512)
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
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
    #  docs: List[Document] = None,
    def __init__(
        self,
        llm,
        load_index_from_last_time = True,
        **kwargs: Any,
    ) -> None:
        """Init params."""
        # create the sentence window node parser w/ default settings
        self.node_parser = SentenceWindowNodeParser.from_defaults(
            window_size=5,
            window_metadata_key="window",
            original_text_metadata_key="original_text",
        )
        
        # llama_index接口的本地LLM
        llama_index_Customllm = LLM(llm)
        self.llm = llama_index_Customllm
        
        # 本地 embedding
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
        embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_PATH, device=embed_device)
        self.embed_model = embed_model

        # 全局会话设置
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model
        
        # create vectorDB
        self.sentence_index = None
        if load_index_from_last_time == False:           
            import faiss
            d = 1024    # dimensions of bge-large-zh
            faiss_index = faiss.IndexFlatL2(d)
            from llama_index.core import (
                SimpleDirectoryReader,
                load_index_from_storage,
                VectorStoreIndex,
                StorageContext,
            )
            from llama_index.vector_stores.faiss import FaissVectorStore
            # load documents
            path_to_directory = KNOWLEDGE_BASE_PATH
            reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
            documents = reader.load_data()         
            # extract nodes
            nodes = self.node_parser.get_nodes_from_documents(documents)
            # construct index from nodes
            vector_store = FaissVectorStore(faiss_index=faiss_index)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            self.sentence_index = VectorStoreIndex(
                nodes, storage_context = storage_context
            )
        else:
            from llama_index.core import (
                load_index_from_storage,
                StorageContext,
            )
            # load index from disk
            from llama_index.vector_stores.faiss import FaissVectorStore
            vector_store = FaissVectorStore.from_persist_dir(str(root_path)+"/storage")
            storage_context = StorageContext.from_defaults(
                vector_store=vector_store, persist_dir=str(root_path)+"/storage"
            )
            self.sentence_index = load_index_from_storage(storage_context=storage_context)
        
        self.postprocessor = MetadataReplacementPostProcessor(
            target_metadata_key="window"
        )
        self.query_engine = self.sentence_index.as_query_engine(
            similarity_top_k=2,
            # the target key defaults to `window` to match the node_parser's default
            node_postprocessors=[self.postprocessor],
        )

    def persist_to_disk(self, path=INDEX_PATH):
        # index 默认存储路径为 DocDoc/storage
        self.sentence_index.storage_context.persist(path)
        print(f"index persisted successfully! Index path: {path}")

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

    # retriever = SentenceWindowRetrieverPack(llm, load_index_from_last_time=False)
    # query_engine = retriever.query_engine
    # query_list = ["岳飞的文学作品有哪些","北大有心理学吗","东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区的主要保护对象有哪些？"]
    # for q in query_list:
    #     print(query_engine.retrieve(q))
    #     print("-"*60)
    #     print()

    # retriever.persist_to_disk()
    
    # retriever = SentenceWindowRetrieverPack(llm, load_index_from_last_time=True)
    # query_engine = retriever.query_engine
    # query_list = ["岳飞的文学作品有哪些","北大有心理学吗","东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区的主要保护对象有哪些？"]
    # for q in query_list:
    #     print(query_engine.retrieve(q))
    #     print("-"*60)
    #     print()
    
    retriever = SentenceWindowRetrieverPack(llm, load_index_from_last_time=True)
    query_engine = retriever.query_engine
    query_list = ["岳飞的文学作品有哪些","北大有心理学吗","东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区的主要保护对象有哪些？"]
    for q in query_list:
        print(retriever.run(q))
        print("-"*60)
        print()
    
    
    
    # from llama_index.core import SimpleDirectoryReader
    # path_to_directory = str(root_path) + "/UserUploadFiles"
    # reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)
    # documents = reader.load_data()
    # print(len(documents))
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
    
    
