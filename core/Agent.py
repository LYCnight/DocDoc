from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))
from core.prompt import WRITE_WITHOUT_DEP, WRITE_WITH_DEP, WRITE_MUTATION


class Writer:
    def __init__(self, llm):
        self.llm = llm
        print("Agent[Writer] loeaded successfully")
    def write_without_dep(self, title:str, heading:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_WITHOUT_DEP.format(title=title, heading=heading, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response
    def write_with_dep(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_WITH_DEP.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response
    def write_mutation(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_MUTATION.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response
    




