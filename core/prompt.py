from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc2/
core_path = Path(__file__).parent    # 当前目录    DocDoc2/core
sys.path.append(str(core_path))
sys.path.append(str(root_path))

from AI.PromptUtil import PromptTemplate

GEN_CONTENT_COMPLETE_COPY = \
"""## role
******
Q: 帮我撰写《岳阳铁水集运煤炭码头一期工程环境影响报告书》的`环境现状调查与评价`章节的目录。要求：None
A:
id:0, heading:环境现状调查与评价, dep:-1, level=1
id:1, heading:自然环境概况, dep:-1, level=2
id:2, heading:地理位置, dep:-1, level=3
id:3, heading:地质、地貌, dep:-1, level=3
id:4, heading:气象气候, dep:-1, level=3
id:5, heading:水文特征, dep:-1, level=3
id:6, heading:土壤, dep:-1, level=3
id:7, heading:植被、生物多样性, dep:-1, level=3
id:8, heading:项目区生态保护区调查, dep:-1, level=2
id:9, heading:湖南东洞庭湖国家级自然保护区, dep:-1, level=3
id:10, heading:岳阳市东洞庭湖江豚市级自然保护区, dep:-1, level=3
id:11, heading:湖南新墙河国家湿地公园, dep:-1, level=3
id:12, heading:东洞庭湖鲤鲫黄颡国家级水产种质资源保护区, dep:-1, level=3
id:13, heading:环境质量现状调查与评价, dep:-1, level=2
id:14, heading:地表水环境质量现状调查与评价, dep:-1, level=3
id:15, heading:水环境质量现状调查, dep:-1, level=4
id:16, heading:评价方法, dep:-1, level=4
id:17, heading:水环境质量现状监测结果及评价, dep:-1, level=4
id:18, heading:环境空气现状调查与评价, dep:-1, level=3
id:19, heading:地下水环境现状调查与评价, dep:-1, level=3
id:20, heading:声环境现状调查与评价, dep:-1, level=3
id:21, heading:底泥环境质量现状与评价, dep:-1, level=3
id:22, heading:生态环境环境质量现状调查与评价, dep:-1, level=3
id:23, heading:调查范围, dep:-1, level=4
id:24, heading:调查方法, dep:-1, level=4
id:25, heading:生态系统现状调查, dep:-1, level=4
id:26, heading:植被及植物多样性调查, dep:-1, level=4
id:27, heading:动物多样性现状调查, dep:-1, level=4
id:28, heading:水生生物调查, dep:-1, level=4
id:29, heading:主要生态问题调查, dep:-1, level=4
id:30, heading:水土流失现状, dep:-1, level=4
id:31, heading:防洪排涝现状, dep:-1, level=2
id:32, heading:区域防洪工程现状, dep:-1, level=3
id:33, heading:区域排涝设施现状, dep:-1, level=3
id:34, heading:区域水资源开发利用现状, dep:-1, level=2
id:35, heading:区域污染源调查, dep:-1, level=2
<end>

Q: 帮我撰写《华能岳阳电厂码头2#泊位提质改造工程环境影响报告书》的`总则`章节的目录。要求：None
A:
id:0, heading:总则, dep:-1, level=1
id:1, heading:编制依据, dep:-1, level=2
id:2, heading:国家法律、法规和政策, dep:-1, level=3
id:3, heading:地方法规、规划, dep:-1, level=3
id:4, heading:技术标准及行业规范, dep:-1, level=3
id:5, heading:其它技术规范及参考依据, dep:-1, level=3
id:6, heading:评价目的及工作原则, dep:-1, level=2
id:7, heading:评价目的, dep:-1, level=3
id:8, heading:评价工作原则, dep:-1, level=3
id:9, heading:评价标准, dep:-1, level=2
id:10, heading:环境功能区划, dep:-1, level=3
id:11, heading:地表水环境功能区, dep:-1, level=4
id:12, heading:地下水环境功能区, dep:-1, level=4
id:13, heading:环境空气功能区, dep:-1, level=4
id:14, heading:声环境功能区, dep:-1, level=4
id:15, heading:土壤环境功能区, dep:-1, level=4
id:16, heading:建设项目所在区域环境, dep:-1, level=4
id:17, heading:环境质量标准, dep:-1, level=3
id:18, heading:污染物排放标准, dep:-1, level=3
id:19, heading:水污染物排放标准, dep:-1, level=4
id:20, heading:大气污染物排放标准, dep:-1, level=4
id:21, heading:噪声排放标准, dep:-1, level=4
id:22, heading:固体废物, dep:-1, level=4
id:23, heading:环境影响因素识别和评价因子筛选, dep:-1, level=2
id:24, heading:环境影响因素识别, dep:-1, level=3
id:25, heading:评价因子, dep:-1, level=3
id:26, heading:评价工作等级及评价范围, dep:-1, level=2
id:27, heading:地表水环境, dep:-1, level=3
id:28, heading:大气环境, dep:-1, level=3
id:29, heading:地下水环境, dep:-1, level=3
id:30, heading:声环境, dep:-1, level=3
id:31, heading:生态环境, dep:-1, level=3
id:32, heading:环境风险, dep:-1, level=3
id:33, heading:土壤环境, dep:-1, level=3
id:34, heading:小结, dep:-1, level=3
id:35, heading:环境敏感目标, dep:-1, level=2
id:36, heading:生态环境保护目标, dep:-1, level=3
id:37, heading:水环境保护目标, dep:-1, level=3
id:38, heading:大气、声环境环境保护目标, dep:-1, level=3
id:39, heading:评价重点, dep:-1, level=2
<end>

Q: 帮我撰写《华能岳阳电厂码头2#泊位提质改造工程环境影响报告书》的`项目概况及工程分析`章节的目录。要求：None
A:
id:0, heading:项目概况及工程分析, dep:-1, level=1
id:1, heading:项目区概况及存在的问题, dep:-1, level=2
id:2, heading:概况, dep:-1, level=3
id:3, heading:存在的问题, dep:-1, level=3
id:4, heading:项目基本情况, dep:-1, level=2
id:5, heading:项目名称及建设性质, dep:-1, level=3
id:6, heading:工程任务及规模, dep:-1, level=3
id:7, heading:工程设计, dep:-1, level=2
id:8, heading:工程等别及洪水标准, dep:-1, level=3
id:9, heading:整体布局与分区, dep:-1, level=3
id:10, heading:水系连通工程, dep:-1, level=3
id:11, heading:水源工程, dep:-1, level=4
id:12, heading:连通渠道工程, dep:-1, level=4
id:13, heading:整治湖泊工程, dep:-1, level=4
id:14, heading:水系连通工程量汇总, dep:-1, level=4
id:15, heading:河道清障工程, dep:-1, level=3
id:16, heading:清淤疏浚工程, dep:-1, level=3
id:17, heading:岸坡整治工程, dep:-1, level=3
id:18, heading:护岸工程, dep:-1, level=4
id:19, heading:滨岸带治理工程, dep:-1, level=4
id:20, heading:堤防险T险段治理, dep:-1, level=3
id:21, heading:附属工程, dep:-1, level=3
id:22, heading:水源涵养, dep:-1, level=3
id:23, heading:工程施工, dep:-1, level=2
id:24, heading:麻塘垸, dep:-1, level=3
id:25, heading:料场, dep:-1, level=4
id:26, heading:施工导流, dep:-1, level=4
id:27, heading:施工交通运输, dep:-1, level=4
id:28, heading:水、电供应及通讯, dep:-1, level=4
id:29, heading:施工办公生活区, dep:-1, level=4
id:30, heading:弃渣, dep:-1, level=4
id:31, heading:施工进度安排, dep:-1, level=4
id:32, heading:施工技术供应, dep:-1, level=4
id:33, heading:新墙河片区, dep:-1, level=3
id:34, heading:料场, dep:-1, level=4
id:35, heading:施工导流, dep:-1, level=4
id:36, heading:施工交通运输, dep:-1, level=4
id:37, heading:水、电供应及通讯, dep:-1, level=4
id:38, heading:施工办公生活区, dep:-1, level=4
id:39, heading:弃渣, dep:-1, level=4
id:40, heading:施工进度安排, dep:-1, level=4
id:41, heading:施工技术供应, dep:-1, level=4
id:42, heading:工程占地处理及移民安置, dep:-1, level=2
id:43, heading:工程占地, dep:-1, level=3
id:44, heading:移民安置, dep:-1, level=3
id:45, heading:征地补偿, dep:-1, level=3
id:46, heading:土石方平衡, dep:-1, level=2
id:47, heading:工程方案合理性分析, dep:-1, level=2
id:48, heading:工程设计方案合理性分析, dep:-1, level=3
id:49, heading:施工布置环境合理性分析, dep:-1, level=3
id:50, heading:工程分析, dep:-1, level=2
id:51, heading:工艺流程分析, dep:-1, level=3
id:52, heading:主体工程施工简介, dep:-1, level=4
id:53, heading:工程影响因素分析, dep:-1, level=4
id:54, heading:施工期污染源强分析, dep:-1, level=3
id:55, heading:废气污染源分析, dep:-1, level=4
id:56, heading:废水污染源分析, dep:-1, level=4
id:57, heading:噪声污染源分析, dep:-1, level=4
id:58, heading:固体废物污染源分析, dep:-1, level=4
id:59, heading:营运期污染源强分析, dep:-1, level=3
id:60, heading:生态环境影响, dep:-1, level=3
id:61, heading:水土流失, dep:-1, level=3"""

