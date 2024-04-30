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
        print("Agent[Writer] loeaded successfully")
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
    

class Investigator:
    def __init__(self, llm):
        self.llm = llm
        print("Agent[Investigator] loeaded successfully")
        
    
    def get_ques_list(self, title, heading):
        prompt = """
# role
你是一名信息搜集专员，为写作者搜集写作所需要的信息。
# requirements
1.信息越具体越好，例如：
    不具体的信息：项目所在地周边的大气排放情况
    具体的信息：某某市周边的大气排放情况

Q：请分析为了写作《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的`大气、声环境环境保护目标`章节的内容，需要获取哪些信息？
A：
1. 武汉市的地理、气象和大气环境现状数据是什么？
2. 《武汉市铁水集运煤炭码头一期工程环境影响评价报告书》的环境影响预测评估方法和技术路线是什么？
3. 大气、声环境的质量标准和评价方法是怎样的？
4. 可以提供大气、声环境监测数据和预测结果吗？特别是项目施工期和运营期的环境影响预测。
5. 大气、声环境治理和保护措施的技术可行性和经济成本如何？
6. 有关大气、声环境治理和保护措施的实施效果监测数据是什么？
7. 大气、声环境治理和保护措施的实施效果评估方法和技术路线是怎样的？
8. 大气、声环境治理和保护措施的实施效果监测数据和评估结果呢？
9. 大气、声环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估如何？

Q：请分析为了写作《{title}》的`{heading}`章节的内容，需要获取哪些信息？
A：""".format(title=title, heading=heading)
        response:str = self.llm(prompt)
        
        import re
        pattern = r'\d+\.\s*(.*?\？)'   # 带 ？

        # Extracting questions using findall method
        ques_list = re.findall(pattern, response)
        return ques_list




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
    pass

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