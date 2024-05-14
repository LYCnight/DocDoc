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
# response = contentExpert.gen_content_complete(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", heading="结论与建议")

# 正则提取测试
# text = """
# id:1, heading:概述, dep:-1, level:1  
# id:2, heading:项目背景及项目建设特点, dep:-1, level:2 
# """
# text = """
# id:0, heading:概述, dep:-1, level:1
# id:1, heading:项目背景与必要性, dep:-1, level:2
# id:2, heading:项目简介, dep:-1, level:3
# id:3, heading:项目地理位置及范围, dep:-1, level:4
# id:4, heading:项目目标与功能定位, dep:-1, level:4
# id:5, heading:项目发起与审批情况, dep:-1, level:4
# id:6, heading:项目与区域发展规划关联, dep:-1, level:4
# id:7, heading:水系现状分析, dep:-1, level:3
# id:8, heading:水资源供需状况, dep:-1, level:4
# id:9, heading:水污染状况, dep:-1, level:4
# id:10, heading:生态完整性评估, dep:-1, level:4
# id:11, heading:环境问题与制约因素, dep:-1, level:2
# id:12, heading:环境影响评价的目的与依据, dep:-1, level:3
# id:13, heading:国内外类似项目经验借鉴, dep:-1, level:4
# id:14, heading:环境影响评价工作计划, dep:-1, level:3
# <end>
# """
# response = contentExpert.re_extract(text)
# print(response)

# gen_content_preliminary 测试
# h_list = contentExpert.gen_content_preliminary(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
# # print(h_list)
# for h in h_list:
#     print(h.id, h.heading, h.dep, h.level)

# gen_content_for_one_heading 测试
# h_list = contentExpert.gen_content_for_one_heading(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", heading="概述")
# # print(h_list)
# for h in h_list:
#     print(h.id, h.heading, h.dep, h.level)
# print("here")

# # 全流程测试
# content:list[Heading] = contentExpert.gen_content_from_title(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
# for h in content:
#     print(h.id, h.heading, h.dep, h.level)
    
# for h in content:
#     print(h.heading, type(h.dep))

# 测试 gen_content_preliminary() 得到的heading的各项属性的类型
# h_list = contentExpert.gen_content_preliminary(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
# # print(h_list)
# for h in h_list:
#     print(h.id, h.heading, h.dep, h.level)
# print("******** id ********")
# for h in h_list:
#     print(h.id, type(h.id))  
# print("******** heading ********")
# for h in h_list:
#     print(h.heading, type(h.heading))     
# print("******** dep ********")
# for h in h_list:
#     print(h.dep, type(h.dep)) 
# print("******** level ********")
# for h in h_list:
#     print(h.level, type(h.level)) 

# 测试 gen_content_for_one_heading() 得到的heading的各项属性的类型
# h_list = contentExpert.gen_content_for_one_heading(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", heading="概述")
# # print(h_list)
# for h in h_list:
#     print(h.id, h.heading, h.dep, h.level)
# print("******** id ********")
# for h in h_list:
#     print(h.id, type(h.id))  
# print("******** heading ********")
# for h in h_list:
#     print(h.heading, type(h.heading))     
# print("******** dep ********")
# for h in h_list:
#     print(h.dep, type(h.dep)) 
# print("******** level ********")
# for h in h_list:
#     print(h.level, type(h.level)) 

# ---- 测试 check_content_format ----
# content = [Heading(id="1", heading="北大", dep="-1", level = "1")]
# content = [Heading(id=1, heading="北大", dep=-1, level = 1)]
# contentExpert.check_content_format(content)

# content = [Heading(id=1, heading="北大", dep=[-1, 2], level = 1)]
# contentExpert.check_content_format(content)

# content = [Heading(id=1, heading="北大", dep=[-1, 2], level = "1")]
# contentExpert.check_content_format(content)

# content = []
# contentExpert.check_content_format(content)

# content = [Heading(id=1, heading=123, dep=-1, level=1)]
# contentExpert.check_content_format(content)

# content = [Heading(id=1, heading="北大", dep="test", level=1)]
# contentExpert.check_content_format(content)

# content = [Heading(id=1, heading="北大", dep=[-1, "test"], level=1)]
# contentExpert.check_content_format(content)


# ---- 测试 小连招 ----
# content = contentExpert.gen_content_preliminary(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
# content = contentExpert.format_content(content)    # 目录格式化
# contentExpert.check_content_format(content)        # 检查目录格式是否合格
# contentExpert.print_content_with_format(content)

# # ---- 最终测试 ---- 
# 不输出日志
# content = contentExpert.gen_content_from_title(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书")
# contentExpert.print_content_with_format(content)

# # 测试 ---- persist_to_xlsx() ---- 
# contentExpert.persist_to_xlsx()
# print("here")

# 测试 ---- persist_to_markdown() ----
# content 和 timestamp 都没有指定
# contentExpert.persist_to_markdown()
# 指定了 content，但是没指定 timestamp
# contentExpert.persist_to_markdown(content=[Heading(1, "Test", [-1], 1)])
# 没指定 content，但是指定了 timestamp
# contentExpert.persist_to_markdown(timestamp="1898") # ValueError: when content is None, timestamp must be None, too.
# 同时指定 content 与 timestamp
# contentExpert.persist_to_markdown(content=[Heading(1, "Test", [-1], 1)], timestamp="1898")
# print("here")

# 测试 ---- get_state_from_xlsx -----
xlsx_file_path = str(root_path) + "/test/content.xlsx"
contentExpert.get_state_from_xlsx(xlsx_file_path)
print("*"*10)

# 测试 ---- read_content_from_xlsx() ----
xlsx_file_path = str(root_path) + "/test/content.xlsx"
content:list[Heading] = contentExpert.read_content_from_xlsx(xlsx_file_path)
contentExpert.persist_to_markdown(content=content, timestamp="2024.5.6")

# ---- 最终测试 ---- 
# 输出日志
content = contentExpert.gen_content_from_title(title="岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", trace_log=True)
contentExpert.persist_to_xlsx()
contentExpert.persist_to_markdown()
print(contentExpert.trace_log_file_path)    # 日志文件路径
print("here")
