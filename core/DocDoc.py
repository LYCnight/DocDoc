from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

class Heading:
    def __init__(self, id, heading, dep, level):
        self.id:int = id
        self.heading:str = heading
        self.dep:list[int] = dep
        self.level:int = level
        self.text:str = None
        self.dep_text:list[str] = []

class TreeNode:
    def __init__(self, heading):
        self.heading = heading
        self.childlist = []
        
        