GEN_CONTENT_FOR_ONE_HEADING = \
"""## role
你是一名环境报告目录专家，擅长根据报告的标题和用户的要求写出优秀的环境报告的目录。
## specification
 - id: heading编号
 - heading：heading标题
 - dep：列表，其中包括写作本节内容所需要参考的其他heading的id。若不需要参考，则设置为-1；若需要参考，并且由多个参考id，则用英文逗号","分隔
 - level: 标题等级，文章title的level为0，其余heading的level从1开始
## format:
id:?, heading:?, dep:?, level=?
## requirement
 - level 从1开始，最大为4
 - 请在目录结尾处加上 <end>
## constraint
 - dep请设置为 -1
 - 请严格按照specification 和 format 输出目录，不要输出其他无关内容
******
Q: 帮我撰写《湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书》的`概述`章节的目录。要求：None
A:
id:0, heading:概述, dep:[-1], level:1
id:1, heading:项目由来, dep:[-1], level:2
id:2, heading:环境影响评价的工作过程, dep:[-1], level:2
id:3, heading:分析判定相关环保政策, dep:[-1], level:2
id:4, heading:产业政策相符性分析, dep:[-1], level:3
id:5, heading:法律法规符合性分析, dep:[-1], level:3
id:6, heading:与相关规划符合性分析, dep:[-1], level:3
id:7, heading:与“三线一单"相符性分析, dep:[-1], level:3
id:8, heading:关注的主要环境问题, dep:[-1], level:2
id:9, heading:项目环评报告书的主要结论, dep:[-1], level:2
<end>

Q: 帮我撰写《岳阳铁水集运煤炭码头一期工程环境影响报告书》的`结论与建议`章节的目录。要求：None
A:
id:0, heading:结论与建议, dep:[-1], level:1
id:1, heading:项目概况, dep:[-1], level:2
id:2, heading:环境质量现状评价结论, dep:[-1], level:2
id:3, heading:地表水水质现状, dep:[-1], level:3
id:4, heading:环境空气质量现状, dep:[-1], level:3
id:5, heading:声环境质量现状, dep:[-1], level:3
id:6, heading:地下水环境质量现状, dep:[-1], level:3
id:7, heading:底泥环境质量现状, dep:[-1], level:3
id:8, heading:生态环境现状结论, dep:[-1], level:3
id:9, heading:环境影响评价结论, dep:[-1], level:2
id:10, heading:水环境影响评价结论, dep:[-1], level:3
id:11, heading:大气环境影响评价结论, dep:[-1], level:3
id:12, heading:声环境影响评价结论, dep:[-1], level:3
id:13, heading:固体废物影响评价结论, dep:[-1], level:3
id:14, heading:生态环境影响评价结论, dep:[-1], level:3
id:15, heading:主要环保措施, dep:[-1], level:2
id:16, heading:废水, dep:[-1], level:3
id:17, heading:废气, dep:[-1], level:3
id:18, heading:噪声, dep:[-1], level:3
id:19, heading:固体废物, dep:[-1], level:3
id:20, heading:生态保护措施, dep:[-1], level:3
id:21, heading:人群健康保护措施, dep:[-1], level:3
id:22, heading:环境影响经济损益分析, dep:[-1], level:2
id:23, heading:环评总结论, dep:[-1], level:2
id:24, heading:建议, dep:[-1], level:2
<end>

Q: 帮我撰写《{title}》的`{heading}`章节的目录。要求：{requirement}
A:"""

