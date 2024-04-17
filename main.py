from AI.PromptUtil import PromptTemplate
from core.prompt import CONTENT_PROMPT, CONTENT_PROMPT_CONSTRAINTS, CONTENT_PROMPT_WITH_COMMENT
from core.prompt import REVIEW_PROMPT, REVIEW_PROMPT_CONSTRAINTS
from core.prompt import WRITE_PROMPT, WRITER_INSTRUCTOR_PROMPT, WRITER_INSTRUCTOR_PROMPT_CONSTRAINT
from config import MAX_REVIEW_TURNS
from LLMs import ChatGLM
from AI.reviewer import review
from AI.content_expert import Content_Queue
import json
from typing import List, Dict

debug = True
llmDebug = True     # 设为True，则关闭llm，全部用写死的内容来做测试
full_text:str = ""  # 储存全文

# 加载 LLM 模型
from config import MODEL_PATH, TOKENIZER_PATH
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

# 加载 embedding 模型
from config import EMBEDDING_PATH
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
                                model_kwargs = {'device': "cuda"})   # 未来在这里进行拓展，支持更多 embedding

# 输入 title 和 information
title = "长沙市湘江大桥绿色工地建设总结报告"
information = """工地名称：长沙市湘江大桥扩建改造工程 
位置：湖南省长沙市，跨越湘江连接河东与河西区域 
施工单位：湖南路桥建设集团有限责任公司 
工程负责人：李四 设计	
单位：中国交通建设股份有限公司设计研究院 
监理单位：湖南华信工程咨询监理有限公司 
施工周期：2021年5月1日至2023年12月31日"""

# 拼装 目录专家 的提示词
content_prompt = PromptTemplate(
    input_variables=["title", "information"],
    template = CONTENT_PROMPT
).format(title=title, information=information) + CONTENT_PROMPT_CONSTRAINTS

if(debug == True):
    print(content_prompt)

content_str = ""

if llmDebug == False:
    #llm生成目录，string格式
    content_str = llm(content_prompt)
    # 打印 llm 生成的目录
    if debug == True:
        print(content_str)
else:
    content_str = """{
"content" : [
    {"headline": "概述", "level": 1},
    {"headline": "1.项目由来", "level": 2},
    {"headline": "2.环境影响评价的工作过程", "level": 2},
    {"headline": "3.分析判定相关环保政策", "level": 2},
    {"headline": "4.关注的主要环境问题", "level": 2},
    {"headline": "第1章总则", "level": 1},
    {"headline": "1.1 编制依据", "level": 2},
    {"headline": "1.2 评价目的及工作原则", "level": 2},
    {"headline": "1.3 评价标准", "level": 2},
    {"headline": "1.4 环境影响因素识别和评价因子筛选", "level": 2},
    {"headline": "1.5 评价工作等级及评价范围", "level": 2},
    {"headline": "1.6 环境敏感目标", "level": 2},
    {"headline": "1.7 评价重点", "level": 2},
    {"headline": "第2章项目概况及工程分析", "level": 1},
    {"headline": "2.1 项目区概况及存在的问题", "level": 2},
    {"headline": "2.2 项目基本情况", "level": 2},
    {"headline": "2.3 工程设计", "level": 2},
    {"headline": "2.4 工程施工", "level": 2},
    {"headline": "2.5 工程占地处理及移民安置", "level": 2},
    {"headline": "2.6 土石方平衡", "level": 2},
    {"headline": "2.7 工程方案合理性分析", "level": 2},
    {"headline": "2.8 工程分析", "level": 2},
    {"headline": "第3章环境现状调查与评价", "level": 1},
    {"headline": "3.1 自然环境概况", "level": 2},
    {"headline": "3.2 项目区生态保护区调查", "level": 2},
    {"headline": "3.3 环境质量现状调查与评价", "level": 2},
    {"headline": "3.4 防洪排涝现状", "level": 2},
    {"headline": "3.5 区域水资源开发利用现状", "level": 2},
    {"headline": "3.6 区域污染源调查", "level": 2},
    {"headline": "第4章环境影响预测与评价", "level": 1},
    {"headline": "4.1 大气环境影响分析", "level": 2},
    {"headline": "4.2 地表水环境影响分析", "level": 2},
    {"headline": "4.3 声环境影响预测与评价", "level": 2},
    {"headline": "4.4 地下水环境影响分析", "level": 2},
    {"headline": "4.5 固体废物对环境的影响分析", "level": 2},
    {"headline": "4.6 生态环境影响分析", "level": 2},
    {"headline": "4.7 水土流失影响分析", "level": 2},
    {"headline": "4.8 环境风险评价", "level": 2},
    {"headline": "第5章环境保护措施", "level": 1},
    {"headline": "5.1 大气环境保护措施", "level": 2},
    {"headline": "5.2 水环境保护措施", "level": 2},
    {"headline": "5.3 声环境保护措施", "level": 2},
    {"headline": "5.4 固体废物污染防治措施", "level": 2},
    {"headline": "5.5 生态保护措施", "level": 2},
    {"headline": "5.6 水土保持措施", "level": 2},
    {"headline": "5.7 人群健康保护措施", "level": 2},
    {"headline": "5.8 环保措施及投资估算", "level": 2},
    {"headline": "第6章环境影响经济损益分析", "level": 1},
    {"headline": "6.1 环保投资估算", "level": 2},
    {"headline": "6.2 环境影响经济损益分析", "level": 2},
    {"headline": "6.3 小结", "level": 2},
    {"headline": "第7章环境管理与环境监测计划", "level": 1},
    {"headline": "7.1 环境管理", "level": 2},
    {"headline": "7.2 环境监测", "level": 2},
    {"headline": "7.3 环境监理", "level": 2},
    {"headline": "7.4 环境保护竣工验收", "level": 2},
    {"headline": "第 8 章 结论与建议", "level": 1},
    {"headline": "8.1 项目概况", "level": 2},
    {"headline": "8.2 环境质量现状评价结论", "level": 2},
    {"headline": "8.3 环境影响评价结论", "level": 2},
    {"headline": "8.4 主要环保措施", "level": 2},
    {"headline": "8.5 环境影响经济损益分析", "level": 2},
    {"headline": "8.6 环评总结论", "level": 2},
    {"headline": "8.7 建议", "level": 2}
]
}"""
    

