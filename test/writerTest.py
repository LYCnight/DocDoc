from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
cur_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(cur_path)) 

# import logging
# 配置日志记录器，使用 'w' 模式以重写文件
# logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
heading = "项目由来"
retrieved_knowledge = """
问：岳阳县位于哪里？
答：岳阳县位于湖南省北部、东洞庭湖东岸。

问：岳阳县的河流情况如何？
答：岳阳县河流密布，水系发达，共有主要河流14条，大部分流入新墙河。

问：新墙河在岳阳县的地位如何？
答：新墙河是岳阳县的母亲河，哺育人口众多，对岳阳县的政治、经济、文化具有重要影响。

问：麻塘片区在岳阳县中扮演什么角色？
答：麻塘片区是岳阳县的北大门，地理位置优越，水资源丰富，对岳阳县的形象具有重要意义。

问：麻塘片区和新墙河目前存在哪些问题？
答：麻塘片区存在水系连通性差、水体黑臭、生态环境差的问题。新墙河存在河道淤积严重、垃圾成堆、滨岸带植被破坏严重、部分地区岸坡严重坍塌、部分地区道路不畅的问题。

问：岳阳县水系连通及农村水系综合整治工程的措施有哪些？
答：整治措施包括水系连通、河道清障、清淤疏浚、岸坡整治、水源涵养与水土保持、河湖管护。

问：整治工程的范围是怎样的？
答：整治范围以岳阳市南湖新区为起点，麻塘片区为纽带，连接岳阳县城区，向上辐射新墙镇、新开镇、公田镇至铁山水库风景区。

问：麻塘片区水系连通工程的目的是什么？
答：目的是通过水系连通、水资源调配及渠道清淤提高水体自净能力，改善水质。

问：整治工程的目标是什么？
答：目标是改善农村河道生态环境，创造良好的水环境，推进城乡一体化。

问：为什么本项目需要编制环境影响报告书？
答：根据《中华人民共和国环境影响评价法》和《建设项目环境保护管理条例》，本项目属于涉及环境敏感区的河湖整治，需编制环境影响报告书。

问：工程内容主要包括哪些？
答：工程内容包括麻塘片区水系连通工程，改扩建水源工程、连通沟渠、整治湖泊；新墙河综合整治，清除杂草、清理河道垃圾、清淤疏浚、护岸工程、滨岸带整治、生态恢复、防汛路面改造、堤防险工险段治理、湖塘清淤加固等。
"""

# logging.info("----------------------------- prompt: write_with_dep -------------------------------")
# logging.info("title:")
# logging.info(title)
# logging.info("heading:")
# logging.info(heading)
# logging.info("retrieved_knowledge:")
# logging.info(retrieved_knowledge)

print("----------------------------- prompt: write_with_dep -------------------------------")
prompt = WRITE_WITHOUT_DEP.format(title=title, heading=heading, retrieved_knowledge=retrieved_knowledge)
print(prompt)

# 加载 LLM 模型
from config import MODEL_PATH, TOKENIZER_PATH
from LLMs import ChatGLM
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

# 加载 Agent[Writer]
from core.prompt import WRITE_WITHOUT_DEP, WRITE_WITH_DEP, WRITE_MUTATION
from core.Agent import Writer
writer = Writer(llm)

# 测试 wirte_without_dep
print(" ------------------------------ wirte_without_dep <start> -----------------------------------")
response = writer.write_without_dep(title, heading, retrieved_knowledge)
print(response)
print(" ------------------------------ wirte_without_dep <end> -----------------------------------")


title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
heading = "项目环评报告书的主要结论"
retrieved_knowledge = ""
dep_text = """
岳阳县水系连通及农村水系综合整治工程建设项目工程的实施可以改善项目区水体的水动力条件和区域水体自净能力，带动周边旅游业发展，提升城市品质、改善人居环境，对促进地区社会经济发展具有重要作用。项目的建设符合国家产业政策和相关法律法规。在落实本次环评及生态专题报告提出的污染防治措施、环境保护措施与环境风险防范措施、妥善协调好工程建设与湖南东洞庭湖国家级自然保护区与湖南新墙河国家湿地公园关系的前提下，从环境保护角度分析，本项目建设是可行的。
"""

