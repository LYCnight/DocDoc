sequential_prompt = """
I want to write a thriller fiction, titled `The Cursed Diary`. Please generate the table of content for me.
"""

sequential_content_prompt = """
The directory is stored in a JSON data structure and encapsulated within <JSON></JSON>, for example:
<JSON>
{
    "content": [
        {"id": 0, "heading": "Environmental Impact Assessment Report on the Construction Project of Comprehensive Treatment of Water System Connection and Rural Water System in Yueyang County", "level": 0},
        {"id": 1, "heading": "Overview", "level": 1},
        {"id": 2, "heading": "Analysis and Judgment of Relevant Environmental Protection Policies", "level": 2},
        {"id": 3, "heading": "Analysis of Consistency with Industrial Policies", "level": 3},
        {"id": 4, "heading": "Analysis of Compliance with Laws and Regulations", "level": 3},
        {"id": 5, "heading": "Analysis of Consistency with Relevant Plans", "level": 3},
        {"id": 6, "heading": "Main Conclusions of the Project's Environmental Impact Assessment Report", "level": 2},
        {"id": 7, "heading": "Conclusions and Recommendations", "level": 1},
        {"id": 8, "heading": "Project Overview", "level": 2},
        {"id": 9, "heading": "Environmental Management", "level": 3},
        {"id": 10, "heading": "Main Environmental Protection Measures", "level": 2},
        {"id": 11, "heading": "Economic Analysis of Environmental Impacts", "level": 3},
        {"id": 12, "heading": "Summary of Environmental Impact Assessment", "level": 3}
    ]
}
</JSON>

### Meaning of Each Field:
- "id": Represents the unique identifier of each directory item, used to distinguish between different directory items.
- "heading": Represents the title of each directory item, describing its content.
- "level": Represents the level or depth of the directory item. "0" usually indicates a first-level directory, "1" indicates a second-level directory, "2" indicates a third-level directory, and so on. For example, for the directory item with id 0, its "level" is 0, indicating that it is the title of the text; for the directory item with id 1, its "level" is 1, indicating that it is a first-level title. This field helps us understand the hierarchical structure of the directory.

### Directory Structure Rules:
All texts can be classified according to the depth of the directory:
- Shallow: Shallow directory structure, with levels ranging from 0 to 1, linear narrative, and no multiple-level directory items.
    - Fiction, News, Opinion articles
- Medium: Multi-level directory structure, with levels ranging from 0 to 3, containing multiple-level directory items.
    - Academic paper, Encyclopedia article
- Deep: Deep directory structure, with levels ranging from 0 to 6, containing deeply multi-level directory items.
    - IT: Software Development Report
    - Medicine: Clinical Study Report
    - Finance: Risk Assessment Report
    - Education: Course Evaluation Report
    - Law: Case Assessment Report
    - Management: Project Management Report
    - Manufacturing: Manufacturing Process Report

### Examples: 
Q: I want to write a science fiction novel with the theme of the moon titled "Under the Moonlight." Could you generate the table of contents for the novel "Under the Moonlight"?
A:
-- Analysis:
The novel falls under the Shallow type of text, with levels ranging from 0 to 1.
-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "Under the Moonlight", "level": 0},
        {"id": 1, "heading": "Prologue", "level": 1},
        {"id": 2, "heading": "The Mysterious Invitation", "level": 1},
        {"id": 3, "heading": "Preparation on Earth", "level": 1},
        {"id": 4, "heading": "Embarking on the Space Journey", "level": 1},
        {"id": 5, "heading": "Anomalies in Space", "level": 1},
        {"id": 6, "heading": "The Moon's Invitation", "level": 1},
        {"id": 7, "heading": "Secrets of the Falling Moon", "level": 1},
        {"id": 8, "heading": "Moonshadow Village", "level": 1},
        {"id": 9, "heading": "Moonshadow Tribe", "level": 1},
        {"id": 10, "heading": "Mysterious Legends", "level": 1},
        {"id": 11, "heading": "The Secret of Moon Ore", "level": 1},
        {"id": 12, "heading": "Dangerous Decision", "level": 1},
        {"id": 13, "heading": "Farewell, Earth", "level": 1},
        {"id": 14, "heading": "Challenges During Return Journey", "level": 1},
        {"id": 15, "heading": "Brave Sacrifice", "level": 1},
        {"id": 16, "heading": "Safe Return", "level": 1},
        {"id": 17, "heading": "After the Return", "level": 1},
        {"id": 18, "heading": "New Horizons", "level": 1},
        {"id": 19, "heading": "Unveiling Secrets", "level": 1},
        {"id": 20, "heading": "Conclusion", "level": 1}
    ]
}
</JSON>

Q: I want to write an opinion article about Trump's defeat in the 2020 US presidential election, titled "2020 US Election | Three Reasons for Trump's Defeat." Please generate the table of contents for me.
A:
-- Analysis:
Opinion articles belong to the Medium category of text, with levels typically ranging from 0 to 3. When writing this opinion article, I believe setting the maximum level to 2 is more appropriate, i.e., level = 0~2. When composing an opinion article, the main goal is to elucidate and support our viewpoints. In this article about Trump's defeat, all three reasons are major points of discussion, while specific examples and arguments serve as sub-points that support these major points. Therefore, each reason (parent entry) should depend on the detailed items used to explain or support it (child entries).
-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "2020 US Election | Three Reasons for Trump's Defeat", "level": 0},
        {"id": 1, "heading": "Introduction", "level": 1},
        {"id": 2, "heading": "First Reason: Handling of the COVID-19 Pandemic", "level": 1},
        {"id": 3, "heading": "Severity of the COVID-19 Pandemic", "level": 2},
        {"id": 4, "heading": "Trump Administration's Response Measures and Issues", "level": 2},
        {"id": 5, "heading": "Public Perception of the Trump Administration's Handling of the Pandemic", "level": 2},
        {"id": 6, "heading": "Second Reason: Trade War Issues", "level": 1},
        {"id": 7, "heading": "Trade Policies Implemented by the Trump Administration", "level": 2},
        {"id": 8, "heading": "Impact of Trade Policies", "level": 2},
        {"id": 9, "heading": "Public Reaction to Trump's Trade War", "level": 2},
        {"id": 10, "heading": "Third Reason: Racial Issues", "level": 1},
        {"id": 11, "heading": "Racial Tensions under the Trump Administration", "level": 2},
        {"id": 12, "heading": "Impact of Racial Issues on Voters", "level": 2},
        {"id": 13, "heading": "Public Perception of Trump's Stance on Racial Issues", "level": 2},
        {"id": 14, "heading": "Conclusion", "level": 1}
    ]
}
</JSON>


### Attention:
1. Please wrap your table of contents within <JSON></JSON> tags. 
2. Make sure your json format is correct

### Task:
"""


