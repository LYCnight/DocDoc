single_prompt_template = """"
Please write one {category} for me entitled “{title}".
### Requirements:
- The structure should be complete, contextualized, and relevant to the topic.
### Note
1. Please write directly in the body, not just an outline.
2. Please write the whole thing, not just parts of it. (e.g. you can't just write an Prologue)
3. Please mark your title within # (markdown format)
4. You can use markdown to give structure to your text
5. You can use markdown to draw some tables or stick paper when needed.
6. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
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
    # timestamp = time.strftime("%Y%m%d%H%M%S")
    
    # store to disk
    # - 使用时间戳命名
    global prompt_log_file_path
    # markdown_file_path = str(cur_path) + f'/output/Sequential/seq_genDoc_{timestamp}.md'
    # prompt_log_file_path = str(cur_path) + f'/output/Sequential/seq_prompt_log_{timestamp}.md'
    # - 使用 title 命名
    markdown_file_path = str(cur_path) + f'/output/Single/Gen/{title}.md'
    prompt_log_file_path = str(cur_path) + f'/output/Single/Log/Log_{title}.md'
    
    # -- write --
    full_text:str = llm(prompt)

    
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

    # 记录日志文件
    with open(prompt_log_file_path, 'a', encoding='utf-8') as file:
        file.write(f"log for \"{title}\"\n")
        file.write(prompt)

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
    prompt = single_prompt_template.format(title=title, category=category)
    print(prompt)
    return prompt


if __name__ == "__main__":
    # 测试：生成一个 markdown 文件
    # prompt = "I want to write a thriller fiction, titled `The Cursed Diary`. Please generate the table of content for me."
    # title = "The Cursed Diary"
    # write(prompt, title)
    # print("completed")
    
    from write_all_docs import ExcelHandler
    xlsx_file_path =  str(cur_path) + "/output_refined_single.xlsx"
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