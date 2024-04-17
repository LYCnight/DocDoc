from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 

import json
from core.prompt import REVIEW_PROMPT, REVIEW_PROMPT_CONSTRAINTS

def review(review_prompt:str, llm, debug:bool = False) -> tuple:
    review_str = llm(review_prompt)
    if(debug == True):
        print(review_str)
    review_json = json.loads(review_str)
    thinking_process = review_json["thinking_process"]
    conclusion = review_json["conclusion"]
    is_qualified:bool = review_json["is_qualified"]
    comment = review_json["comment"]
    return thinking_process, conclusion, is_qualified, comment

if __name__ == "__main__":
    text = """（1）国家级自然保护区     
项目部分工程位于东洞庭湖国家级自然保护区的实验区内，对东洞庭湖国家级自然保护区可能产生的影响进行预测是本次评价的重点。
（2）国家重要湿地生态系统
本项目工程位于新墙河国家湿地公园恢复重建区和科普宣教利用区内，对新墙河国家湿地公园生态系统可能产生的影响进行预测是本次评价的重点。
（3）陆生生态环境 
工程施工对陆生生态环境的影响表现在工程占地对土地资源的影响，施工活动对土壤和植被、野生动物的影响。
本工程永久占地总面积为29.91亩。工程临时占地1660.68亩。施工活动对土壤环境最直接的影响就是施工期各类施工机械的碾压和建筑物占压对土壤结构、肥力、物理性质的破坏。工程永久建筑物以及永久道路修建区的地表土壤在施工过程中彻底被占压覆盖，土壤性质永久改变不可恢复。施工临建设施占压及施工活动扰动区表层土壤结构、肥力、物理性质将被临时性破坏，需要较长时间才可恢复，若施工结束后配合恢复措施，则这一过程将被缩短。对地表植被而言，与土壤相同，工程永久占地将对原地表植被造成一次性永久破坏；施工临建设施占压和施工活动扰动区域等临时占地在施工结束后，通过采取一定的整治恢复措施，地表植被可以逐步得到恢复。
工程施工对野生动物的影响表现为：工程施工活动可能干扰工程区内野生动物的正常栖息觅食，施工噪声会对其产生惊扰。工程永久占地、临时占地为绿化、耕地、渔塘等。施工活动对施工区域陆生植物的影响较小。受影响植物基本为地区常见种类，工程建设不会对区域植物物种构成和区系组成造成显著不利影响。工程范围内没有国家重点保护的珍稀濒危植物，不存在工程对珍稀濒危植物的影响问题。
（4）水生生态环境 
工程施工会对一些鱼类的种群结构、活动和繁殖以及水禽的栖息有一定影响，但施工对水域环境的影响是短期的和有限的。施工结束后，水中悬浮物会恢复到施工前水平，各种生物亦会重新适应水域环境的变化。本工程对水生生物的影响很小。"""
    
    review_prompt = REVIEW_PROMPT.format(text=text) + "\n" + REVIEW_PROMPT_CONSTRAINTS

    print(review_prompt)

    from LLMs import init_llm_and_embedding
    llm, embedding = init_llm_and_embedding()
    thinking_process, conclusion, is_qualified, comment = review(review_prompt, llm, debug=True)
    print("thinking_process: ", thinking_process)
    print("conclusion: ", conclusion)
    print("is_qualified: ", is_qualified)
    print("comment: ", comment)