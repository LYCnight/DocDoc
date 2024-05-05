from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

class Heading:
    def __init__(self, id, heading, dep, level):
        self.id = id
        self.heading = heading
        self.dep = dep
        self.level = level
        self.text = None
        self.dep_text = []

class TreeNode:
    def __init__(self, heading):
        self.heading = heading
        self.childlist = []
        
        