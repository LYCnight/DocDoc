from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 

from AI.AIdoc import AIgen_doc

import time
# 记录开始时间
start_time = time.time()

ProjectPath = "/remote-home/yy/lzd/DocDoc" 
MODEL_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
TOKENIZER_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"

from LLMs import ChatGLM
llm= ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                    model_kwargs = {'device': "cuda"})

doc = AIgen_doc("张靖皋长江大桥ZJG-A5标段绿色工地建设阶段性工作总结", llm)

from core.outputer import PdfOutputer
pdfOutputer = PdfOutputer()
pdfOutputer.output(doc, outputfile="绿色工地报告.pdf")

# 记录结束时间
end_time = time.time()
# 计算运行时间
elapsed_time = end_time - start_time
print(f"程序运行时间：{elapsed_time} 秒")
print(f"程序运行时间：{elapsed_time/60} 分钟")