GEN_CONTENT_PRELIMINARY = \
""" ## role
你是一名环境报告目录专家，擅长根据报告的标题和用户的要求写出优秀的环境报告的目录。
## specification
 - id: heading编号
 - heading：heading标题
 - dep：列表。其中包含写作本节内容所需要参考的其他heading的id。若不需要参考，则设置为-1；若需要参考，并且由多个参考id，则用英文逗号","分隔
 - level: 标题等级，文章title的level为0，其余heading的level从1开始
## constraint
 - dep请设置为 -1
******
Q: 帮我撰写《湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书》的目录。要求：None
A: 
id:0, heading:湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书, dep:[-1], level:0
id:1, heading:概述, dep:[-1], level:1
id:2, heading:总则, dep:[-1], level:1
id:3, heading:建设项目工程分析, dep:[-1], level:1
id:4, heading:环境现状调查与评价, dep:[-1], level:1
id:5, heading:环境影响预测与评价, dep:[-1], level:1
id:6, heading:环境保护措施, dep:[-1], level:1
id:7, heading:环境风险分析, dep:[-1], level:1
id:8, heading:环境管理与环境监测, dep:[-1], level:1
id:9, heading:环境保护投资与环境影响经济损益分析, dep:[-1], level:1
id:10, heading:环境影响评价结论, dep:[-1], level:1


Q: 帮我撰写《华能岳阳电厂码头2#泊位提质改造工程环境影响报告书》的目录。要求：None
A:
id:0, heading:华能岳阳电厂码头2#泊位提质改造工程环境影响报告书, dep:[-1], level:0
id:1, heading:概述, dep:[-1], level:1
id:2, heading:总则, dep:[-1], level:1
id:3, heading:工程概况及工程环境影响分析, dep:[-1], level:1
id:4, heading:环境质量现状调查与评价, dep:[-1], level:1
id:5, heading:环境可行性分析, dep:[-1], level:1
id:6, heading:环境影响预测与评价, dep:[-1], level:1
id:7, heading:水产种质资源保护区环境影响评价及保护措施, dep:[-1], level:1
id:8, heading:环境影响减缓措施及技术经济论证, dep:[-1], level:1
id:9, heading:环境经济损益分析, dep:[-1], level:1
id:10, heading:环境保护管理及监测计划, dep:[-1], level:1
id:11, heading:评价结论与建议, dep:[-1], level:1

Q: 帮我撰写《岳阳铁水集运煤炭码头一期工程环境影响报告书》的目录。要求：None
A:
id:0, heading:岳阳铁水集运煤炭码头一期工程环境影响报告书, dep:[-1], level:0
id:1, heading:概述, dep:[-1], level:1
id:2, heading:总则, dep:[-1], level:1
id:3, heading:工程概况与工程分析, dep:[-1], level:1
id:4, heading:环境现状调查与评价, dep:[-1], level:1
id:5, heading:环境可行性分析, dep:[-1], level:1
id:6, heading:环境影响预测与评价, dep:[-1], level:1
id:7, heading:水产种质资源保护区影响评价及保护措施, dep:[-1], level:1
id:8, heading:环境保护措施及其可行性论证, dep:[-1], level:1
id:9, heading:环境影响经济损益分析, dep:[-1], level:1
id:10, heading:环境管理与监测计划, dep:[-1], level:1
id:11, heading:环境影响评价结论, dep:[-1], level:1

Q: 帮我撰写《{title}》的目录。要求：{requirement}
A:"""


WRITE_DIGEST = """
<role>
你是一名写作专家, 正在写作<{title}>
digest 是你迄今为止所写的内容的摘要。
text 是目录项'{heading}'的正文。
</role>
<rule>
digest 为目录项(0~i)的内容摘要。
text 是 第(i+1)个目录项的的正文。
digest 为目录项(0~i)的内容摘要。
text 是 第(i+1)个目录项的的正文。
请你总结text(i+1)的重点信息，并融入到digest(0~i)中，形成新的digest(0~i+1)。在此过程中，应避免直接复制前面的内容，而是通过重新组织来提炼信息，确保摘要的最终长度相对稳定，且随着添加的内容逐渐丰富。
</rule>
<content>
{content}
</content>
<text>
{text}
</text>
<digest>
{digest}
</digest>
<task>
Q: 请你根据digest和text，更新digest。请直接输出digest的内容。
A: 
"""

WRITE_WITHOUT_DEP = '''
<role>
你是一名写作专家
</role>
<rule>
你正在写作<{title}>的目录项`{heading}`的正文内容。
constraints: 是必须遵守的约束条件
content: 是文章的目录
digest：是你迄今为止已写内容的概括
last_heading：是上一次所写的目录项的内容。你需要从中学习，并保持语言风格的一致性。
retrieved_knowledge: 是你通过查阅资料获得的参考信息
</rule>
<constraints>
1. 你只能返回markdoWn格式的文本
2. 你的返回的正文中不能含有 #, ##, ###, ####, #####, ###### 等markdown heading命令
</constraints>
<content>
{content}
</content>
<digest>
{digest}
</digest>
<last_heading>
{last_heading}
<last_heading/>
<retrieved_knowledge>
{retrieved_knowledge}
</retrieved_knowledge>
<attention>
请记住，你是一名写作专家，正在写作这一节的正文内容。
所以你需要观察last_heading的语言风格和写作特征，保证你写作风格的一致性，确保你的内容更像人类写作出来的而不是像AI的风格。
</attention>
<task>
Q: 请根据content, digest, last_heading, retrieved_knowledge, 生成目录项`{heading}`的正文内容。
A:
'''

WRITE_WITH_DEP = '''
<role>
你是一名写作专家
</role>
<rule>
你正在写作<{title}>的目录项`{heading}`的正文内容。
constraints: 是必须遵守的约束条件
content: 是文章的目录
digest：是你迄今为止已写内容的概括
last_heading：是上一次所写的目录项的内容。你需要从中学习，并保持语言风格的一致性。
retrieved_knowledge: 是你通过查阅资料获得的参考信息
dep_text: 是你已经完成的内容，你需要依赖这些内容来写作本节内容
</rule>
<constraints>
1. 你只能返回markdoWn格式的文本
2. 你的返回的正文中不能含有 #, ##, ###, ####, #####, ###### 等markdown heading命令
</constraints>
</rule>
<content>
{content}
</content>
<digest>
{digest}
</digest>
<last_heading>
{last_heading}
<last_heading/>
<retrieved_knowledge>
{retrieved_knowledge}
</retrieved_knowledge>
<dep_text>
{dep_text}
</dep_text>
<attention>
请记住，你是一名写作专家，正在写作这一节的正文内容。
所以你需要观察last_heading的语言风格和写作特征，保证你写作风格的一致性，确保你的内容更像人类写作出来的而不是像AI的风格。
</attention>
<task>
Q: 请根据content, digest, last_heading, dep_text, retrieved_knowledge, 生成目录项`{heading}`的正文内容。
A:
'''

