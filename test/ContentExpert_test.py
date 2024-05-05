from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc2
cur_path = Path(__file__).parent    # 当前目录    /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

# from DocDoc_with_writer_investigator import Heading
class Heading:
    def __init__(self, id, heading, dep, level):
        self.id = id
        self.heading = heading
        self.dep = dep
        self.level = level
        self.text = None
        self.dep_text = []

from config import MODEL_PATH, TOKENIZER_PATH
from LLMs import ChatGLM
print(MODEL_PATH)
print(TOKENIZER_PATH)
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

from core.Agent import ContentExpert
contentExpert = ContentExpert(llm)

# response = contentExpert.gen_content_preliminary(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
response = contentExpert.gen_content_complete(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", heading="结论与建议")
print(response)


