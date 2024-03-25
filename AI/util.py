from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 

from typing import List

def promptlist_Add(promptlist:str, information:str = None) -> List[str]:
    return promptlist

if __name__ == "__main__":
    from core.prompt import promptlist_template_short
    from langchain import PromptTemplate
    information = "德才兼备，知行合一"
    print(promptlist_template_short[0].format(information = information))
