from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
cur_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(cur_path)) 

# 加载 LLM 模型
from config import MODEL_PATH, TOKENIZER_PATH
from LLMs import ChatGLM
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

from core.Agent import Investigator
title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
heading = "地下水环境现状调查与评价"
# title = "南杨州码头项目环境影响报告书"
# heading = "大气环境影响预测与评价"
print()
investigator = Investigator(llm)

# ques_list:list[str] = investigator.get_ques_list(title=title, heading=heading)
# print(ques_list)

# ans_list = investigator.get_ans_list(ques_list)
# print(ans_list)


retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
print("-----------------------")
print(retrieved_knowledge)

# retrieved_knowledge = investigator.get_retr


# from core.RAG import SentenceWindowRetrieverPack
# from llama_index.core import SimpleDirectoryReader

# path_to_directory = str(root_path) + "/UserUploadFiles"
# reader = SimpleDirectoryReader(input_dir=path_to_directory, recursive=True)

# documents = reader.load_data()
# retriever = SentenceWindowRetrieverPack(documents)
# response = retriever.run("华盛顿在哪里")
# print(response)










