from abc import ABC, abstractmethod 
from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录
sys.path.append(str(root_path))

from transformers import AutoTokenizer, AutoModel
from typing import NoReturn

class LLM():
    tokenizer: object = None
    model: object = None

    def __init__(self):
        pass

    def __call__(self, prompt: str) -> str:  # 模型响应
        '''
        - 功能：
            接收prompt，生成并返回回答
        '''
        pass

    def load_model(self, 
                MODEL_PATH: str = "THUDM/chatglm-6b", 
                TOKENIZER_PATH: str = "THUDM/chatglm-6b") -> NoReturn:
        '''
        - 功能：
            接受模型地址，加载AI模型
        '''
        pass

class Loader(ABC):  
    def __init__(self):  # 构造方法
        pass

    @abstractmethod      # @abstractmethod 抽象方法必须在子类中实现
    def load(self,*args,**kwargs):
        '''
        类型：抽象方法
        功能：加载模型
        '''
        pass


class Spliter(ABC):  
    def __init__(self):
        pass

    @abstractmethod      # @abstractmethod 抽象方法必须在子类中实现
    def split(self,*args,**kwargs):
        '''
        类型：抽象方法
        功能：分割文本（字符串）
        '''
        pass



class Retriever(ABC):
    def __init__(self):
        pass

    @abstractmethod      # @abstractmethod 抽象方法必须在子类中实现
    def query_search(self,*args,**kwargs):
        '''
        类型：抽象方法
        功能：文本检索
        '''
        pass



class Vectordb(ABC):
    def __init__(self):
        pass

    @abstractmethod      # @abstractmethod 抽象方法必须在子类中实现
    def store(self,*args,**kwargs):
        '''
        类型：抽象方法
        功能：知识存储
        '''
        pass

class Outputer(ABC):
    def __init__(self):
        pass

    @abstractmethod      # @abstractmethod 抽象方法必须在子类中实现
    def output(self,*args,**kwargs):
        '''
        类型：抽象方法
        功能：输出成各种各样的产品（pdf，word，PPT...）
        '''
        pass