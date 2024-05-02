import logging
import sys
from llama_index.core import Settings
from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager

# 定义日志
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# 使用LlamaDebugHandler构建事件回溯器，以追踪LlamaIndex执行过程中发生的事件
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
Settings.callback_manager = callback_manager

from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader(input_files=["./北京大学语料.pdf"]).load_data()

from RAG import SentenceWindowRetrieverPack
retriever = SentenceWindowRetrieverPack(documents)
response = retriever.run("北大有心理学吗")
print(response)

# get_llm_inputs_outputs返回每个LLM调用的开始/结束事件
event_pairs = llama_debug.get_llm_inputs_outputs()
# print(event_pairs[0][1].payload.keys())
print(event_pairs[0][1].payload["formatted_prompt"])