max_review_turns = MAX_REVIEW_TURNS
while(max_review_turns > 0):
    
    # 拼装 审核员 的提示词
    review_prompt = PromptTemplate(
        input_variables=["text"],
        template = REVIEW_PROMPT
    ).format(text=content_str) + REVIEW_PROMPT_CONSTRAINTS

    # 审核员对内容进行审核
    thinking_process, conclusion, is_qualified, comment = review(review_prompt, llm, debug=True)
    # 最大审核轮数 -1
    max_review_turns -= 1

    if(is_qualified):   
        break #审核通过，跳出循环
    else:
        # 审核未通过，要求内容生产者修改内容
        content_prompt_with_comment = PromptTemplate(
            input_variables=["title", "information", "result_last_time", "comment"],
            template = CONTENT_PROMPT_WITH_COMMENT
        ).format(title=title, information=information, result_last_time=content_str, comment=comment) + CONTENT_PROMPT_CONSTRAINTS

        if debug == True:
            print(content_prompt_with_comment)

        content_str= llm(content_prompt_with_comment)

if debug == True:
    print(f"审核完成, 总共历经{MAX_REVIEW_TURNS - max_review_turns}轮审核")
    print("优化后的目录：\n", content_str)



# ----------------写作模块-----------------
# 解析 JSON 数据
content_json = json.loads(content_str) 

# 获取目录列表
headline_list: List[Dict] = content_json["content"]

# 构造目录队列
conQue = Content_Queue(headline_list)

# 遍历队列列表
if debug == True:
    for headline in headline_list:
        print(f"{headline['headline']}, level: {headline['level']}")

# ------写作循环------
# 检查 conQue 是否为`非空` 
#while conQue.empty() != True:

# 取出队头的目录（Dict 格式）
current_headline_dict:Dict = conQue.pop()
current_headline = current_headline_dict['headline']

# 取出下一个目录
next_headline = ""
if(conQue.empty() != True):
    next_headline_dict = conQue.top()
    next_headline = next_headline_dict['headline']
else:
    next_headline = "文章结尾"



# 构造 写作专家领导 提示词
write_instructor_prompt = PromptTemplate(
    input_variables=["title", "content", "headline", "next_headline"],
    template = WRITER_INSTRUCTOR_PROMPT
).format(title=title, content=content_str, 
            headline=current_headline,
            next_headline=next_headline) + WRITER_INSTRUCTOR_PROMPT_CONSTRAINT

# 打印 写作专家领导 提示词
if debug == True:
    print("*" * 50 + "写作专家-提示词" + "*" * 50)
    print(write_instructor_prompt)

# 写作专家领导 生成响应
write_instructor_response_str = llm(write_instructor_prompt)

# 打印 llm 的响应
if debug == True:
    print("*" * 50 + "写作专家的响应-str格式" + "*" * 50)
    print(write_instructor_response_str)

# 段落写作
write_instructor_response_json = json.loads(write_instructor_response_str)

# 获取段落写作指导列表
para_guide_list : List[Dict] = write_instructor_response_json["para_guide_list"]

# 储存上下文 (just for context between current_headline and next_headline)
context = ""

# 段落写作循环
for i, para_guide_dict in enumerate(para_guide_list, start=1):
    # 获取该段落的段落写作指导
    para_guide:str = para_guide_dict["para_guide"]
    
    # 构造 写作专家 提示词
    write_prompt = PromptTemplate(
        input_variables=["title", "current_headline", "next_headline", "i", "para_guide", "context"],
        template = WRITE_PROMPT
    ).format(title=title, current_headline=current_headline, next_headline=next_headline,
             i=i, para_guide=para_guide, context = context) 
    # 打印 写作专家 的提示词
    if debug == True:
        print("*" * 50 + f"`{current_headline}`-第{i}段-写作专家的提示词-str格式" + "*" * 50)
        print(write_prompt)
    
    # 获得 写作专家 的响应
    para = llm(write_prompt)
    # 打印 写作专家 的响应
    if debug == True:
        print("*" * 50 + f"`{current_headline}`-第{i}段的内容-str格式" + "*" * 50)
        print(para)
    
    # 拼装上下文
    context += para

print("*" * 50 + f"`{current_headline}`的内容-str格式" + "*" * 50)
print(context)

# 拼装全文
full_text += context