WRITE_MUTATION = """
<role>
你是一名写作专家
</role>
<rule>
你正在写作<{title}>的目录项`{heading}`的正文内容。
constraints: 是必须遵守的约束条件
content: 是文章的目录
digest：是你迄今为止已写内容的概括
last_heading：是上一次所写的目录项的内容。你需要从中学习，并保持语言风格的一致性。
retrieved_knowledge: 是你通过查阅资料获得的参考信息
dep_text: 是你之前所写的内容，你需要总结这些内容，并生成这些内容的引导性文字
</rule>
<constraints>
1. 你只能返回markdoWn格式的文本
2. 你的返回的正文中不能含有 #, ##, ###, ####, #####, ###### 等markdown heading命令
</constraints>
</rule>
<content>
{content}
</content>
<digest>
{digest}
</digest>
<last_heading>
{last_heading}
<last_heading/>
<retrieved_knowledge>
{retrieved_knowledge}
</retrieved_knowledge>
<dep_text>
{dep_text}
</dep_text>
<attention>
请记住，你是一名写作专家，正在写作这一节的正文内容。
所以你需要观察last_heading的语言风格和写作特征，保证你写作风格的一致性，确保你的内容更像人类写作出来的而不是像AI的风格。
</attention>
<task>
Q: 请根据content, digest, last_heading, dep_text, retrieved_knowledge, 生成目录项`{heading}`的正文内容。
A:
"""

RETRIEVED_KNOWLEDGE = """
问：岳阳县位于哪里？
答：岳阳县位于湖南省北部、东洞庭湖东岸。

问：岳阳县的河流情况如何？
答：岳阳县河流密布，水系发达，共有主要河流14条，大部分流入新墙河。
"""

CONTENT_PROMPT = '''
你是一个目录生成专家，擅长于生成逻辑清晰，条理清楚的目录。
现在我需要写一份《{title}》，请你根据标题和我提供的信息，生成文章的详细目录。

信息：
{information}
'''



CONTENT_PROMPT_CONSTRAINTS = '''
注意：
你只能以JSON格式生成响应，就像下面这样（headline 表示标题，level表示标题等级，从1开始）
响应格式：
{
  "content" : [
        {"headline": "第一章", "level" : 1},
        {"headline": "1.1 回国", "level" : 2},
        {"headline": "第二章", "level" : 1}
              ]
}
请确保你的响应能被 Python json.loads 正确解析
'''




CONTENT_PROMPT_WITH_COMMENT = '''
你是一个目录生成专家，擅长于生成逻辑清晰，条理清楚的目录。
现在我需要写一份《{title}》，请你根据标题和我提供的信息，生成文章的详细目录。

信息：
{information}
------------------------
这是你过去输出的结果：
{result_last_time}
------------------------
一位文本审核员认为你撰写的目录还有提升空间，请你根据他的意见，修改你过去的结果以达到审核员的要求
意见：
{comment}
------------------------
'''



REVIEW_PROMPT = '''
你是一名文本内容质量审核员，负责审查文本质量，给出提升建议，并且给出结论：
1.审查通过，文本质量合格
2.审查不通过，文本质量不合格，要求写作者根据你给出的意见进行修改。

内容：
{text}
'''



REVIEW_PROMPT_CONSTRAINTS = """--------------------------CONSTRAINTS-------------------------------
请从以下角度评估文本质量：
1.前后逻辑通畅
2.内容详实不空洞
3.用词严谨
4.字数不能太少，每一段至少需要两句话。

要求：
1.在"thinking_process"中写下你每一步的思考过程。
3.根据你的思考过程，在"conclusion"中写下你对这段文本内容质量的评价结论，一定要客观。
3.根据你的思考过程和评价结论，如果你认为文本质量合格，则在 "is_qualified"中填写 `true`（bool值），否则填写 `false`(bool值)
4.如果"is_qualified"为`false`，则根据 "thinking process" 和 "conclusion"，在"comment"中为内容写作者提供越详细越好的修改建议。 
  如果"is_qualified"为`true`，则在 "comment" 中填写 "文本质量合格，无需修改"

注意：
你只能以JSON格式生成响应，就像下面这样：
响应格式：
{   
    "thinking_process":"your thinking process",
    "conclusion": "your conclusion",
    "is_qualified": true,
    "comment": "your comment"
}
请确保你的响应能被 Python json.loads 正确解析
"""




WRITER_INSTRUCTOR_PROMPT_ROLE = """
# role
你是一名环境报告段落写作指导专家，负责给写作专家分配写作任务。你会根据完整目录和相关信息，列出当前要写作的headline的`段落写作指导`，分配给写作专家填充正文的内容。
"""


WRITER_INSTRUCTOR_PROMPT_CONSTRAINT = """
# constraint
你只能以JSON格式生成响应，就像下面这样：
响应格式：
{   
    "paras_count" : "你认为需要写的段落的数量"
    "para_guide_list" : [
        {"para_guide" : "这一段的写作要求"},
        {"para_guide" : "这一段的写作要求"},
        {"para_guide" : "这一段的写作要求"}
    ] 
}
请确保你的响应能被 Python json.loads 正确解析
"""

WRITER_INSTRUCTOR_PROMPT_TITLE_AND_CONTENT = """
# title
《{title}》

# content
{content}
"""

WRITER_INSTRUCTOR_PROMPT_EXAMPLE = """
# example
---
## example.1 
Human:
帮我给出`4.4.1 施工期对地下水水质的影响分析`的写作任务
AI:
 {   
    "paras_count" : "1"
    "para_guide_list" : [
        {"para_guide" : "参考信息：【岳阳县水系连通及农村水系综合整治工程基坑经常性排水的悬浮物浓度约为2000mg/L左右，pH值为9～11；涵闸施工废水主要含有一定的SS，并伴有少量油污。本工程基坑排水拟在基坑中设若干串行集水坑，向集水坑中投加聚丙烯酰胺絮凝剂，让基坑废水静置沉淀2h后抽出外排；砂浆拌合机冲洗废水统一收集经沉淀处理后回用于生产，不外排；施工区的生活污水依托民房化粪池处理。】请根据参考信息，帮我写一份该项目施工期对地下水的影响分析。"}
    ] 
}

## example.2 
Human:
帮我给出`4.5.2 营运期固体废物对环境的影响分析`的写作任务
AI:
 {   
    "paras_count" : "1"
    "para_guide_list" : [
        {"para_guide" : "参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目在营运期共有管理人员6人】 请根据参考信息，帮我写一份运营期固体废物对环境的影响分析"}
    ] 
}

## example.3 
Human:
帮我给出`4.6.6 对东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区影响分析`的写作任务
AI:
 {   
    "paras_count" : "1"
    "para_guide_list" : [
        {"para_guide" : "参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目永久占地面积约29亩，评价区分布水禽主要包括雁鸭类和鸥类，分布涉禽主要包括鸻鹬类，鸣禽多以喜与人类混居的种类为主。】 请根据参考信息，请帮我写一份项目施工期对鸟类栖息地的影响分析"}
    ] 
}

## example.4 
Human:
帮我给出`4.4.2营运期对地下水的影响分析`的写作任务
AI:
 {   
    "paras_count" : "1"
    "para_guide_list" : [
        {"para_guide" : "参考信息：【岳阳县水系连通及农村水系综合整治工程的工程区地下水类型主要为第四系孔隙水和基岩裂隙水。第四系孔隙水赋存于第四系冲洪积砂砾石层中，由于砂砾石层含泥量较高，渗透性较低，含水层顶板上部为微弱透水的粉质粘土，渗透系数2.22×10-5cm/s～3.84×10-5cm/s，顶板埋深为 3.60～6.20m，相应的高程为 26.67～25.08m；含水层底板以下为泥质板岩，埋深 5.00～8.50m，相应的高程为 23.68～24.37m，局部具微承压性。该含水层与下部基岩裂隙水连通，并接收其补给。】
                        请根据参考信息帮我写一份该项目营运期对地下水的影响分析"}
    ] 
}
---
"""


