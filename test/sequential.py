sequential_prompt = """
我想写一篇深度学习领域的论文，标题为`VOLO: Vision Outlooker for Visual Recognition`。请你帮我生成目录。
请注意，这是一篇将会投稿于ECCV会议的论文，所以请按照学术论文的风格生成目录。
下面是一些参考信息：
- 文章概要：
视觉识别多年来一直由卷积神经网络（CNN）主导。尽管最近流行的视觉变换器（ViT）在ImageNet分类中展示了基于自注意力模型的巨大潜力，但如果不提供额外数据，其性能仍然不及最新的SOTA CNN。在这项工作中，我们尝试缩小性能差距，并证明基于注意力的模型确实能够超越CNN。
我们发现，限制ViT在ImageNet分类中表现的一个主要因素是它们在将细粒度特征编码到标记表示中的低效率。为了解决这个问题，我们引入了一种新颖的展望注意力，并提出了一种简单且通用的架构，称为Vision Outlooker（VOLO）。与关注于粗粒度水平的全局依赖建模的自注意力不同，展望注意力有效地将细粒度特征和上下文编码到标记中，这被证明对识别性能至关重要，但在自注意力中却被很大程度上忽略了。
实验表明，我们的VOLO在ImageNet-1K分类中达到了87.1%的top-1准确率，这是第一个在这个具有竞争力的基准上超过87%准确率的模型，且无需使用任何额外的训练数据。此外，预训练的VOLO在转移到下游任务时表现良好，如语义分割。在Cityscapes验证集上我们达到了84.3%的mIoU得分，在ADE20K验证集上达到了54.3%。
代码可在https://github.com/sail-sg/volo获得。
- Outlook Attention
原理：Outlook Attention 通过局部窗口内的密集空间聚合来有效地编码细粒度信息，与自注意力机制相比，它通过简单的重塑操作生成注意力权重，从而避免了昂贵的点积注意力计算。
实现：对于每个空间位置 (i, j)，Outlook Attention 计算其与以 (i, j) 为中心的局部窗口内所有邻居的相似度。生成的展望权重直接用作聚合值的注意力权重，通过 Softmax 函数进行重塑。
"""

