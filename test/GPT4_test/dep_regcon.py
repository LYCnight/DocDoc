from pathlib import Path		
import sys
cur_path = Path(__file__).parent    # 当前目录    DocDoc/test/GPT4_test
test_path = Path(__file__).parent.parent    # 测试目录    DocDoc/test
root_path = Path(__file__).parent.parent.parent    # 项目根目录    DocDoc/
sys.path.append(str(cur_path))
sys.path.append(str(test_path))
sys.path.append(str(root_path))
# print(str(cur_path), str(test_path), str(root_path))
from prompt import prompt
from core.Agent import ContentExpert
from DocDoc import Heading
from prompt import fake_history


def printContent(content:list[Heading]):
    for i in range(len(content)):
        print(content[i].id, content[i].heading, content[i].dep, content[i].level)

def makeJson(content:list[Heading]) -> str:
    json_str = "{\n\t\"content\":[\n"
    length = len(content)
    for i in range(length - 1):
        json_str += '\t\t' + '{"id": ' + str(content[i].id) + ', "heading": "' + content[i].heading + '", "dep": ' + str(content[i].dep) + ', "level": ' + str(content[i].level) + '},'
        json_str += '\n'
    json_str += '\t\t' + '{"id": ' + str(content[length - 1].id) + ', "heading": "' + content[length - 1].heading + '", "dep": ' + str(content[length - 1].dep) + ', "level": ' + str(content[length - 1].level) + '}'
    json_str += '\n'
    json_str += '\t]\n}'
    return json_str

#  -- 读取目录 -- 
# llm = "fake_llm"
# contentExpert = ContentExpert(llm)
# content:list[Heading] = contentExpert.read_content_from_xlsx(str(test_path) + "/content_12h.xlsx")
# printContent(content)
# json:str = makeJson(content)
# print(json)

#  -- 与 GPT-4 交互 --
import os
os.environ["OPENAI_API_KEY"] = "sk-zojBY7XNiHrUW96X957dCc90889c47219a328173F20eA50d" #输入网站发给你的转发key
os.environ["OPENAI_BASE_URL"] = "https://gtapi.xiaoerchaoren.com:8932/v1"
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-4o-2024-05-13",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"}
    # {"role": "user", "content": prompt}
    # {"role": "user", "content": fake_history}
  ]
)
response = completion.choices[0].message.content
print(response)


# history  = f"""<human>: {prompt},
# ---
# <assistant>: {response}"""
# print(fake_history)


# # test for json extract
# import json
# from prompt import fake_result

# # 读取 json 文件
# import re
# json_str = re.search(r'<JSON>(.*?)</JSON>', fake_result, re.DOTALL).group(1)
# try:
#     # 尝试解析JSON数据
#     json_data:dict = json.loads(json_str)
#     print("JSON格式正确") 
#     # 可选：输出解析后的JSON数据，验证内容
#     print(json.dumps(json_data, indent=4, ensure_ascii=False))
# except json.JSONDecodeError as e:
#     print("JSON格式错误:", e)
  
  
# # read_content_from_json
# content:list[Heading] = []
# # print(json_data['content'])
# for row in json_data['content']:
#     heading_obj = Heading(row['id'], row['heading'], [row['dep']], row['level'])
#     content.append(heading_obj)
# printContent(content)
# # # json:str = makeJson(content)
# # print(json)
# # heading_obj = Heading(row['id'], row['heading'], [row['dep']], row['level'])
# # content.append(heading_obj)


# -- 集成至 content_expert --
# llm = "fake_llm"
# contentExpert = ContentExpert(llm)
# # print(contentExpert.chat("你好"))
# content : list[Heading] = contentExpert.gen_content(prompt)


# from prompt import fake_json_str
# import json
# fake_json_data:dict = json.loads(fake_json_str)
# print(fake_json_data)
# content:list[Heading] = contentExpert.read_content_from_json(fake_json_data)
# printContent(content)
# print(type(content[0].id))
# print(type(content[0].heading))
# print(type(content[0].dep))
# print(type(content[0].level))

