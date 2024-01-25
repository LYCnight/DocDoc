from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

from typing import List, NoReturn

from base import Outputer

class PdfOutputer(Outputer):
    def info(self):
        print("I am PdfOutputer")

    def output(self, text:str,  outputfile:str = "pdfoutput.pdf", outputpath:str = str(root_path)+"/test/output") -> NoReturn:    
        '''
        将大模型生成的内容输出为pdf
        - text: 大模型的回答
        - outputfile：输出的文件名（带后缀）
        - outputpath：输出路径
        '''
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.pdfbase import pdfmetrics
        from reportlab.lib import  colors
        from reportlab.pdfbase.ttfonts import TTFont

        pdfmetrics.registerFont(TTFont('宋体', str(core_path)+'/fonts/simsun.ttc')) # 字体注册

        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = '宋体'

        pdf_filepath = ""
        if(outputpath[-1] == "/"):
            pdf_filepath = outputpath + outputfile
        elif(outputfile[-1] != "/"):
            pdf_filepath = outputpath + "/" + outputfile 

        text_pdf = text.replace("\n", "<br/>") # 转换为 pdf 的换行符

        doc = SimpleDocTemplate(pdf_filepath, pagesize=letter)
        doc.build([Paragraph(text_pdf, ct)])
        print("*" * 100)
        print(f"{outputfile} 生成完毕！")
        print(f"文件位于：{pdf_filepath}")



if __name__ == "__main__":
    # from outputer import PdfOutputer
    # text = "讨厌红楼梦"
    # pdfOutputer = PdfOutputer()
    # pdfOutputer.output(text)

    # path = str(root_path)+"/test/output/"
    # print(path)     # /remote-home/yy/lzd/DocDoc2/test/output/
    # print(path[-1])   #  /

    file_path = str(root_path) + "/test/files/中文语料.txt"
    print(file_path)

    # # 读取文件内容
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     content = file.read()

    from loader import Loader_adapter
    loader = Loader_adapter()
    content = loader.load(file_path)

    from outputer import PdfOutputer
    pdfOutputer = PdfOutputer()
    pdfOutputer.output(content)