sequential_content_prompt_ch = """
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
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `{heading}` of the article `<{title}>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{content}
</content>
<task>
Q: Please write the body content for the table of contents item `{heading}` based on the content.
A:
"""

sequential_write_prompt_ch = """
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
cur_path = Path(__file__).parent    # 当前目录    DocDoc/test/GPT4_test
test_path = Path(__file__).parent.parent    # 测试目录    DocDoc/test
root_path = Path(__file__).parent.parent.parent    # 项目根目录    DocDoc/
sys.path.append(str(cur_path))
sys.path.append(str(test_path))
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

# 生成目录
def genContent(prompt:str) -> list[Heading]:
    '''核心方法：传入prompt，生成content'''
    import time
    delay = 3   # 等待时间，单位：秒  
    
    prompt = sequential_content_prompt + "Q: " + prompt + "\nA:" 
    while True:
        try:
            response:str = llm(prompt)
            print(response)
            json_data:dict = content_expert.extract_json_from_str(response) # 这里有可能会报错
            break   # 成功了就退出循环
        except Exception as e:
            print(f"function `gen_content` faild: {e}. Retrying...")
            time.sleep(delay)    

    content:list[Heading] = []
    for row in json_data['content']:
        heading_obj = Heading(row['id'], row['heading'], row['level'])
        content.append(heading_obj)
    # -- 记录 prompt_log -- 
    global prompt_log_file_path
    with open(prompt_log_file_path, 'a', encoding='utf-8') as file:
        file.write("---- prompt_log for contentExpert ----\n")
        file.write(prompt+"\n")
        file.write(response+"\n\n")
    # -- 记录 prompt_log -- 
    return content

# 打印目录
def printContent(content:list[Heading]) -> None:
    for i in range(len(content)):
        print(content[i].id, content[i].heading, content[i].level)

# 撰写一个目录项的正文
def write_one_round(title:str, heading:str, content: list[Heading]) -> str:
    prompt:str =  sequential_write_prompt.format(title=title, heading=heading, content=content)
    print(prompt)
    text:str = llm(prompt)
    # -- 记录 prompt_log -- 
    global prompt_log_file_path
    with open(prompt_log_file_path, 'a', encoding='utf-8') as file:
        file.write(f"---- prompt_log for write_one_round of heading: `{heading}` ----\n")
        file.write(prompt+"\n\n")
    # -- 记录 prompt_log -- 
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

# ------------------ main ------------------

# -- init --
# llm = ChatGLM()


def write(prompt, title) -> str:
    """传入prompt,生成正文，返回文件路径"""
    # 记录程序开始运行时间，使用时间戳生成唯一的文件名
    start_time = time.time()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    # store to disk
    # - 使用时间戳命名
    global prompt_log_file_path
    # markdown_file_path = str(cur_path) + f'/output/Sequential/seq_genDoc_{timestamp}.md'
    # prompt_log_file_path = str(cur_path) + f'/output/Sequential/seq_prompt_log_{timestamp}.md'
    # - 使用 title 命名
    markdown_file_path = str(cur_path) + f'/output/Sequential/Gen/{title}.md'
    prompt_log_file_path = str(cur_path) + f'/output/Sequential/Log/Log_{title}.md'
    
    content:list[Heading] = genContent(prompt)
    printContent(content)   # 打印 content

    # -- write --
    title:str = content[0].heading   # 获取文章标题
    content_str = content_to_jsonStr(content)  # 将 content 转换为 string 格式的 Json
    # print(content_str)

    # 测试：查看写作的prompt是否正常
    # h = content[1]
    # heading:str = h.heading
    # text:str = write_one_round(title, heading, content_str)
    # h.text = text 

    for i in range(1, len(content)):   # i starts from 1
        h = content[i]
        heading:str = h.heading
        text:str = write_one_round(title, heading, content_str)
        h.text = text 

    # -- assemble full_text --  
    full_text:str = doc_assemble(content)

    # -- store_to_disk --
    # 计算程序运行时间，并保留两位小数
    end_time = time.time()

    # -- 计算程序运行时间 -- 
    run_time_seconds = round(end_time - start_time, 2) # 秒
    # 将秒数转换为分钟和秒的形式
    minutes = int(run_time_seconds // 60)
    seconds = run_time_seconds % 60
    # 格式化为 n分m秒 的形式
    run_time_formatted = f"{minutes}分{seconds:.2f}秒"
    log =  f"算法耗时：`{run_time_formatted}\n"

    # print(markdown_file_path)
    with open(markdown_file_path, 'a', encoding='utf-8') as file:
            file.write(f"运行开始自: {get_current_time()}\n" + f"所用模型：`gpt-4o`, 所用Embed_model:`None`\n") 
            file.write(log)
            file.write(full_text)   
    
    # 打印 生成文件 和 日志文件 的文件地址
    print(markdown_file_path)
    print(prompt_log_file_path)
    
    return markdown_file_path


def make_prompt(title:str, category:str) -> str:
    prompt_template:str = f"""I want to write one {category}, titled "{title}". Please generate the table of content for me."""
    prompt = prompt_template.format(title, category)
    return prompt


if __name__ == "__main__":
    # 测试：生成一个 markdown 文件
    # prompt = "I want to write a thriller fiction, titled `The Cursed Diary`. Please generate the table of content for me."
    # title = "The Cursed Diary"
    # write(prompt, title)
    # print("completed")
    
    from write_all_docs import ExcelHandler
    xlsx_file_path =  str(cur_path) + "/output_refined_sequential.xlsx"
    # /root/AI4E/lzd/DocDoc/test/GPT4_test/output_refined_sequential.xlsx
    excel = ExcelHandler(xlsx_file_path)

    # Iterate through each row in the Excel file
    for row_num, row in enumerate(excel, start=2):
        if(row['Done'] != 1):   # 还没有被处理过
            title: str = row['Title']
            category: str = row['Category']
            prompt: str = make_prompt(title, category)
            # print(prompt)   # for test
            file_path: str = write(prompt, title)
            excel.update_row(row_num, 'Prompt', prompt)
            excel.update_row(row_num, 'Text', file_path)
            excel.update_row(row_num, 'Done', 1)    # if done, set to 1
            # Save the updated Excel file
            excel.save()        # < 边写边存。这样就算程序崩溃我也可以获得一部分结果>

    # Save the updated Excel file
    excel.save()

    print("completed successfully!")