sequential_content_prompt = """
## rule
目录存储于json数据结构中，并用<JSON></JSON>封装，例如：
<JSON>
{
        "content":[
                {"id": 0, "heading": "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", "level": 0},
                {"id": 1, "heading": "概述", "level": 1},
                {"id": 2, "heading": "分析判定相关环保政策", "level": 2},
                {"id": 3, "heading": "产业政策相符性分析", "level": 3},
                {"id": 4, "heading": "法律法规符合性分析", "level": 3},
                {"id": 5, "heading": "与相关规划符合性分析", "level": 3},
                {"id": 6, "heading": "项目环评报告书的主要结论", "level": 2},
                {"id": 7, "heading": "结论与建议", "level": 1},
                {"id": 8, "heading": "项目概况", "level": 2},
                {"id": 9, "heading": "环境管理", "level": 3},
                {"id": 10, "heading": "主要环保措施", "level": 2},
                {"id": 11, "heading": "环境影响经济损益分析", "level": 3},
                {"id": 12, "heading": "环评总结论", "level": 3}
        ]
}
<JSON>

各个字段的含义
- "id"：表示每个目录项的唯一标识符，可以用来区别不同的目录项。
- "heading"：表示每个目录项的标题，描述了目录项的内容。
- "level"：代表目录项的等级或深度。"0"通常表示这是一级目录，"1"表示二级目录，"2"表示三级目录，以此类推。比如"id"为0的目录项的"level"为0, 它是文本的title; "id"为1的目录项的"level"为1, 它是一级标题。这个字段可以帮助我们了解目录的层次结构。

## task
Q: 我想写一本以月球为主题的科幻小说《月影之下》，请你生成小说《月影之下》的目录，并详细说明目录项的依赖关系。
A: 
<JSON>
{
    "content":[
        {"id": 0, "heading": "月影之下",  "level": 0},
        {"id": 1, "heading": "序言", : 1},
        {"id": 2, "heading": "神秘的邀请函","level": 1},
        {"id": 3, "heading": "地球上的准备", "level": 1},
        {"id": 4, "heading": "太空之旅启程", "level": 1},
        {"id": 5, "heading": "宇宙中的异样", "level": 1},
        {"id": 6, "heading": "月亮的邀请", "level": 1},
        {"id": 7, "heading": "落月的秘密", "level": 1},
        {"id": 8, "heading": "月影村落", "level": 1},
        {"id": 9, "heading": "月影族人", "level": 1},
        {"id": 10, "heading": "神秘的传说", "level": 1},
        {"id": 11, "heading": "月亮矿石的秘密", "level": 1},
        {"id": 12, "heading": "危险的决定", "level": 1},
        {"id": 13, "heading": "再见，地球", "level": 1},
        {"id": 14, "heading": "归航中的挑战", "level": 1},
        {"id": 15, "heading": "勇敢的牺牲", "level": 1},
        {"id": 16, "heading": "安全归航", "level": 1},
        {"id": 17, "heading": "回归之后", "level": 1},
        {"id": 18, "heading": "新的前景", "level": 1},
        {"id": 19, "heading": "解开的秘密", "level": 1},
        {"id": 20, "heading": "结语", "dep": "level": 1}
    ]
}
</JSON>

Q: 我想写一则以关于特朗普在2020美国总统大选中落选的Opinion article，标题为《美国大选2020|特朗普落选的三个原因》，请你生成Opinion article的目录。
A:
<JSON>
{
    "content":[
        {"id": 0, "heading": "美国大选2020|特朗普落选的三个原因", "level": 0},
        {"id": 1, "heading": "引言", "level": 1},
        {"id": 2, "heading": "第一原因：新冠疫情的处理", "level": 1},
        {"id": 3, "heading": "新冠疫情的严重性", "level": 2},
        {"id": 4, "heading": "特朗普政府的应对措施和问题", "level": 2},
        {"id": 5, "heading": "公众对特朗普政府应对疫情的评价", "level": 2},
        {"id": 6, "heading": "第二原因：贸易战问题", "level": 1},
        {"id": 7, "heading": "特朗普政权实施的贸易政策", "level": 2},
        {"id": 8, "heading": "贸易政策带来的影响", "level": 2},
        {"id": 9, "heading": "公众对特朗普贸易战的反应", "level": 2},
        {"id": 10, "heading": "第三原因：种族问题", "level": 1},
        {"id": 11, "heading": "特朗普政府下的种族紧张", "level": 2},
        {"id": 12, "heading": "种族问题对选民的影响", "level": 2},
        {"id": 13, "heading": "美国公众对特朗普种族问题立场的评价", "level": 2},
        {"id": 14, "heading": "结论", "level": 1}
    ]
}
</JSON>

"""

sequential_write_prompt = """
<role>
你是一名写作专家
</role>
<rule>
你正在写作<{title}>的目录项`{heading}`的正文内容。
content: 是文章的目录
</rule>
<constraints>
1. 你只能返回markdoWn格式的文本
2. 你的返回的正文中不能含有 #, ##, ###, ####, #####, ###### 等markdown heading命令
</constraints>
<content>
{content}
</content>
<task>
Q: 请根据content写作目录项`{heading}`的正文内容。
A:
"""


from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc
cur_path = Path(__file__).parent    # 当前目录    /DocDoc/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

from LLMs import ChatGLM
from core.Agent import Writer
from core.Agent import ContentExpert
import time

# init
llm = ChatGLM()
content_expert = ContentExpert(llm)    

class Heading:
    def __init__(self, id, heading, level):
        self.id:int = id
        self.heading:str = heading
        self.level:int = level
        self.text:str = None

# 生成目录
def genContent(prompt:str) -> list[Heading]:
    prompt = sequential_content_prompt + "Q: " + prompt + "\nA:" 
    response:str = llm(prompt)
    json_data:dict = content_expert.extract_json_from_str(response)
    content:list[Heading] = []
    for row in json_data['content']:
        heading_obj = Heading(row['id'], row['heading'], row['level'])
        content.append(heading_obj)
    return content