print("----------------------------- prompt: write_with_dep -------------------------------")
prompt = WRITE_WITH_DEP.format(title=title, heading=heading, dep_text = dep_text, retrieved_knowledge=retrieved_knowledge)
print(prompt)
# 测试 wirte_without_dep
print(" ------------------------------ wirte_with_dep <start> -----------------------------------")
response = writer.write_with_dep(title, heading, dep_text, retrieved_knowledge)
print(response)
print(" ------------------------------ wirte_with_dep <end> -----------------------------------")


title = "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书"
heading = "6.2环境影响经济损益分析"
retrieved_knowledge = ""
dep_text = """
6.2.1环境影响经济损失
环境影响经济损失包括为减免不利环境影响而采取的环境保护投资、土地资源损失、周围环境以及人群健康损失。
6.2.1.1环境保护投资
本次为减免、恢复或补偿不利环境影响所采取的环境保护措施主要包括以下内容：施工生产废水及生活污水处理、大气污染控制措施、固体废物处置、噪声控制措施；施工期环境监测及环境管理；生态保护措施；鱼类资源保护以及人群健康保护等。工程环境保护措施总投资约280万元。
6.2.1.2土地资源损失
本工程永久占地总面积为29.91亩。工程临时占地1660.68亩。项目建设以河道工程为主，工程利用部分现有河道，因此工程占地中水利设施用地面积比重较大。另由于附属设施的建设，将占用河道两岸部分水田及旱地等。
6.2.1.3周边环境及人群健康损失
由于工程施工期较长，施工量大，施工期施工区人员高度集中，在工程建设过程中所产生的废水、废气、废渣将对局部环境产生不利影响，工程施工过程中建设物资的运输也会增加局部地区的环境污染。
6.2.2环境影响经济效益
本工程的效益主要为直接效益和间接效益，直接效益为防洪效益，间接效益为改善水环境、提升旅游品质等。
6.2.2.1直接效益
根据岳阳县新闻网报告，岳阳县2020年汛期灾情造成的直接经济损失共计25339万元，其中农业损失20656万元，基础设施损失4111万元，家庭财产损失552万元，公益性经济损失20万元。本工程实施后，多年平均减少洪灾损失为2500万元。
6.2.2.2间接效益
（1）增强生态系统功能，创造生态美好环境
工程的实施，对防止水土流失、增加绿化面积和水面面积，涵养水份，起到了相当大的作用。通过绿化及美化设计，可成为市区的一道亮丽的风景线。同时，生态系统功能增强，区域抗御自然灾害的能力提高，单位面积生物量也将会大幅度提高，生态环境将明显改善。通过项目的建设，流域林草覆盖度将大大提高，当地野生动物将得以繁衍和发展，有利形成人、动植物与自然协调发展并和谐相处的美好环境。
（2）缓解人地矛盾，促进经济发展
通过本项目的建设，将进一步改善人居环境和生态环境，树立良好的城市形象。项目的建设对提升城市的综合竞争能力将起到一定的促进作用，项目建设将带动周边区域的开发，提升周边土地的使用价值，带动相关产业的发展，对加快城市化进程、促进岳阳县地区经济发展将起到一定的推动作用。
"""

print("----------------------------- prompt: write_mutation -------------------------------")
prompt = WRITE_MUTATION.format(title=title, heading=heading, dep_text = dep_text, retrieved_knowledge=retrieved_knowledge)
print(prompt)
# 测试 wirte_without_dep
print(" ------------------------------ wirte_mutation <start> -----------------------------------")
response = writer.write_mutation(title, heading, dep_text, retrieved_knowledge)
print(response)
print(" ------------------------------ wirte_mutation <end> -----------------------------------")





