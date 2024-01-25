from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))


from base import Retriever  

class Simple_retriever(Retriever):
    def query_search(self):
        print("I am Simple_retriever")

class Multivector_retriever(Retriever):
    def query_search(self):
        print("I am Multivector_retriever")

class ParentDoc_retriever(Retriever):
    def query_search(self):
        print("I am ParentDoc_retriever")