WRITER_INSTRUCTOR_PROMPT_END = """
Human:
帮我给出 `{current_headline}`的写作任务
AI: 
"""




WRITE_PROMPT = """
# role
你是一名环境报告写作专家，能根据相关信息和要求撰写环境报告的文本。

# task
请你根据来撰写一段内容。

# example:
---
# example.1
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程的工程区地下水类型主要为第四系孔隙水和基岩裂隙水。第四系孔隙水赋存于第四系冲洪积砂砾石层中，由于砂砾石层含泥量较高，渗透性较低，含水层顶板上部为微弱透水的粉质粘土，渗透系数2.22×10-5cm/s～3.84×10-5cm/s，顶板埋深为 3.60～6.20m，相应的高程为 26.67～25.08m；含水层底板以下为泥质板岩，埋深 5.00～8.50m，相应的高程为 23.68～24.37m，局部具微承压性。该含水层与下部基岩裂隙水连通，并接收其补给。】
请根据参考信息帮我写一份该项目营运期对地下水的影响分析。
AI:
4.4.2营运期对地下水的影响分析
（1） 地下水类型
工程区地下水类型主要为第四系孔隙水和基岩裂隙水。第四系孔隙水赋存于第四系冲洪积砂砾石层中，由于砂砾石层含泥量较高，渗透性较低，含水层顶板上部为微弱透水的粉质粘土，渗透系数2.22×10-5cm/s～3.84×10-5cm/s，顶板埋深为 3.60～6.20m，相应的高程为 26.67～25.08m；含水层底板以下为泥质板岩，埋深 5.00～8.50m，相应的高程为 23.68～24.37m，局部具微承压性。该含水层与下部基岩裂隙水连通，并接收其补给，排泄条件差。
基岩裂隙水主要赋存于风化较强的基岩裂隙和受构造影响的长大裂隙中，裂隙水分布于基岩顶部强风化、中等风化带中，该类型地下水受基岩裂隙控制，分布不连续，含水量小，储水能力较弱。补给来源主要为地表水体和大气降水。岩层倾角较陡，水平向渗透性差，主要沿风化裂隙和构造裂隙形成地下径流向下游排泄，在适当的位置向地势低洼处排泄。
（2）工程对地下水水质的影响分析
本工程建设将增加区域水系连通性，运营期水质优于现状水体，可以有效提高项目区水体水质，稀释水中污染物的含量，结合本次水体整治工作，减弱了水体下渗补给对地下水的可能污染。工程建设对地下水补给和地下水水位的影响很小，周边地下水水位抬升较小，建设不会引起明显的水文地质问题，也不会对周边的植被、动物和农作物组成的生态系统产生明显的影响。
（3）工程对地下水水位变化及其对生态的影响分析
工程运行后，地下水水位有所抬升，区域主要为东洞庭湖湿地生态系统、新墙河湿地生态系统和农田生态系统，工程建设地下水抬升，有利于枯水期内湿地和农田地表水的补给，将改善区域湿地植被生产力水平，提高天然植被生产力水平，生态系统承载力提高，从而改善保护区野生动物生境。湿地保护区的植被恢复，一方面使天然植被覆盖度提高，为保护区的野生动物提供良好的天然庇护场所，另一方面有利于湿地保护区野生动物食物链的稳定和改善，对该区活动的野生动物生长繁殖具有良好的作用。
因此，本项目运营期对区域地下水环境有改善的作用。

# example.2
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目属于非污染源的治理项目】
请根据参考信息帮我写一份该项目运营期对生态环境影响分析
AI：
本项目工程本身属于非污染源的治理项目，运营期间主要生态环境影响是对水生生态环境的正面影响。工程实施后，可加快水体循环速度，增加区域水系连通性，提高了水体自净能力，有效改善水环境质量；护岸的建设可有效防止河水对岸坡的侵蚀，对于保护河流水质是有益的；排水渠内原有的腐殖质和有机物被清除，对水质起到明显的改善作用。
工程运营期间对周边湿地生态系统、农林生态系统、村镇生态系统植被及植物多样性、动物多样性基本无明显影响。

# example.3
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目施工占地区域两栖爬行动物及兽类均为湖南省常见种，包括中华大蟾蜍、泽陆蛙、赤链蛇、黑线姬鼠。】
请根据参考信息帮我写一份该项目施工期对其余陆生脊椎动物的影响分析
AI:
本项目对两栖爬行动物及兽类的影响类似，主要体现在生境的占用及生活生产废水弃渣等对周边生境的影响。具体影响如下：
1）施工占地的影响
本项目施工占地将直接导致施工区域生境被破坏及侵占。调查发现，施工占地区域两栖爬行动物及兽类均为湖南省常见种，包括中华大蟾蜍、泽陆蛙、赤链蛇、黑线姬鼠等，此类物种生境范围广泛，适应性强，当施工区域生境被侵占或破坏时，可迁移至周边适宜生境栖息。本项目周边生境与施工区域生境类似，均为农田、水塘等，因此，此类影响对此类动物的影响较小。
2）废气的影响
本项目施工时会产生施工扬尘、施工机械和运输车辆尾气等。本项目施工区域地势开阔，空气对流强，除施工区局部地区扬尘较重外，此类影响对两栖爬行动物及兽类的影响很小。
3）废水的影响
本项目施工时会产生一定的施工废水、基坑废水等，此类废水随意排放，将对周边水体水体水质、pH值等产生影响，进而对此类动物的繁殖以及水栖型两栖动物（黑斑侧褶蛙等）造成影响。从施工工艺上看，施工期产生的废水将经隔油、沉淀等处理后，用于施工用水或者施工道路洒水抑尘，杜绝废水未经任何处理直接排入周边水体。因此，此类影响经过相应处理后其程度较小。
4）噪声的影响
本项目施工时会产生一定的噪声及振动，将对施工区域的此类动物产生驱赶效应。由于施工区域周边适宜生境丰富，因此，此类影响对此类动物的影响很小。
5）固废的影响
本项目施工期会产生一定量生活垃圾、废弃土方。施工人员产生的生活垃圾经收集后由环卫部门及时清运至城市垃圾填埋场进行卫生填埋。本工程疏浚土拟用于两岸大堤内坡压浸。
施工期产生的固废通过弃土复耕复绿、生活垃圾统一集中处理等方式有效降低其对施工区周边环境的占用和破坏，因此，此类影响相对较小。

# example.3
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目涉及东洞庭湖自然保护区的实验区和湖南新墙河湿地公园，会导致部分地表裸露、水土流失，将可能造成土壤侵蚀。】
请帮我写一份该项目施工期对生态环境影响分析
AI:
1、生态系统类型及其特有程度
据调查，本项目水环境综合治理工程建设将影响评价区的生态系统类型：湿地生态系统、淡水生态系统、林地生态系统、农田生态系统。受影响的4种景观生态系统类型并非特有的植被类型，在保护区以及湖南乃至全国其它地区都有分布。所以，本项目水环境综合治理工程对保护区景观类型的影响程度为中低度影响。
2、对生态系统稳定性的影响
自然生态系统的恢复稳定性，可根据植被净生产力的多少度量。如果植被净生产力高，则其恢复稳定性强，反之则弱。工程建成运营后，植被慢慢恢复，因此，工程建设对区域自然体系的景观异质化程度和阻抗能力无明显影响。
3、对景观美学价值的影响
本工程涉及东洞庭湖自然保护区的实验区和湖南新墙河湿地公园，工程在一定程度上破坏了景观的美观和自然性，降低了观赏价值，非自然因素增加，使得水、林、田比例发生改变，这将削弱自然景观的美学内涵，以及增加自然保育成本，从而直接或间接的影响保护区的美学、经济和文化价值。但水体、景观工程局部提高了景观的观赏性，对美学、经济和文化价值具有一定的促进作用。
工程建设期间产生的固体废物、粉尘将影响自然景观的清洁性，使工程区景观的自然性和美学价值变低，但是这些影响随着临时用地的植被和景观的逐步恢复，这些临时影响将逐步消除。同时，工程建成后，将增加工程区内的湿地和观赏景观，其美学观赏价值较高。因此工程建设对评价区原有自然景观的美学价值将产生中低度影响。
4、导致评价区土壤侵蚀及地质灾害发生的可能性
拟建工程会导致部分地表裸露、水土流失，将可能造成土壤侵蚀。评价区地貌为平原，地势平坦，坡度小，发生地质灾害的可能较小。同时，在湖泊清淤、河渠清淤、河湖连通等工程建成后，将提升评价区的防洪能力，减小河湖水的淤 积、浸没、塌岸等地质灾害发生的可能性。总体来看，本工程建设对评价区土壤侵蚀及地质灾害的影响为中低度影响。
5、对自然植被覆盖的影响
生态系统服务功能的大小与天然植被面积有着正向的关联性。生态系统服务功能主要表现为提供保存生物进化所需要的丰富的物种与遗传资源，太阳能、二氧化碳的固定，有机质的合成，区域气候调节，维持水及营养物质的循环，土壤的形成与水土保持，污染物的吸收与降解及创造物种赖以生存与繁育的条件，维持整个大气化学组分的平衡与稳定，以及由于丰富的生物多样性所形成的自然景观及其具有的美学、文化、科学、教育的价值。湿地生态系统提供的最重要的4 类服务功能为娱乐游憩、防洪控水、缓冲风暴和改善水质。工程区自然景观类型以水域湿地为主，本项目为水环境综合整治和水系连通过程，对于整个自然保护区自然植被的影响较小，影响程度为中低度。

# example.4
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目工程位于东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区东面，最近距离约120m。且本工程在保护区内没有工程建设，无施工活动。】
请根据参考信息帮我写一份项目对东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区影响分析
AI:
本项目工程位于东洞庭湖鲤、鲫、黄颡国家级水产种质资源保护区东面，最近距离约120m。本工程在保护区内没有工程建设，无施工活动，对保护区基本无影响。
东洞庭湖鲤鲫黄颡国家级水产种质资源保护区主要保护对象为鲤、鲫、黄颡、鲶，这些鱼类为长江中游常见鱼类。本项目实施后工程运行基本不改变新墙河的水文情势。本项目麻塘垸水系连通工程的实施，可提高麻塘垸片区蓄滞能力，通过水系连通、水资源调配及渠道清淤，提高水体自净能力。新墙河片区通过河道清淤、岸坡整治工程、涵闸重建等措施，可有效增加新墙河河道过水能力，减少了地表水的滞留时间，并且增大了河道水环境容量。过水流量的增加提高了对排入新墙河水体的污水的混合稀释作用，加大了水体的自净能力。另一方面，河道疏浚清除了表层底泥，减少了內源污染物，有利于抑制河道內源污染物释放。故本项目对东洞庭湖水质有改善作用，对保护区内鱼类生境有利。

# example.5
Human:
参考信息：【岳阳县水系连通及农村水系综合整治工程建设项目产生的水土流失因子如下：
①降水因子：项目区多年平均降水1439.1mm，降水年际变化大，且年内分配不均，汛期（4~9 月）降雨量约占全年降雨量的70%左右，雨季（3月下旬~7 月上旬）降雨量占全年的45%左右，且降雨集中、暴雨频发、短时降雨强度大，加大了水力侵蚀。 
②土壤因子：工程区土壤主要以红壤为主，结构疏松、易于水解，抗蚀能力差，是水土流失潜在的自然因素。 
③植被因子：项目区场地在扰动破坏的情况下，原地表植被被破坏，地表形不成有效的保护层，使地表的抗蚀能力降低，产生严重的水土流失。 
④人为因子：对工程建设产生的土方、裸露地表在没有采取防护措施保护的情况下，就会产生大量的水土流失。】
请根据参考信息帮我写一份该项目工程建设对水土流失的影响因素分析
---

Human:
{para_guide}
AI:
"""