# -- GPT4 集成至 LLMs.py --
# from LLMs import ChatGLM
# llm = ChatGLM()
# contentExpert = ContentExpert(llm)
# # print(contentExpert.llm("你好"))
# content : list[Heading] = contentExpert.gen_content(prompt)
# printContent(content)


# # -- writer --
# from core.Agent import Writer
# from LLMs import ChatGLM
# from prompt import fake_text, fake_digest, fake_content
# llm = ChatGLM()
# writer = Writer(llm)
# title = "基于JavaSprint与React的云计算平台开发技术报告"
# heading = "数据库设计"
# response, prompt = writer.write_digest(title, heading, fake_text, fake_digest, fake_content)
# print(prompt)
# print("*"*100)
# print(response)

# from prompt import fake_history2
# resp = llm(fake_history2)
# print(resp)

# -- writer.write_without_dep--
# from core.Agent import Writer
# from LLMs import ChatGLM
# from prompt import fake_text, fake_digest, fake_content
# llm = ChatGLM()
# writer = Writer(llm)
# contentExpert = ContentExpert(llm)
# title = "基于JavaSprint与React的云计算平台开发技术报告"
# heading = "数据库设计"
# content:list[Heading] = contentExpert.read_content_from_json(eval(fake_content))
# digest = "digest"
# from DocDoc_with_wic_globalview import get_last_heading
# last_heading = get_last_heading(11, content)
# retrieved_knowledge = "retrieved_knowledge"
# response, prompt = writer.write_without_dep(title, heading, fake_content, digest, last_heading, retrieved_knowledge)
# print(prompt)
# print("*"*100)
# print(response)

# -- writer.write_with_dep--
# from core.Agent import Writer
# from LLMs import ChatGLM
# from prompt import fake_text, fake_digest, fake_content
# llm = ChatGLM()
# writer = Writer(llm)
# contentExpert = ContentExpert(llm)
# title = "基于JavaSprint与React的云计算平台开发技术报告"
# heading = "数据库设计"
# content:list[Heading] = contentExpert.read_content_from_json(eval(fake_content))
# digest = "digest"
# dep_text = "dep_text"
# from DocDoc_with_wic_globalview import get_last_heading
# last_heading = get_last_heading(11, content)
# retrieved_knowledge = "retrieved_knowledge"
# response, prompt = writer.write_with_dep(title, heading, fake_content, digest, last_heading, dep_text, retrieved_knowledge)
# print(prompt)
# print("*"*100)
# print(response)

# -- writer.write_mutation--
# from core.Agent import Writer
# from LLMs import ChatGLM
# from prompt import fake_text, fake_digest, fake_content
# lfrom LLMs import ChatGLM
# writer = Writer(llm)
# contentExpert = ContentExpert(llm)
# title = "基于JavaSprint与React的云计算平台开发技术报告"
# heading = "数据库设计"
# content:list[Heading] = contentExpert.read_content_from_json(eval(fake_content))
# digest = "digest"
# dep_text = "dep_text"
# from DocDoc_with_wic_globalview import get_last_heading
# last_heading = get_last_heading(11, content)
# retrieved_knowledge = "retrieved_knowledge"
# response, prompt = writer.write_mutation(title, heading, fake_content, digest, last_heading, dep_text, retrieved_knowledge)
# print(prompt)
# print("*"*100)
# print(response)

# -- test content_response --
from LLMs import ChatGLM
llm = ChatGLM()
contentExpert = ContentExpert(llm)
prompt = "我想写一本软件工程专业的毕业论文，《基于Java Spring和React的全栈电子商务平台开发》。请你生成目录，并详细说明目录项的依赖关系。"
content, content_response = contentExpert.gen_content(prompt)
print(content_response)