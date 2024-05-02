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
        
        # 本地LLM
        from customLLM import LLM
        pretrained_model_name_or_path = "/root/AI4E/share/chatglm3-6b-128k"
        llm = LLM(pretrained_model_name_or_path)
        self.llm = llm
        
        # 本地 embedding
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
        embed_model = HuggingFaceEmbedding(model_name="/root/AI4E/share/bge-large-zh")
        self.embed_model = embed_model

        # 全局会话设置
        Settings.llm = llm
        Settings.embed_model = embed_model
        self.Settings = Settings

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
    from llama_index.core import SimpleDirectoryReader
    documents = SimpleDirectoryReader(input_files=["./岳飞语料.pdf"]).load_data()
    retriever = SentenceWindowRetrieverPack(documents)
    response = retriever.run("岳飞有什么作品？")
    print(response)
    print(retriever.get_modules())
    
    