# WRITE_PROMPT_CONSTRAINTS = """--------------------------CONSTRAINTS-------------------------------
# 要求：
# 1.字数不能太少
# 2.如果有段落，请合理分段
# 3.如果有需要，你可以列点或者列表
# 4.前后逻辑通畅
# 5.内容详实不空洞
# 6.环境领域的用词需要严谨
# 7.不能胡编乱造没有的信息

# 注意：
# 1. 你只能以JSON格式生成响应，将当前写作的 headline 和 level 置于 "headline" 和 "level" 中，并将生成的文本的内容置于"text"中。
# 2. "text" 字段中的换行符应该写成 \\n
# 3. "text" 字段中的文本只能写在一行中

# 正确响应格式：
# {   
#     "content" : {"headline":"current headline", "level": "current headline's level"}
#     "text": "your text \\n is written here \\n and only has one line"
# }

# 请输出正确的 JSON 格式，确保你的响应能被 Python json.loads 正确解析
# """


FORMAT_CONTROLLER_PROMPT = """
# role
你是一名文本格式控制员，负责将零散的文本整理成一个完整的段落。

# task
将零散的不连贯的段落合并成一个连贯的段落。在整理过程中，文本的内容被重新组织和连接，以确保段落之间的逻辑流畅性和连贯性。这种重组和连接过程有助于使文本更易读、更容易理解，并确保信息传达的清晰性和准确性。

# example：
---
## example.1
整理前：
施工期的大多不利环境影响将随着施工期的结束而很快消失。
工程占地、提防工程中引起的陆域环境及水域环境的生态影响。
施工过程中建筑垃圾、清淤垃圾及施工人员的生活垃圾等固废影响。
施工机械及运输车辆的噪声。
开挖、河流疏浚时悬浮物的扩散影响，砂石生产系统废水，施工人员的生活污水等水环境影响。
施工扬尘、施工机械及运输车辆的燃油废气，底泥修复、清淤恶臭气体等大气环境影响。

整理后：
本项目的环境影响主要体现在施工期，施工期的环境影响主要是施工扬尘、施工机械及运输车辆的燃油废气，底泥修复、清淤恶臭气体等大气环境影响；开挖、河流疏浚时悬浮物的扩散影响，砂石生产系统废水，施工人员的生活污水等水环境影响；施工机械及运输车辆的噪声；施工过程中建筑垃圾、清淤垃圾及施工人员的生活垃圾等固废影响；工程占地、提防工程中引起的陆域环境及水域环境的生态影响。施工期的大多不利环境影响将随着施工期的结束而很快消失。

## example.2
整理前：
新墙河中存在阻水违章建筑和构筑物，主要包括乱堆的生活、建筑垃圾、违规采砂（现已停止）的尾堆、以及杂草等。
河道中的阻水废弃物和阻水杂草阻碍了水流，导致河道行洪排涝受阻，加速了河道淤积，并且恶化了水环境。
进行了针对河道内严重阻碍洪水通畅的阻水障碍物、废弃物以及阻水杂草的清理工作。

整理后：
新墙河阻水违章建、构筑物型式主要有：乱堆的生活、建筑垃圾、违规采砂（现已停止）的尾堆、杂草等。河道中的阻水废弃物及阻水杂草阻滞水流，严重影响河道行洪排涝，加速了河道淤积，加剧了水环境的恶化。此次对整治河道内碍洪严重的阻水障碍物、废弃物及阻水杂草进行清理。

## example.3
整理前：
本项目工程本身属于非污染源的治理项目，在运营期间主要生态环境影响是对水生生态环境的正面影响。
工程实施后，水体循环速度加快，区域水系连通性增加，水体自净能力提高，水环境质量得到有效改善。
护岸的建设有助于防止河水对岸坡的侵蚀，对保护河流水质起到积极作用。
排水渠内的腐殖质和有机物被清除，显著改善了水质。

整理后：
本项目工程本身属于非污染源的治理项目，运营期间主要生态环境影响是对水生生态环境的正面影响。工程实施后，可加快水体循环速度，增加区域水系连通性，提高了水体自净能力，有效改善水环境质量；护岸的建设可有效防止河水对岸坡的侵蚀，对于保护河流水质是有益的；排水渠内原有的腐殖质和有机物被清除，对水质起到明显的改善作用。

## example.4
整理前：
根据实际调查和查阅相关资料，项目区内未发现有珍稀动植物分布，现有动植物资源在保护区范围和周边区域较为常见。
项目建设期间，通过采取加强管理、严禁施工人员随意破坏植被、乱挖野生植物和猎杀野生动物等措施，可显著降低保护区重要遗传资料流失的可能性。

整理后：
根据实际调查和查阅相关资料，项目区内未发现有珍稀动植物分布，现有动植物资源在保护区范围和周边区域较为常见。项目建设期间，通过采取加强管理，严禁施工人员随意破坏植被、乱挖野生植物和猎杀野生动物等措施，可显著降低保护区重要遗传资料流失的可能性。

## example. 5
整理前：
施工期间对进入施工区的施工人员进行血吸虫病体检，筛检血吸虫病原携带者，血防体检主要采用免疫学方法。
检查时间为：每年在施工进场前和施工结束后各进行一次，共进行2次血防抽检，抽检人数按施工总人数的20%计算。
发现血吸虫病急性感染者和患有血吸虫病的人员应及时治疗，治疗费用按可能触水人员的3%预留，可能触水人员按施工人员的50%计算。

整理后：
对进入施工区的施工人员定期进行血吸虫病体检，筛检血吸虫病原携带者，血防体检主要采用免疫学方法。检查时间为：每年在施工进场前开展一次，施工结束再进行一次。施工期内一共进行2次血防抽检，人数按施工总人数的20%计。施工期间，若发现血吸虫病急性感染者和血吸虫病人应及时治疗，治疗费按可能触水人员的3%预留，可能触水人员按施工人员的50%考虑。
---

整理前：
{text_to_be_formatted}
整理后：
"""





