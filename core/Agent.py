from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
cur_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(cur_path))
sys.path.append(str(root_path))
from core.prompt import (WRITE_WITHOUT_DEP, WRITE_WITH_DEP, WRITE_MUTATION, 
                         GEN_CONTENT_PRELIMINARY, GEN_CONTENT_FOR_ONE_HEADING,)
from config import QUES_COUNT, MODEL_CONTEXT_LENGHTH, CUT_DOWN, MODEL_PATH
from DocDoc import Heading
import time


class Writer:
    def __init__(self, llm):
        self.llm = llm
        print("Agent[Writer] loaded successfully")
    def write_without_dep(self, title:str, heading:str, retrieved_knowledge:str = None) -> tuple[str,str]:
        prompt = WRITE_WITHOUT_DEP.format(title=title, heading=heading, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return (response, prompt)
    def write_with_dep(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str = None) -> tuple[str,str]:
        prompt = WRITE_WITH_DEP.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return (response, prompt)
    def write_mutation(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str = None) -> tuple[str,str]:
        prompt = WRITE_MUTATION.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return (response, prompt) 
    def formulate(self, text: str) -> str:
        # 替换 #, ##, ###, ####, #####, ###### 等Markdown heading命令
        import re
        text = re.sub(r'#+\s*(.*)', r'\1', text)
        return text
        


def token_length_control(text:list[str], target:int, cutDown:int):
    token_length = tokenCount(text[0])
    while(token_length > target):
        text[0] = text[0][:-cutDown]   # 有个负号，千万别丢了
        token_length = tokenCount(text[0])
    return text[0]

def tokenCount(text:str):
    """输入字符串，返回token长度"""
    from transformers import AutoTokenizer
    from config import  TOKENIZER_PATH
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
    tokens = tokenizer.encode(text, add_special_tokens=False) 
    return len(tokens)
        
        
        
class Investigator:

    ques_count = QUES_COUNT  # 针对单个写作节点，最多问出`ques_count`个问题
    
    def __init__(self, llm, load_index_From_last_time=False):      
        self.llm = llm       
        
        from core.RAG import SentenceWindowRetrieverPack
        self.retriever = SentenceWindowRetrieverPack(llm, load_index_From_last_time)
        self.query_engine = self.retriever.query_engine
        print("Agent[Investigator] loaded successfully")

    def persist_to_disk(self):
        self.retriever.persist_to_disk()

    def answer(self, prompt:str) -> str:
        response:str = self.query_engine.query(prompt)
        return response
    
    def get_retrieved_knowledge(self, title, heading) -> str:
        # 记录开始时间
        start_time = time.time()    # debug
        ques_list = self.get_ques_list(title, heading)
        print(ques_list)
        ans_list = self.get_ans_list(ques_list)
        print(ans_list)
        retrieved_knowledge:str = self.QA_assemble(ques_list=ques_list, ans_list=ans_list)
        print("done")
        # 记录结束时间
        end_time = time.time()      # debug
        execution_time = end_time - start_time      # debug
        print(f"获取`retrieved_knowledge`的运行时间：`{execution_time}`秒")     # debug
        print(f"问题数: `{len(ques_list)}`")    
        print(f"回答数: `{len(ans_list)}`")
        return retrieved_knowledge
        
    def get_relevant_answer(self, ques:str) -> str:
        relevant_context_list:list[str] = self.get_relevant_context_list(ques)
        relevant_context = []
        relevant_context.append("")
        for text in relevant_context_list:
            relevant_context[0] += f"{text}\n"
            relevant_context[0] += f"---\n"
        
        # relevant_context.append("项目建设期间，评价区由于人为活动增加、外来建筑材料的进入、潮湿的生境，将促使蚊虫滋生，鼠类迁移，这些因素在一定程度上增加了引起病虫害爆发的可能性，但是通过严格处理施工期间产生的生活和建筑垃圾、尽量使用本地经过检疫的生物材料、定期对施工区域消毒等措施，可在很大程度上降低造成病虫害爆发的可能性")
        
        # 控制 relevant_context[0] 的长度（Token数）
        target = MODEL_CONTEXT_LENGHTH * 1024  # 单位：K(tokens)
        cutDown = CUT_DOWN * 1024  # 单位：K(tokens)
        # 记录开始时间
        # start_time = time.time()    # debug
        relevant_context[0] = token_length_control(relevant_context, target, cutDown)
        # 记录结束时间
        # end_time = time.time()      # debug
        # execution_time = end_time - start_time      # debug
        # print(f"处理token长度的运行时间：`{execution_time}`秒")     # debug
        # return relevant_context[0]    # debug
        prompt = f"""
# role
你是一名环境专家
# task
根据给出的相关信息，结合你的环境知识，回答问题。
# constraints
请尽可能精确、简短地回答问题，不要输出冗长的回答。

*********
Q:武汉市的总面积是多少平方千米？常住人口数量是多少？
Relevant_contexts:武汉市是中国湖北省的省会城市，也是一个副省级市和超大城市。作为国家中心城市，武汉在国家发展和规划中占有重要地位，是中部地区的中心城市，拥有重要的工业基地、科教基地和综合交通枢纽功能。武汉由13个区组成，总面积为8569.15平方千米，2023年末常住人口达到1377.40万人。 地理位置上，武汉位于江汉平原东部、长江中游，长江与汉江在此交汇，形成了武昌、汉口、汉阳三镇隔江而立的独特格局。城市内部水系发达，水域面积占总面积的四分之一，因此被评为国际湿地城市。 作为中国经济地理的中心，武汉有“九省通衢”之称，是中国内陆最大的水陆空交通枢纽和长江中游的航运中心。高铁网络覆盖中国大部分地区，并且是华中地区唯一可以直航全球五大洲的城市。 武汉市还是长江经济带的核心城市，是中部崛起战略的重要支点，并且是全面创新改革试验区。城市正致力于建设成为具有全国经济中心、高水平科技创新中心、商贸物流中心和国际交往中心四大功能的国家中心城市。 在历史文化方面，武汉是国家历史文化名城，楚文化的重要发祥地。自春秋战国时期起，武汉一直是中国南方的军事和商业重镇。在元代，武汉成为湖广行省的省治，明清时期被誉为“楚中第一繁盛处”和“天下四聚”之一。清末，汉口开埠和洋务运动推动了武汉的现代化进程，使其成为近代中国的重要经济中心。武汉还是辛亥革命的首义之地，在近代史上多次成为全国的政治、军事和文化中心。 经济上，2023年武汉市实现地区生产总值20011.65亿元，同比增长5.7%。
A:武汉市总面积为8569.15平方千米，2023年末常住人口达到1377.40万人。

Q:{ques}
Relevant_contexts:{relevant_context[0]}
A:"""
        print("------------------get_relevant_answer------------------")
        # print(prompt) #  debug
        answer:str = self.llm(prompt)
        print(prompt + answer)  # debug
        return answer
    
    def get_relevant_context_list(self, ques:str) -> list[str]:
        relevant_context_list:list[str] = []
        TextNode_list = self.query_engine.retrieve(ques) 
        for TextNode in TextNode_list:
            relevant_context_list.append(TextNode.get_text())
        return relevant_context_list
    
    def QA_assemble(self, ques_list, ans_list):
        QA:str = ""
        for i in range(len(ques_list)):
            QA += "Q：" + ques_list[i] + "\n"
            QA += "A:" + ans_list[i] + "\n"
            QA += "-----\n"
        return QA
    
    def get_ques_list(self, title, heading) -> list[str]:
        prompt = f"""
# role
你是一名信息搜集专员，为写作者搜集写作所需要的信息。
# constraints
1.列出{self.ques_count}个问题，请严格遵守
2.你只能用中文列出问题
# requirements
问题越具体越好，例如：
    - 不具体的问题：项目所在地周边的大气排放情况
    - 具体的问题：某某市周边的大气排放情况
    
**************************
Q:请分析为了写作《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的`大气、声环境环境保护目标`章节的内容，需要获取哪些信息？
A:
1. 武汉市的地理、气象和大气环境现状数据是什么？//
2. 《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的环境影响预测评估方法和技术路线是什么？//
3. 大气、声环境的质量标准和评价方法是怎样的？//
4. 可以提供大气、声环境监测数据和预测结果吗？特别是项目施工期和运营期的环境影响预测。//
5. 大气、声环境治理和保护措施的技术可行性和经济成本如何？//
6. 有关大气、声环境治理和保护措施的实施效果监测数据是什么？//
7. 大气、声环境治理和保护措施的实施效果评估方法和技术路线是怎样的？特别是湖南省的评估方法。//
8. 大气、声环境治理和保护措施的实施效果监测数据和评估结果呢？//
9. 大气、声环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估如何？//
<END>

Q:请分析为了写作《{title}》的`{heading}`章节的内容，需要获取哪些信息？
A:"""
        response:str = self.llm(prompt)
        print(response)
        
        import re
        pattern = r'\d+\.\s*(.*?)(?:[//])'

        # Extracting questions using findall method
        ques_list:list[str] = re.findall(pattern, response)
        # 控制一下问题数量
        ques_list = ques_list[:self.ques_count]
        
        return ques_list

    def get_ans_list(self, ques_list):
        ans_list:list[str] = []
        for i in range(len(ques_list)):
            ques:str = ques_list[i]
            # ans:str = self.get_relevant_context_list(ques)
            ans:str = self.get_relevant_answer(ques)
            ans_list.append(ans)
        return ans_list
            

class ContentExpert:
    def __init__(self, llm):
        self.llm = llm
        self.content:list[Heading] = []     # 生成的目录
        self.trace_log:bool = False
        self.trace_log_text:str = ""
        self.trace_log_file_path:str = ""
        self.timestamp:str = ""     # gen_content_from_title() 运行时间戳
        self.start_time:float    # gen_content_from_title() 运行开始时间
        print("Agent[ContentExpert] loaded successfully")  
    
    def get_state_from_xlsx(self, xlsx_file_path) -> tuple[int, int, int]:
        """获取 Excel 文件中 heading 的数量、最小 level 和最大 level"""
        import pandas as pd
        df = pd.read_excel(xlsx_file_path)
        num_headings = len(df)
        df_min_level = df['level'].min()
        df_max_level = df['level'].max()
        message = f"`{xlsx_file_path}`信息：\n  - `{num_headings}`个heading\n  - level 范围为 [{df_min_level}, {df_max_level}]\n"
        print(message)
        return num_headings, df_min_level, df_max_level
    
    def read_content_from_xlsx(self, xlsx_file_path:str, min_level:int=None, max_level:int=None) -> list[Heading]:
        """
            - 从xlsx文件中读取指定level范围的目录
            - min_level和max_level用于筛选目录
            - 出于算法底层原理，min_level 必须设置为0，才能让 Agent[Writer] 正常运行
        """
        import pandas as pd
        # 读取 Excel 文件
        df = pd.read_excel(xlsx_file_path)
        # 获取content状态
        num_headings = len(df)          # heading数量
        df_min_level = df['level'].min()   # 最小level
        df_max_level = df['level'].max()   # 最大level
        # 设置本次读取的level范围
        if(min_level == None):
            # min_level = df_min_level   # 最小level
            min_level = 0   # 出于算法底层原理，min_level 必须设置为0，才能让 Agent[Writer] 正常运行
        if(max_level == None):
            max_level = df_max_level   # 最大level
        # 根据 Excel 中的数据构造 Heading 对象的列表
        content:list[Heading] = []
        for index, row in df.iterrows():
            if min_level <= row['level'] <= max_level:
                heading_obj = Heading(row['id'], row['heading'], [row['dep']], row['level'])
                content.append(heading_obj)
        # 输出信息
        message_1 = f"{xlsx_file_path}信息：\n  - `{num_headings}`个heading\n  - level 范围为 [{df_min_level}, {df_max_level}]\n"
        message_2 = f"共读取`{num_headings}`个heading，读取的 level 范围为 [{min_level}, {max_level}]"
        message = message_1 + message_2
        print(message)
        return content
        
    def persist_to_markdown(self, content:list[Heading]=None, timestamp:str=None) -> None:
        if content is not None:
            if(timestamp is not None):
                pass
            else:                       # 生成唯一的文件名，使用时间戳
                timestamp = time.strftime("%Y%m%d%H%M%S")    
        else:
            if(timestamp is not None):
                raise ValueError("when content is None, timestamp must be None, too.")
            else:
                content = self.content
                timestamp = self.timestamp
        # debug
        # content = [Heading(1, "中国大学榜单", [-1], 0), Heading(1, "北大", [-1], 1), Heading(1, "清华", [2,3,4], 2)] 
        # timestamp = "2024.5.6"
        # 构造 markdown
        text:str = ""
        for h in content:
            if(h.level == 0):
                text +=  f"**{h.heading}**\n"
            elif(h.level > 0):
                text += "#" * h.level + " " + h.heading + "\n"
        # 写入markdown
        content_markdown_path = str(root_path) + "/test/content/"
        with open(content_markdown_path + f"content_{timestamp}.md" , 'w', encoding='utf-8') as file:
            file.write(text)
        

    def get_current_content(self) -> list[Heading]:
        """返回当前目录"""
        return self.content
    
    def persist_to_xlsx(self, content: list[Heading]=None) -> None:
        """将当前目录保存为xlsx格式"""
        if(content == None):
            content = self.content 
        # # debug
        # content = [Heading(1, "北大", [-1], 1), Heading(1, "清华", [2,3,4], 2)]   
        import pandas as pd
        # 将数据转换为字典列表
        data = [{"id": item.id, "heading": item.heading, "dep": item.dep, "level": item.level} for item in content]
        # 创建 DataFrame 对象
        df = pd.DataFrame(data)
        # 检测目标文件夹是否存在，不存在则创建它
        import os
        target_folder = str(root_path) + "/test/content/"
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        # 将数据写入 Excel 文件
        xlsx_file_path = target_folder + f"content_{self.timestamp}.xlsx"
        df.to_excel(xlsx_file_path, index=False)
        print(f"content persisted on {xlsx_file_path}")
    
    def gen_content_from_title(self, title:str, trace_log:bool=False, timestamp:str=None) -> list[Heading]:
        """
            - 传入 title，生成完整的目录
            - 默认使用 trace_log 模式，即记录运行日志
            - 默认使用 timestamp 模式，即生成唯一的文件名，使用时间戳
            - trace_log 模式下，记录运行日志，并生成唯一的文件名，使用时间戳
        """
        # 日志
        self.trace_log = trace_log
        # 记录程序开始时间
        self.start_time = time.time()
        if(self.trace_log == True):
            if(timestamp == None):
                # 生成唯一的文件名，使用时间戳
                self.timestamp = time.strftime("%Y%m%d%H%M%S")
            else:
                self.timestamp = timestamp
            self.trace_log_file_path = str(root_path) + f"/test/output/contentLog_{self.timestamp}.txt"
        # 生成目录    
        level_1_heading_list:list[Heading] = self.gen_content_preliminary(title)    # 生成一级heading
        content = self.content_assemble(title, level_1_heading_list)  # 生成完整目录
        content = self.format_content(content)    # 目录格式化
        self.check_content_format(content)        # 检查目录格式是否合格
        self.content.clear()    # 先清空上一次生成的目录
        self.content = content
        # 记录时间
        if(self.trace_log == True):
            # 计算程序运行时间，并保留两位小数
            end_time:float = time.time()
            run_time_seconds = round(end_time - self.start_time, 2) # 秒
            # 将秒数转换为分钟和秒的形式
            minutes = int(run_time_seconds // 60)
            seconds = run_time_seconds % 60
            # 格式化为 n分m秒 的形式
            run_time_formatted = f"{minutes}分{seconds:.2f}秒"
            # 记录生成章节数目、程序运行时间
            run_time =  f"目录算法耗时：`{run_time_formatted}`，共生成`{len(self.content)}`个heading\n"
            model_info = f"所用模型：`{MODEL_PATH}`\n"
            # 打开目录文件，读取原始内容
            with open(self.trace_log_file_path, 'r', encoding='utf-8') as file:
                origin_log = file.read()
            # 拼接新log
            new_log = run_time + model_info + origin_log
            # 再次打开文件，以写入模式覆盖原内容
            with open(self.trace_log_file_path, 'w', encoding='utf-8') as file:
                file.write(new_log)
            # 最后将 self.trace__log 还原为 False
            self.trace_log = False
                
        return self.content 
    
    def gen_content_preliminary(self, title:str, requirement:str=None) -> list[Heading]:
        """传入 title，生成一级heading"""
        prompt = GEN_CONTENT_PRELIMINARY.format(title=title, requirement=requirement)
        response:str = self.llm(prompt)
        if(self.trace_log == True):
            with open(self.trace_log_file_path, 'a', encoding='utf-8') as file:
                # file.write(f"----- prompt for gen_content_preliminary(), title:{title} -----\n" + prompt + "\n")  # 打印 prompt
                file.write(f"----- response for gen_content_preliminary(), title:{title} -----\n" + response + "\n")    # 打印 response
        matches:list[tuple] = self.re_extract(response)
        h_list:list[Heading] = []
        for match in matches:
            id,heading,dep,level = match
            h_list.append(Heading(id, heading, dep, level))
        return h_list
    
    def gen_content_for_one_heading(self, title:str, heading:str, requirement:str=None) -> list[Heading]:
        """传入 heading，生成其下层content"""
        prompt = GEN_CONTENT_FOR_ONE_HEADING.format(title=title, heading=heading, requirement=requirement)
        response:str = self.llm(prompt)      
        if(self.trace_log == True):
            with open(self.trace_log_file_path, 'a', encoding='utf-8') as file:
                # file.write(f"----- prompt for gen_content_for_one_heading(), heading:{heading} -----\n" + prompt + "\n")  # 打印 prompt
                file.write(f"----- response for gen_content_for_one_heading(), heading:{heading} -----\n" + response + "\n")    # 打印 response
        matches:list[tuple] = self.re_extract(response) # 正则提取
        h_list:list[Heading] = []
        for match in matches:
            id,heading,dep,level = match
            h_list.append(Heading(id, heading, dep, level))
        return h_list
    
    
    def print_content_with_format(self, content:list[Heading]):
        if(content == None):
            content = self.content    
        for h in content:
            print(f"id:{h.id}, type:{type(h.id).__name__}  ||  heading:{h.heading}, type:{type(h.heading).__name__}  ||  dep:{h.dep}, type:{type(h.dep).__name__}  ||  level:{h.level}, type:{type(h.level).__name__}")
    
    def print_content(self, content:list[Heading]):
        if(content == None):
            content = self.content
        for h in content:
            print(f"id:{h.id}, heading:{h.heading}, dep:{h.dep} , level:{h.level}")
    
    def check_content_format(self, content:list[Heading]) -> None:
        if(len(content) == 0):
            print("content is Null")
            return
        for h in content:
            assert isinstance(h.heading, str), f"h.heading's type must be str, but now is {type(h.heading).__name__}, and the value is {h.heading}"
            assert isinstance(h.id, int), f"h.id's type must be int, but now is {type(h.id).__name__}, and the value is {h.id}"
            if isinstance(h.dep, list):
                assert all(isinstance(item, int) for item in h.dep), f"Elements in h.dep must be integers, but now is {type(h.dep).__name__}, and the value is {h.dep}"
            else:
                assert isinstance(h.dep, int), f"h.dep's type must be int, but now is {type(h.dep).__name__}, and the value is {h.dep}"
            assert isinstance(h.level, int), f"h.level's type must be int, but now is {type(h.level).__name__}, and the value is {h.level}"
        print("content's format is qualified")
    
    def format_content(self, content:list[Heading]) -> list[Heading]:
        for h in content:
            if(isinstance(h.id, str)):
                h.id = eval(h.id)
            if(isinstance(h.dep, str)):
                h.dep = eval(h.dep)
            if(isinstance(h.level, str)):
                h.level = eval(h.level)
        return content
    
    def re_extract(self, text:str) -> list[tuple]:
        import re
        # 正则表达式模式
        pattern = r"id:(\d+), heading:(.*?), dep:(.*?), level:(\d+)"
        # 使用正则表达式进行匹配
        matches = re.findall(pattern, text)
        return matches
    
    def content_assemble(self, title:str, level_1_heading_list:list[Heading]) -> list[Heading]:
        content:list[Heading] = []  
        id = 0
        level_1_heading_list[0].id = id
        id += 1
        content.append(level_1_heading_list[0]) # add doc title
        level_1_heading_list = level_1_heading_list[1:]    # remove title
        for heading in level_1_heading_list:
            heading_list:list[Heading] = self.gen_content_for_one_heading(title, heading.heading)
            for h in heading_list:
                h.id = id   # 更新序号
                id += 1
                content.append(h)
        return content
    

question = """
1. 请提供岳阳县的地理、气象和大气环境现状数据，包括地理位置、气候类型、气象参数（如温度、湿度、风速等）以及大气污染源分布情况。

2. 请提供岳阳县农村水系现状数据，包括水系分布、水文特征、水质状况等。

3. 请提供《岳阳县水系连通及农村水系综合整治工程建设项目》的环境影响预测评估方法和技术路线。

4. 请提供大气、声环境质量标准和评价方法。

5. 请提供大气、声环境监测数据和预测结果，包括项目施工期和运营期的环境影响预测。

6. 请提供大气、声环境治理和保护措施的技术可行性和经济成本。

7. 请提供大气、声环境治理和保护措施的实施效果监测数据。

8. 请提供大气、声环境治理和保护措施的实施效果评估方法和技术路线。

9. 请提供大气、声环境治理和保护措施的实施效果监测数据和评估结果。

10. 请提供大气、声环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估。
"""

if __name__ == "__main__":
    # text = "大大大大大大大大大大"
    # print(tokenCount(text))
    
    # relevant_context = []
    # relevant_context.append(text)
    # target = 5  # token数量, 122880 = 120k
    # cutDown = 1  # 每次削减的token数量，1024 = 1k
    # relevant_context[0] = token_length_control(relevant_context, target, cutDown)
    # print(relevant_context[0])
    # print(tokenCount(relevant_context[0]))
    
    from config import MODEL_PATH, TOKENIZER_PATH
    from LLMs import ChatGLM
    print(MODEL_PATH)
    print(TOKENIZER_PATH)
    llm = ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    
    investigator = Investigator(llm, load_index_From_last_time=False)
    investigator.persist_to_disk()
    
    # ques = "项目建设期间，哪些因素会促使蚊虫滋生和鼠类迁移？"
    # ans = investigator.get_relevant_answer(ques)
    # print(ans)
    
    title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
    heading = "湖南东洞庭湖国家级自然保护区"
    retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    print(retrieved_knowledge)
    