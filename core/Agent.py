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
    
    path_to_directory = str(root_path) + "/UserUploadFiles"
    
    def __init__(self, llm):
        from llama_index.core import SimpleDirectoryReader
        from core.RAG import SentenceWindowRetrieverPack        
        reader = SimpleDirectoryReader(input_dir = self.path_to_directory, recursive = True) 
        documents = reader.load_data()
        retriever = SentenceWindowRetrieverPack(llm, documents)
        query_engine = retriever.query_engine
        
        self.llm = llm
        self.query_engine = query_engine
        self.retriever = retriever  
        print("Agent[Investigator] loeaded successfully")
    
    def get_retrieved_knowledge(self, title, heading) -> str:
        ques_list = self.get_ques_list(title, heading)
        print(ques_list)
        ans_list = self.get_ans_list(ques_list)
        print(ans_list)
        retrieved_knowledge:str = self.QA_assemble(ques_list=ques_list, ans_list=ans_list)
        print("done")
        return retrieved_knowledge
        
    def get_relevant_answer(self, ques:str) -> str:
        relevant_context_list:list[str] = self.get_relevant_context_list(ques)
        relevant_contexts:str = ""
        for text in relevant_context_list:
            relevant_contexts += f"{text}\n"
            relevant_contexts += f"---\n"
        
        prompt = f"""
# role
你是一名环境专家
# task
请结合你的环境知识，根据`relevant_contexts`，回答问题。
# relevant
{relevant_contexts}

*********
Q:{ques}
A:""".format(relevant_contexts=relevant_contexts, ques=ques)
        
        answer:str = self.llm(prompt)
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
        print(response)
        
        import re
        pattern = r'\d+\.\s*(.*?)(?:[？?;；])'

        # Extracting questions using findall method
        ques_list:list[str] = re.findall(pattern, response)
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