content_template_short = '''

'''

AIContinue_template = '''
系统：你是一个专门续写文本的助手
"""
示例：
人类：我是一只小鸟
助手：我是一只小鸟，翱翔在蓝天。一天，我发现一片被破坏的森林，决定唤醒人们的环保意识。我的歌声成为呼唤，人们行动起来，保护了土地。现在，我在天空中飞翔，不仅享受自由，更肩负起守护地球的责任。我的故事成为了一个关于自然与人类共生的传奇。
"""
人类：'''

AIImprove_template = '''
系统：你是一个专门续写文本的助手
"""
人类：本项目采用了前后端方案，使用了java搭建后端，Vue搭建了前端
助手：
本研究项目在技术实施上充分考虑到前后端的一体性，以确保系统的整体性和协同性。具体而言，项目的后端架构采用了Java语言，通过其强大的生态系统和稳健性，为系统提供了可靠的后台支持。与此同时，前端方面充分利用了Vue框架的轻量级特性和灵活性，为用户界面的构建和交互提供了高效的解决方案。这一整合性的技术方案不仅在系统层面确保了协同工作的顺畅性，也为项目的可维护性和可扩展性奠定了坚实基础。
"""
人类：'''

content_template = '''
目录
1 项目背景
1.1 项目概况
1.2 绿色工地创建的必要性
2 编制依据
2.1 法律法规
2.2 规范标准
2.2.1 国家层面规范标准
2.2.2 地方层面规范标准
2.2.3 集团层面规范标准
2.3 项目相关文件
3 绿色工地组织管理
3.1 重视前期策划
3.2 加强制度体系建设
3.3 强化过程落实管控
3.4 绿色工地文化
4 “五节一环保”实施措施
4.1 环境保护
4.1.1 环境保护实施措施
4.1.2 环境保护措施清单
4.1.3 环境保护要素评价
4.2 节水与水资源利用
4.2.1 节水与水资源利用实施措施
4.2.2 节水与水资源利用措施清单
4.2.3 节水与水资源利用要素评价
4.3 节能与能源利用
4.3.1 节能与能源利用实施措施
4.3.2 节能与能源利用措施清单
4.3.3 节能与能源利用要素评价
4.4 节地与施工用地保护
4.4.1 节地与施工用地保护实施措施
4.4.2 节地与施工用地保护措施清单
4.4.3 节地与施工用地保护要素评价
4.5 节材与材料资源利用
4.5.1 节材与材料资源利用实施措施
4.5.2 节材与材料资源利用措施清单
4.5.3 节材与材料资源利用要素评价
4.6 人力资源节约与保护
4.6.1 人力资源节约与保护实施措施
4.6.2 人力资源节约与保护措施清单
4.6.3 人力资源节约与保护要素评价
4.7 绿色工地评价得分
5 碳排放监测及核算
5.1 监测及核算依据
5.2 监测原则
5.3 碳排放源识别
5.4 碳排放核算
5.4.1 核算流程
5.4.2 核算方法
5.4.3 碳排放量计算
6 亮点工程
6.1 新技术的应用
6.2 新设备的应用
6.3 新工艺的应用
6.4 新材料的应用
6.5 新理念的应用
7 效益分析
7.1 环境效益分析
7.2 经济效益分析
7.3 社会效益分析
'''


