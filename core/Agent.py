from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))
from core.prompt import (WRITE_WITHOUT_DEP, WRITE_WITH_DEP, WRITE_MUTATION, 
                         GEN_CONTENT_PRELIMINARY, GEN_CONTENT_COMPLETE)
from config import QUES_COUNT, MODEL_CONTEXT_LENGHTH, CUT_DOWN
from DocDoc import Heading


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
        import time
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
        # import time
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
        print("Agent[ContentExpert] loaded successfully")   
    
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
    
    def gen_content_from_title(self, title:str) -> list[Heading]:
        level_1_heading_list:list[Heading] = self.gen_content_preliminary(title)    # 生成一级heading
        content = self.content_assemble(title, level_1_heading_list)  # 生成完整目录
        content = self.format_content(content)    # 目录格式化
        self.check_content_format(content)        # 检查目录格式是否合格
        self.content.clear()    # 先清空上一次生成的目录
        self.content = content
        return self.content
    
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
    
    def gen_content_preliminary(self, title:str, requirement:str=None) -> list[Heading]:
        prompt = GEN_CONTENT_PRELIMINARY.format(title=title, requirement=requirement)
        # print(prompt)     # debug
        response:str = self.llm(prompt)
        # print(response)   # debug
        matches:list[tuple] = self.re_extract(response)
        h_list:list[Heading] = []
        for match in matches:
            id,heading,dep,level = match
            h_list.append(Heading(id, heading, dep, level))
        return h_list
    
    def gen_content_for_one_heading(self, title:str, heading:str, requirement:str=None) -> list[Heading]:
        prompt = GEN_CONTENT_COMPLETE.format(title=title, heading=heading, requirement=requirement)
        # print(prompt)   # debug
        response:str = self.llm(prompt)
        # print(response) # debug
        matches:list[tuple] = self.re_extract(response) # 正则提取
        h_list:list[Heading] = []
        for match in matches:
            id,heading,dep,level = match
            h_list.append(Heading(id, heading, dep, level))
        return h_list
    
    def gen_content(self, title:str, requirement:str=None) -> str:
        prompt = """## role
你是一名环境报告目录专家，擅长根据报告的标题和用户的要求写出优秀的环境报告的目录。
## specification
 - id: heading编号
 - heading：heading标题
 - dep：写作本节内容所需要参考的其他heading的id。若不需要参考，则设置为-1；若需要参考，并且由多个参考id，则用英文逗号","分隔
 - level: 标题等级，文章title的level为0，其余heading的level从1开始
## requirement
 - 短目录：20~60个heading
 - 中目录：120~180个heading
 - 长目录：220~280个heading
## constraints
请按照specification的要求输出目录
""" + \
"""###
Q: 帮我撰写《湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书》的目录。要求：生成一份短目录
A：
[
 {"id": 0, "heading": "湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书", "dep": -1, "level": 0},
 {"id": 1, "heading": "概述", "dep": -1, "level": 1},
 {"id": 2, "heading": "项目背景及项目建设特点", "dep": -1, "level": 2},
 {"id": 3, "heading": "环境影响评价工作过程", "dep": -1, "level": 2},
 {"id": 4, "heading": "分析判定相关情况", "dep": -1, "level": 2},
 {"id": 5, "heading": "关注的主要环境问题", "dep": -1, "level": 2},
 {"id": 6, "heading": "报告书的主要评价结论", "dep": 73, "level": 2},
 {"id": 7, "heading": "总则", "dep": -1, "level": 1},
 {"id": 8, "heading": "编制依据", "dep": -1, "level": 2},
 {"id": 9, "heading": "评价因子与评价标准", "dep": -1, "level": 2},
 {"id": 10, "heading": "评价工作等级和评价重点", "dep": -1, "level": 2},
 {"id": 11, "heading": "评价范围及敏感点", "dep": -1, "level": 2},
 {"id": 12, "heading": "环境功能区划", "dep": -1, "level": 2},
 {"id": 13, "heading": "建设项目工程分析", "dep": -1, "level": 1},
 {"id": 14, "heading": "流域概况", "dep": -1, "level": 2},
 {"id": 15, "heading": "工程健设的必要性分析", "dep": -1, "level": 2},
 {"id": 16, "heading": "工程建设与相关政策、规划的符合性分析", "dep": -1, "level": 2},
 {"id": 17, "heading": "与《湖南东洞庭湖国家级自然保护区总体规划》的符合性分析", "dep": -1, "level": 2},
 {"id": 18, "heading": "与《水产种质资源保护区管理暂行办法》的符合性分析", "dep": -1, "level": 2},
 {"id": 19, "heading": "工程方案的环境合理性分析", "dep": -1, "level": 2},
 {"id": 20, "heading": "华容河现有水利工程概况", "dep": -1, "level": 2},
 {"id": 21, "heading": "现有工程概况", "dep": -1, "level": 2},
 {"id": 22, "heading": "拟建项目概况", "dep": -1, "level": 2},
 {"id": 23, "heading": "工程分析", "dep": -1, "level": 2},
 {"id": 24, "heading": "环境现状调查与评价", "dep": -1, "level": 1},
 {"id": 25, "heading": "自然环境现状", "dep": -1, "level": 2},
 {"id": 26, "heading": "生态敏感区概况", "dep": -1, "level": 2},
 {"id": 27, "heading": "环境质量现状调查", "dep": -1, "level": 2},
 {"id": 28, "heading": "湖南东洞庭湖国家级自然保护区生态环境现状调查与评价", "dep": -1, "level": 2},
 {"id": 29, "heading": "东洞庭湖中国圆田螺国家级水产种质资源保护区生态环境现状调查与评价", "dep": -1, "level": 2},
 {"id": 30, "heading": "区域污染源调查", "dep": -1, "level": 2},
 {"id": 31, "heading": "区域环境问题", "dep": -1, "level": 2},
 {"id": 32, "heading": "环境影响预测与评价", "dep": -1, "level": 1},
 {"id": 33, "heading": "生态环境影响预测和评价", "dep": -1, "level": 2},
 {"id": 34, "heading": "水文情势预测和评价", "dep": -1, "level": 2},
 {"id": 35, "heading": "水环境影响预测和评价", "dep": -1, "level": 2},
 {"id": 36, "heading": "地下水环境影响预测和评价", "dep": -1, "level": 2},
 {"id": 37, "heading": "水土流失预测和评价", "dep": -1, "level": 2},
 {"id": 38, "heading": "大气环境影响预测评价", "dep": -1, "level": 2},
 {"id": 39, "heading": "声环境影响预测和评价", "dep": -1, "level": 2},
 {"id": 40, "heading": "固体废弃物的环境影响", "dep": -1, "level": 2},
 {"id": 41, "heading": "移民安置环境影响评价", "dep": -1, "level": 2},
 {"id": 42, "heading": "社会环境影响评价", "dep": -1, "level": 2},
 {"id": 43, "heading": "对人群健康的影响", "dep": -1, "level": 2},
 {"id": 44, "heading": "环境保护措施", "dep": -1, "level": 1},
 {"id": 45, "heading": "水环境保护措施", "dep": -1, "level": 2},
 {"id": 46, "heading": "大气环境保护措施", "dep": -1, "level": 2},
 {"id": 47, "heading": "噪声控制措施", "dep": -1, "level": 2},
 {"id": 48, "heading": "固体废弃物处置措施", "dep": -1, "level": 2},
 {"id": 49, "heading": "生态保护措施", "dep": -1, "level": 2},
 {"id": 50, "heading": "水土流失防护措施", "dep": -1, "level": 2},
 {"id": 51, "heading": "移民安置保护措施", "dep": -1, "level": 2},
 {"id": 52, "heading": "人群健康保护措施", "dep": -1, "level": 2},
 {"id": 53, "heading": "环境风险分析", "dep": -1, "level": 1},
 {"id": 54, "heading": "环境风险识别", "dep": -1, "level": 2},
 {"id": 55, "heading": "环境风险潜势划分", "dep": -1, "level": 2},
 {"id": 56, "heading": "环境风险分析", "dep": -1, "level": 2},
 {"id": 57, "heading": "环境风险防范与应急措施", "dep": -1, "level": 2},
 {"id": 58, "heading": "应急预案", "dep": -1, "level": 2},
 {"id": 59, "heading": "环境管理与环境监测", "dep": -1, "level": 1},
 {"id": 60, "heading": "环境管理", "dep": -1, "level": 2},
 {"id": 61, "heading": "环境监理", "dep": -1, "level": 2},
 {"id": 62, "heading": "环境监测", "dep": -1, "level": 2},
 {"id": 63, "heading": "环境保护投资与环境影响经济损益分析", "dep": -1, "level": 1},
 {"id": 64, "heading": "环境保护投资估算", "dep": -1, "level": 2},
 {"id": 65, "heading": "经济损益分析", "dep": -1, "level": 2},
 {"id": 66, "heading": "环境影响评价结论", "dep": -1, "level": 1},
 {"id": 67, "heading": "工程概况", "dep": -1, "level": 2},
 {"id": 68, "heading": "环境现状评价结论", "dep": -1, "level": 2},
 {"id": 69, "heading": "环境影响评价结论", "dep": -1, "level": 2},
 {"id": 70, "heading": "主要环境保护措施", "dep": -1, "level": 2},
 {"id": 71, "heading": "环境保护投资概算与效益分析", "dep": -1, "level": 2},
 {"id": 72, "heading": "公众参与结论", "dep": -1, "level": 2},
 {"id": 73, "heading": "综合评价结论", "dep": -1, "level": 2},
 {"id": 73, "heading": "综合评价结论", "dep": -1, "level": 2}
]
""" + \
"""
Q:帮我撰写《{title}》的目录。要求：{requirement}
A:""".format(title=title, requirement=requirement)
        print(prompt)
        print("*"*60)
        response = self.llm(prompt)
        return response
    

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
    