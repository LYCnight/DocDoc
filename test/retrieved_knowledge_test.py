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

# 加载 Agent[Writer]
from core.Agent import Writer
writer = Writer(llm)

print(" -----------without_RAG----------")
title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
heading = "地下水环境现状调查与评价"
retrieved_knowledge = ""
response = writer.write_without_dep(title, heading, retrieved_knowledge)
print(response)
print()


print(" -----------with_RAG----------")
retrieved_knowledge = """1. 岳阳县的地理、地质和水文地质现状数据是什么？
2. 岳阳县的水系分布情况和水文特征是什么？
3. 岳阳县地下水环境质量现状如何？
4. 岳阳县地下水环境质量监测数据和评价结果是什么？
5. 岳阳县地下水环境治理和保护措施的技术可行性和经济成本如何？
6. 岳阳县地下水环境治理和保护措施的实施效果监测数据是什么？
7. 岳阳县地下水环境治理和保护措施的实施效果评估方法和技术路线是怎样的？
8. 岳阳县地下水环境治理和保护措施的实施效果监测数据和评估结果呢？
9. 岳阳县地下水环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估如何？"""
response = writer.write_without_dep(title, heading, retrieved_knowledge)
print(response)



