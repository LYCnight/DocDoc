from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))
from core.prompt import WRITE_WITHOUT_DEP, WRITE_WITH_DEP, WRITE_MUTATION


class Writer:
    def __init__(self, llm):
        self.llm = llm
        print("Agent[Writer] loaded successfully")
    def write_without_dep(self, title:str, heading:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_WITHOUT_DEP.format(title=title, heading=heading, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response
    def write_with_dep(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_WITH_DEP.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response
    def write_mutation(self, title:str, heading:str, dep_text:str, retrieved_knowledge:str) -> str:
        prompt = WRITE_MUTATION.format(title=title, heading=heading, dep_text=dep_text, retrieved_knowledge=retrieved_knowledge)
        response:str = self.llm(prompt)
        return response 
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
    
    path_to_directory = str(root_path) + "/UserUploadFiles"
    ques_count = 2  # 最多问出`ques_count`个问题
    
    def __init__(self, llm):
        from llama_index.core import SimpleDirectoryReader
        from core.RAG import SentenceWindowRetrieverPack        
        reader = SimpleDirectoryReader(input_dir = self.path_to_directory, recursive = True) 
        ## 加载用户上传的数据
        documents = reader.load_data()
        retriever = SentenceWindowRetrieverPack(llm, documents)
        query_engine = retriever.query_engine
        
        self.llm = llm
        self.query_engine = query_engine
        self.retriever = retriever  
        print("Agent[Investigator] loaded successfully")
    
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
        target = 122880  # token数量, 122880 = 120k
        cutDown = 1024  # 每次削减的token数量，1024 = 1k
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
    
    investigator = Investigator(llm)
    
    # ques = "项目建设期间，哪些因素会促使蚊虫滋生和鼠类迁移？"
    # ans = investigator.get_relevant_answer(ques)
    # print(ans)
    
    title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
    heading = "湖南东洞庭湖国家级自然保护区"
    retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    print(retrieved_knowledge)
    # ques_list = investigator.get_ques_list(title, heading)
    # print(f"最大问题数量: {investigator.ques_count}")
    # print(ques_list)
    # print(len(ques_list))
    
#     def get_ques_list(question):
#         prompt = """
# Q：
# 1. 请提供武汉市的地理、气象和大气环境现状数据，包括地理位置、气候类型、气象参数（如温度、湿度、风速等）以及大气污染源分布情况。
# 3. 请提供《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的环境影响预测评估方法和技术路线。
# 4. 请提供大气、声环境质量标准和评价方法。
# 5. 请提供大气、声环境监测数据和预测结果，包括项目施工期和运营期的环境影响预测。
# 6. 请提供大气、声环境治理和保护措施的技术可行性和经济成本。
# 7. 请提供大气、声环境治理和保护措施的实施效果监测数据。
# 8. 请提供大气、声环境治理和保护措施的实施效果评估方法和技术路线。
# 9. 请提供大气、声环境治理和保护措施的实施效果监测数据和评估结果。
# 10. 请提供大气、声环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估。

# A：
# 1. 武汉市的地理、气象和大气环境现状数据是什么？
# 2. 《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的环境影响预测评估方法和技术路线是什么？
# 3. 大气、声环境的质量标准和评价方法是怎样的？
# 4. 可以提供大气、声环境监测数据和预测结果吗？特别是项目施工期和运营期的环境影响预测。
# 5. 大气、声环境治理和保护措施的技术可行性和经济成本如何？
# 6. 有关大气、声环境治理和保护措施的实施效果监测数据是什么？
# 7. 大气、声环境治理和保护措施的实施效果评估方法和技术路线是怎样的？
# 8. 大气、声环境治理和保护措施的实施效果监测数据和评估结果呢？
# 9. 大气、声环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估如何？

# Q:"""