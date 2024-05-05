from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc2
cur_path = Path(__file__).parent    # 当前目录    /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

from config import MODEL_PATH, TOKENIZER_PATH
from LLMs import ChatGLM
print(MODEL_PATH)
print(TOKENIZER_PATH)
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

from core.Agent import ContentExpert
contentExpert = ContentExpert(llm)

response = contentExpert.gen_content(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", requirement="短报告")
print(response)


