import json
import queue
from typing import List, Dict

# ----------------写作模块 JSON 解析 --------------------------
response_str = """
{
    "content" : {"headline":"第一章 项目背景与概述", "level": "1"},
    "text" : "Dumpling Recipe:\\n\\nIngredients:\\n- 2 cups all-purpose flour\\n- 1/2 teaspoon salt\\n- 3/4 cup water\\n- 1 pound ground pork\\n"
}
"""


response_json = json.loads(response_str)
headline = response_json['content']['headline']
level = response_json['content']['level']
text:str = response_json['text'] 

# 打印 Json 数据，测试 JSON 是否解析成功
print("*" * 50 + "解析写作专家的响应-JSON格式" + "*" * 50)
print("headline: " +  headline + ", level: " + level)
print("text: \n" + text)



# ----------------目录模块 JSON 解析 --------------------------
# class Content_Queue:
#     def __init__(self, headline_list):
#         self.queue = queue.Queue()
#         for headline in headline_list:
#             self.queue.put(headline)

#     def top(self):
#         """
#         获取队列头部元素
#         """
#         try:
#             # 获取队列头部元素
#             headline = self.queue.queue[0]
#             return headline
#         except IndexError:
#             print("Queue is empty")
#             return None

#     def pop(self):
#         """
#         获取并弹出头部元素
#         """
#         try:
#             headline = self.queue.get_nowait()
#             return headline
#         except queue.Empty:
#             print("Queue is empty")
#             return None

#     def empty(self):
#         return self.queue.empty()

#     def push(self, headline):
#         self.queue.put(headline)


# content_str = """{
#   "content" : [
#         {"headline": "第一章 项目背景与概述", "level" : 1},
#         {"headline": "1.1 项目名称与位置", "level" : 2},
#         {"headline": "1.2 项目背景", "level" : 3},
#         {"headline": "1.3 项目目的", "level" : 3},
#         {"headline": "1.4 项目意义", "level" : 3},
#         {"headline": "1.5 项目概况", "level" : 3},
#         {"headline": "第二章 项目管理与组织结构", "level" : 1},
#         {"headline": "2.1 建设单位", "level" : 2},
#         {"headline": "2.2 设计单位", "level" : 2},
#         {"headline": "2.3 监理单位", "level" : 2},
#         {"headline": "2.4 施工单位", "level" : 2},
#         {"headline": "第三章 绿色施工技术", "level" : 1},
#         {"headline": "3.1 绿色施工理念", "level" : 2},
#         {"headline": "3.2 绿色施工措施", "level" : 3},
#         {"headline": "3.3 绿色施工评价体系", "level" : 3},
#         {"headline": "第四章 工程进度与质量控制", "level" : 1},
#         {"headline": "4.1 施工进度管理", "level" : 2},
#         {"headline": "4.2 质量控制措施", "level" : 3},
#         {"headline": "4.3 工程验收与评价", "level" : 3},
#         {"headline": "第五章 项目效益与社会影响", "level" : 1},
#         {"headline": "5.1 经济效益", "level" : 2},
#         {"headline": "5.2 社会效益", "level" : 2},
#         {"headline": "5.3 环境影响", "level" : 2},
#         {"headline": "第五章 项目管理与组织结构", "level" : 1},
#         {"headline": "5.4 项目团队建设", "level" : 2},
#         {"headline": "5.5 项目风险管理", "level" : 2},
#         {"headline": "5.6 项目总结与经验", "level" : 3},
#         {"headline": "参考文献", "level" : 1},
#         {"headline": "致谢", "level" : 1}
#       ]
# }"""

# # 解析 JSON 数据
# data = json.loads(content_str)

# # 获取目录列表
# headline_list = data["content"]

# # 获取目录列表
# headline_list: List[Dict] = data["content"]

# # 构造目录队列
# cq = Content_Queue(headline_list)


# # 遍历队列列表
# for headline in headline_list:
#     print(f"{headline['headline']}, level: {headline['level']}")

# # 遍历目录队列
# # while(cq.empty() != True):
# #     print(cq.pop())
# #     """输出
# #     {'headline': '第一章 项目背景与概述', 'level': 1}
# #     {'headline': '1.1 项目名称与位置', 'level': 2}
# #     {'headline': '1.2 项目背景', 'level': 3}
# #     """