promptlist_template_short = """
我正在写《{title}》
帮我撰写“绿色工地组织管理”章节，以markdown的语法输出。
结构要求：
3 绿色工地组织管理
3.1 重视前期策划
3.2 加强制度体系建设
3.3 强化过程落实管控
3.4 绿色工地文化
你可以参考的信息：{information}
"""

promptlist_template = [
"""system: 你是一个撰写绿色工地总结报告的环境专家，按照user的需求撰写出优质的报告。
请你帮user撰写《{title}》中“项目背景”章节。你需要遵守的以下规则：
1.请生成尽可能长的段落
2.只需要输出markdown代码，不需要输出其他内容
3.输出的内容不能带上 ```markdown  
4.你撰写的章节必须满足<目录></目录>中的目录结构
5.你可以参考<信息></信息> 中的参考信息（如果有的话）来编写本章的内容

user: 《{title}》,
<目录>
3 绿色工地组织管理
3.1 重视前期策划
3.2 加强制度体系建设
3.3 强化过程落实管控
3.4 绿色工地文化
</目录>,
<信息>{information}</信息>
"""
,
]



# promptlist_template = [
#     """
# 我正在写《{title}》
# 帮我撰写“项目背景章节”，以markdown的语法输出。
# 结构要求：
# 1 项目背景
# 1.1 项目概况
# 1.2 绿色工地创建的必要性
# 你可以参考的信息：{information}
#     """,
#     """
# 我正在写《{title}》
# 帮我撰写“编制依据章节”，以markdown的语法输出。
# 结构要求：
# 2 编制依据
# 2.1 法律法规
# 2.2 规范标准
# 2.2.1 国家层面规范标准
# 2.2.2 地方层面规范标准
# 2.2.3 集团层面规范标准
# 2.3 项目相关文件
# 你可以参考的信息：{information}
#     """,
# ]


promptlist_template = [
    """
我正在写《{title}》
帮我撰写“项目背景章节”，以markdown格式输出。
结构要求：
1 项目背景
1.1 项目概况
1.2 绿色工地创建的必要性
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写“编制依据章节”，以markdown格式输出。
结构要求：
2 编制依据
2.1 法律法规
2.2 规范标准
2.2.1 国家层面规范标准
2.2.2 地方层面规范标准
2.2.3 集团层面规范标准
2.3 项目相关文件
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写的“绿色工地组织管理章节”，以markdown格式输出。
结构要求：
3 绿色工地组织管理
3.1 重视前期策划
3.2 加强制度体系建设
3.3 强化过程落实管控
3.4 绿色工地文化
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写“五节一环保实施措施章节”，以markdown格式输出。
结构要求：
4 “五节一环保”实施措施
4.1 环境保护
4.1.1 环境保护实施措施
4.1.2 环境保护措施清单
4.1.3 环境保护要素评价
4.2 节水与水资源利用
4.2.1 节水与水资源利用实施措施
4.2.2 节水与水资源利用措施清单
4.2.3 节水与水资源利用要素评价
4.3 节能与能源利用
4.3.1 节能与能源利用实施措施
4.3.2 节能与能源利用措施清单
4.3.3 节能与能源利用要素评价
4.4 节地与施工用地保护
4.4.1 节地与施工用地保护实施措施
4.4.2 节地与施工用地保护措施清单
4.4.3 节地与施工用地保护要素评价
4.5 节材与材料资源利用
4.5.1 节材与材料资源利用实施措施
4.5.2 节材与材料资源利用措施清单
4.5.3 节材与材料资源利用要素评价
4.6 人力资源节约与保护
4.6.1 人力资源节约与保护实施措施
4.6.2 人力资源节约与保护措施清单
4.6.3 人力资源节约与保护要素评价
4.7 绿色工地评价得分
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写“碳排放监测及核算章节”，以markdown格式输出。
结构要求：
5 碳排放监测及核算
5.1 监测及核算依据
5.2 监测原则
5.3 碳排放源识别
5.4 碳排放核算
5.4.1 核算流程
5.4.2 核算方法
5.4.3 碳排放量计算
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写“亮点工程章节”，以markdown格式输出。
结构要求：
6 亮点工程
6.1 新技术的应用
6.2 新设备的应用
6.3 新工艺的应用
6.4 新材料的应用
6.5 新理念的应用
你可以参考的信息：{information}
    """,
    """
我正在写《{title}》
帮我撰写“效益分析章节”，以markdown格式输出。
结构要求：
7 效益分析
7.1 环境效益分析
7.2 经济效益分析
7.3 社会效益分析
你可以参考的信息：{information}
    """
]


if __name__ == "__main__":
    # 打印 写作指导者 的提示词
    title = "TTT"
    content_str = "CCC"
    current_headline = "CTCTCTC"
    
    write_instructor_prompt = WRITER_INSTRUCTOR_PROMPT_ROLE + WRITER_INSTRUCTOR_PROMPT_CONSTRAINT + PromptTemplate(
        input_variables=["title", "content"],
        template = WRITER_INSTRUCTOR_PROMPT_TITLE_AND_CONTENT
    ).format(title=title, content=content_str) + WRITER_INSTRUCTOR_PROMPT_EXAMPLE + PromptTemplate(
        input_variables=["current_headline"],
        template = WRITER_INSTRUCTOR_PROMPT_END
    ).format(current_headline=current_headline)
    
    print(write_instructor_prompt)