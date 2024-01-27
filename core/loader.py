from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))


from base import Loader  
from typing import Union, List

class Loader_adapter(Loader):
    def load(self, filelist: Union[str, List[str]] = None) -> str:
        '''
        功能：“文件加载”。传入一个或多个文件路径，将其内容转换为字符串进行返回
        '''
        print("I am loader_apdapter. I can load files in multiple formats ")
        
        if filelist is None:
            raise ValueError("filelist cannot be None")
        # 如果只上传一个文件 ： 单个 str
        elif isinstance(filelist, str):
            return self.load_one_file(filelist)
        # 如果只上传一个文件 ： 只包含一个元素的list
        elif (isinstance(filelist, list) and len(filelist) == 1):
            return self.load_one_file(filelist[0])
        # 如果上传多个文件： 包含多个元素的list
        elif isinstance(filelist, list) and len(filelist) > 1:
            content = ""
            for file in filelist:
                content += self.load_one_file(file) + "\n"
            return content
        else:
            raise ValueError("Invalid filelist format")


    def load_one_file(self, file:str) -> str:
        '''
        功能：传入一个文件路径，将其内容转换为字符串进行返回
        '''
        # 使用Path对象获取文件后缀
        file_suffix = Path(file).suffix[1:].lower()

        match file_suffix:
            case "txt":
                txt_loader = Txt_loader()
                content = txt_loader.load(file)
            case "docx":
                word_loader = Word_loader()
                content = word_loader.load(file)
            case "pdf":
                pdf_loader = Pdf_loader()
                content = pdf_loader.load(file)
            case _:
                content = "Unsupported file format"
            
        return content


class Txt_loader(Loader):
    def load(self, filepath:str = None) -> str: 
        '''
        功能：加载 txt 文件
        '''
        # 读取文件内容
        content = ""
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

class Word_loader(Loader):
    def load(self, filepath:str = None) -> str:
        print("I am Word_loader")
        from docx import Document
        doc = Document(filepath)   # load word
        texts = ""
        for paragraph in doc.paragraphs:
            # print(paragraph.text)  # 文本
            texts = texts + paragraph.text + "\n" # 拼接文本 
        return texts


class Pdf_loader(Loader):
    def load(self, file:str = None) -> str:
        print("I am Pdf_loader")


if __name__ == "__main__":
    pass
    import os
    # --- test: 获取文件路径
    # file = "pku/Tree.txt"
    # file_suffix = Path(file).suffix[1:].lower()     # txt
    # print(file_suffix)

    # # --- test: 实例化子类
    # txt_loader = Txt_loader()
    # txt_loader.load()   # 成功

    # --- test: load_one_file
    # file = "pku/Tree.txt"
    # fileloader = Loader_adapter()
    # fileloader.load_one_file(file)

    # -- test:  Word_loader  --
    # filename = '汨罗江洪道治理报告书（2021）.docx'
    # filepath = str(root_path) + "/test/files/" + filename   
    # print(filepath)   # /remote-home/yy/lzd/DocDoc2/test/files/汨罗江洪道治理报告书（2021）.docx
    # from loader import Word_loader
    # word_loader = Word_loader()
    # content = word_loader.load(filepath)
    # print(content)      


    # ---- test: loader_adapter.load(filelist) and load_one_file(filepath) --------
    # from config import import_selecter
    # loader, spliter, retriever, vectordb = import_selecter("spacy", "simple", "faiss")
    # loader.load("")
    # spliter.info()
    # retriever.query_search()

    # filename = '汨罗江洪道治理报告书（2021）.docx'
    # filepath = str(root_path) + "/test/files/" + filename   

    # content = loader.load_one_file(filepath)
    # # print(content) 

    # filelist = ['汨罗江洪道治理报告书（2021）.docx', "长江湖南段三期河道整治工程环境影响报告书（2022）.docx"]
    # # filelist = ['testdocx1.docx', 'testdocx2.docx']
    # filelist = [(str(root_path)+"/test/files/"+file) for file in filelist]
    # print(filelist)   
    # content = loader.load(filelist)
    # print(content)   


    # # 指定输出的txt文件路径
    # output_directory = str(root_path) + "/test/output/"
    # output_txt_path = output_directory + "output.txt"

    # # 确保输出目录存在
    # os.makedirs(output_directory, exist_ok=True)

    # # 将内容写入txt文件
    # with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
    #     txt_file.write(content)

    # print(f"Content has been written to {output_txt_path}")



    # ---------- test:   Txt_loader   ---------------
    # file_path = str(root_path) + "/test/files/中文语料.txt"
    # print(file_path)

    # from loader import Txt_loader
    # txt_laoder = Txt_loader()
    # content = txt_laoder.load(file_path)
    # print(content)

    # --------- test:    Txt_loader   ---------------
    # from loader import Loader_adapter
    # txt_loader = Loader_adapter()       # 多态
    # filelist = ["中文语料.txt", "中文语料2.txt"]
    # filelist = [str(root_path) + "/test/files/" + file    for file in filelist]
    # print(filelist)

    # content = txt_loader.load(filelist)
    # print(content)