# 打印目录
def printContent(content:list[Heading]) -> None:
    for i in range(len(content)):
        print(content[i].id, content[i].heading, content[i].level)

# 撰写正文
def write(title:str, heading:str, content: list[Heading]) -> str:
    prompt:str =  sequential_write_prompt.format(title=title, heading=heading, content=content)
    print(prompt)
    text:str = llm(prompt)
    # text = "测试"
    return text

# 组装全文
def doc_assemble(content:list[Heading]) -> str:
    full_text = ""
    title = content[0]
    full_text += f"**{title.heading}**\n"
    for heading in content:
        if heading.level > 0:
            # print("heading:", heading.heading, ", heading->level =", heading.level)
            full_text += "#" * heading.level + " " + heading.heading + "\n"
            if heading.text:
                full_text += heading.text + "\n"
    return full_text

def get_current_time() -> str:
    import time
    import pytz
    from datetime import datetime

    # 获取当前时间的时间戳
    start_time = time.time()

    # 将时间戳转换为datetime对象，并设置时区为UTC
    utc_time = datetime.utcfromtimestamp(start_time).replace(tzinfo=pytz.utc)

    # 强制设置时区为东八区
    tz = pytz.timezone('Asia/Shanghai')
    local_time = utc_time.astimezone(tz)

    # 将强制设置时区后的时间格式化为24小时制的时间字符串
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

def content_to_jsonStr(content:list[Heading]) -> str: 
    json_str = "{\n\t\"content\":[\n"
    length = len(content)
    for i in range(length - 1):
        json_str += '\t\t' + '{"id": ' + str(content[i].id) + ', "heading": "' + content[i].heading +  ', "level": ' + str(content[i].level) + '},'
        json_str += '\n'
    json_str += '\t\t' + '{"id": ' + str(content[length - 1].id) + ', "heading": "' + content[length - 1].heading + ', "level": ' + str(content[length - 1].level) + '}'
    json_str += '\n'
    json_str += '\t]\n}'
    return json_str

# ------------------ main ------------------

# 记录程序开始运行时间，使用时间戳生成唯一的文件名
start_time = time.time()
timestamp = time.strftime("%Y%m%d%H%M%S")

# -- init --
# llm = ChatGLM()

# -- content --

content:list[Heading] = genContent(sequential_prompt)
printContent(content)   # 打印 content

# -- write --
title:str = content[0].heading   # 获取文章标题
content_str = content_to_jsonStr(content)  # 将 content 转换为 string 格式的 Json
print(content_str)

# 测试：查看写作的prompt是否正常
# h = content[1]
# heading:str = h.heading
# text:str = write(title, heading, content_str)
# h.text = text 

for i in range(1, len(content)):   # i starts from 1
    h = content[i]
    heading:str = h.heading
    text:str = write(title, heading, content_str)
    h.text = text 

# -- assemble full_text --  
full_text:str = doc_assemble(content)

# -- store_to_disk --
# 计算程序运行时间，并保留两位小数
end_time = time.time()

# store to disk
markdown_file_path = str(cur_path) + f'/output/sequential/seq_genDoc_{timestamp}.md'

# -- 计算程序运行时间 -- 
run_time_seconds = round(end_time - start_time, 2) # 秒
# 将秒数转换为分钟和秒的形式
minutes = int(run_time_seconds // 60)
seconds = run_time_seconds % 60
# 格式化为 n分m秒 的形式
run_time_formatted = f"{minutes}分{seconds:.2f}秒"
log =  f"算法耗时：`{run_time_formatted}\n"

print(markdown_file_path)
with open(markdown_file_path, 'a', encoding='utf-8') as file:
        file.write(f"运行开始自: {get_current_time()}\n" + f"所用模型：`gpt-4o-2924-05-13`, 所用Embed_model:`None`\n") 
        file.write(log)
        file.write(full_text)   
