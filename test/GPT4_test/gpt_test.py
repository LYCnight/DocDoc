from pathlib import Path		
import sys
cur_path = Path(__file__).parent    # 当前目录    DocDoc/test/GPT4_test
test_path = Path(__file__).parent.parent    # 测试目录    DocDoc/test
root_path = Path(__file__).parent.parent.parent    # 项目根目录    DocDoc/
sys.path.append(str(cur_path))
sys.path.append(str(test_path))
sys.path.append(str(root_path))

prompt_en = """<JSON>
{
    "content": [
        {"id": 0, "heading": "Environmental Impact Assessment Report of Liumen Sluice Drainage Project in Huarong Flood Control Area of Dongting Lake, Hunan Province", "dep": [-1], "level": 0},
        {"id": 1, "heading": "Overview", "dep": [2,3,4,5,6], "level": 1},
        {"id": 2, "heading": "Project Background and Project Construction Characteristics", "dep": [-1], "level": 2},
        {"id": 3, "heading": "Environmental Impact Assessment Work Process", "dep": [-1], "level": 2},
        {"id": 4, "heading": "Analysis and Determination of Relevant Situations", "dep": [-1], "level": 2},
        {"id": 5, "heading": "Main Environmental Issues of Concern", "dep": [-1], "level": 2},
        {"id": 6, "heading": "Main Evaluation Conclusions of the Report", "dep": [-1], "level": 2},
        {"id": 7, "heading": "General Provisions", "dep": [-1], "level": 1},
        {"id": 8, "heading": "Construction Project Engineering Analysis", "dep": [-1], "level": 1},
        {"id": 9, "heading": "Environmental Status Survey and Evaluation", "dep": [-1], "level": 1},
        {"id": 10, "heading": "Prediction and Evaluation of Environmental Impacts", "dep": [11,12,17,20,23,29,35,41,44,45,48], "level": 1},
        {"id": 11, "heading": "Prediction and Evaluation of Ecological Environmental Impacts", "dep": [-1], "level": 2},
        {"id": 12, "heading": "Prediction and Evaluation of Hydrological Conditions", "dep": [13,16], "level": 2},
        {"id": 13, "heading": "Hydrological Conditions during Construction Period", "dep": [14,15], "level": 3},
        {"id": 14, "heading": "Impact on Surface Hydrological Conditions of River Sections", "dep": [-1], "level": 4},
        {"id": 15, "heading": "Impact on Surrounding Groundwater Hydrological Conditions of River Sections", "dep": [-1], "level": 4},
        {"id": 16, "heading": "Hydrological Conditions during Operation Period", "dep": [-1], "level": 3},
        {"id": 17, "heading": "Prediction and Evaluation of Water Environment Impacts", "dep": [18,19], "level": 2},
        {"id": 18, "heading": "Surface Water Environment Impacts during Construction Period", "dep": [-1], "level": 3},
        {"id": 19, "heading": "Surface Water Environment Impacts during Operation Period", "dep": [-1], "level": 3},
        {"id": 20, "heading": "Prediction and Evaluation of Groundwater Environment Impacts", "dep": [21,22], "level": 2},
        {"id": 21, "heading": "Groundwater Environment Impacts during Construction Period", "dep": [-1], "level": 3},
        {"id": 22, "heading": "Groundwater Environment Impacts during Operation Period", "dep": [-1], "level": 3},
        {"id": 23, "heading": "Prediction and Evaluation of Soil Erosion", "dep": [24,25,26], "level": 2},
        {"id": 24, "heading": "Affected Range and Prediction Period", "dep": [-1], "level": 3},
        {"id": 25, "heading": "Content and Methods of Soil Erosion Prediction", "dep": [-1], "level": 3},
        {"id": 26, "heading": "Prediction Results", "dep": [27,28], "level": 3},
        {"id": 27, "heading": "Potential Hazards of Soil Erosion", "dep": [-1], "level": 4},
        {"id": 28, "heading": "Analysis and Results of Soil Erosion Prediction", "dep": [-1], "level": 4},
        {"id": 29, "heading": "Prediction and Evaluation of Atmospheric Environment Impacts", "dep": [30,34], "level": 2},
        {"id": 30, "heading": "Analysis of Environmental Impacts during Construction Period", "dep": [31,32,33], "level": 3},
        {"id": 31, "heading": "Analysis of Construction Dust Impact", "dep": [-1], "level": 4},
        {"id": 32, "heading": "Analysis of Construction Exhaust Gas Impact", "dep": [-1], "level": 4},
        {"id": 33, "heading": "Analysis of Construction Camp Canteen Fume Impact", "dep": [-1], "level": 4},
        {"id": 34, "heading": "Analysis of Environmental Impacts during Operation Period", "dep": [-1], "level": 3},
        {"id": 35, "heading": "Prediction and Evaluation of Sound Environment Impacts", "dep": [36,40], "level": 2},
        {"id": 36, "heading": "Evaluation of Noise Impact during Construction Period", "dep": [37,38,39], "level": 3},
        {"id": 37, "heading": "Impact of Fixed Noise Sources", "dep": [-1], "level": 4},
        {"id": 38, "heading": "Impact of Mobile Noise Sources", "dep": [-1], "level": 4},
        {"id": 39, "heading": "Prediction of Noise Impact on Sound Environment Sensitive Points", "dep": [-1], "level": 4},
        {"id": 40, "heading": "Evaluation of Noise Impact during Operation Period", "dep": [-1], "level": 3},
        {"id": 41, "heading": "Environmental Impacts of Solid Waste", "dep": [42,43], "level": 2},
        {"id": 42, "heading": "Environmental Impact Assessment of Solid Waste during Construction Period", "dep": [-1], "level": 3},
        {"id": 43, "heading": "Environmental Impact Assessment of Solid Waste during Operation Period", "dep": [-1], "level": 3},
        {"id": 44, "heading": "Environmental Impact Assessment of Resettlement", "dep": [-1], "level": 2},
        {"id": 45, "heading": "Environmental Impact Assessment of Social Environment", "dep": [46,47], "level": 2},
        {"id": 46, "heading": "Impact on Social Environment during Construction Period", "dep": [-1], "level": 3},
        {"id": 47, "heading": "Impact on Social Environment during Operation Period", "dep": [-1], "level": 3},
        {"id": 48, "heading": "Impact on Public Health", "dep": [-1], "level": 2},
        {"id": 49, "heading": "Conclusion of Environmental Impact Assessment", "dep": [50,51,53,61,62,63,64,65], "level": 1},
        {"id": 50, "heading": "Project Overview", "dep": [-1], "level": 2},
        {"id": 51, "heading": "Conclusion of Environmental Status Assessment", "dep": [52], "level": 2},
        {"id": 52, "heading": "Current Status of Environmental Quality", "dep": [-1], "level": 3},
        {"id": 53, "heading": "Conclusion of Environmental Impact Assessment", "dep": [54,55,56,57,58,59,60], "level": 2},
        {"id": 54, "heading": "Hydrological Conditions", "dep": [-1], "level": 3},
        {"id": 55, "heading": "Water Environment Impact", "dep": [-1], "level": 3},
        {"id": 56, "heading": "Ecological Environment Impact", "dep": [-1], "level": 3},
        {"id": 57, "heading": "Soil Erosion Impact", "dep": [-1], "level": 3},
        {"id": 58, "heading": "Atmospheric and Sound Environment Impact", "dep": [-1], "level": 3},
        {"id": 59, "heading": "Resettlement Environmental Impact", "dep": [-1], "level": 3},
        {"id": 60, "heading": "Social Environment Impact", "dep": [-1], "level": 3},
        {"id": 61, "heading": "Main Environmental Protection Measures", "dep": [-1], "level": 2},
        {"id": 62, "heading": "Environmental Protection Investment Budget and Benefit Analysis", "dep": [-1], "level": 2},
        {"id": 63, "heading": "Conclusion of Public Participation", "dep": [-1], "level": 2},
        {"id": 64, "heading": "Comprehensive Evaluation Conclusion", "dep": [-1], "level": 2},
        {"id": 65, "heading": "Recommendations", "dep": [-1], "level": 2}
    ]
}
</JSON>"""


prompt_template = """
The directory is stored in a JSON data structure and encapsulated within <JSON></JSON>, for example:
<JSON>
{
    "content": [
        {"id": 0, "heading": "Environmental Impact Assessment Report on the Construction Project of Comprehensive Treatment of Water System Connection and Rural Water System in Yueyang County", "dep": [-1], "level": 0},
        {"id": 1, "heading": "Overview", "dep": [-1], "level": 1},
        {"id": 2, "heading": "Analysis and Judgment of Relevant Environmental Protection Policies", "dep": [-1], "level": 2},
        {"id": 3, "heading": "Analysis of Consistency with Industrial Policies", "dep": [-1], "level": 3},
        {"id": 4, "heading": "Analysis of Compliance with Laws and Regulations", "dep": [-1], "level": 3},
        {"id": 5, "heading": "Analysis of Consistency with Relevant Plans", "dep": [-1], "level": 3},
        {"id": 6, "heading": "Main Conclusions of the Project's Environmental Impact Assessment Report", "dep": [12], "level": 2},
        {"id": 7, "heading": "Conclusions and Recommendations", "dep": [-1], "level": 1},
        {"id": 8, "heading": "Project Overview", "dep": [-1], "level": 2},
        {"id": 9, "heading": "Environmental Management", "dep": [3], "level": 3},
        {"id": 10, "heading": "Main Environmental Protection Measures", "dep": [-1], "level": 2},
        {"id": 11, "heading": "Economic Analysis of Environmental Impacts", "dep": [-1], "level": 3},
        {"id": 12, "heading": "Summary of Environmental Impact Assessment", "dep": [-1], "level": 3}
    ]
}
</JSON>


### Meaning of Each Field:
- "id": Represents the unique identifier of each directory item, used to distinguish between different directory items.
- "heading": Represents the title of each directory item, describing its content.
- "dep": Represents the dependency of the current directory item. This is an array containing the id(s) of other directory items that the current item depends on or is related to. "-1" usually indicates that the current directory item is a top-level item, meaning it does not depend on any other items. For example, for the directory item with id 6, "Main Conclusions of the Project's Environmental Impact Assessment Report," its dep value is [12], indicating that it depends on the directory item with id 12, "Summary of Environmental Impact Assessment."
(Note: The dep of any directory item will not depend on (id:0), because (id:0) is a top-level directory item representing the title of the article.)
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

### Directory Item Dependency Rules:
1. In the directory structure, a directory item can depend on one or more other directory items. This dependency relationship indicates that the referenced text is needed during writing.
For example, in a novel, the writing of a plot may depend on a previous plot or an earlier setting. Or in a multi-level directory text, a broader topic may depend on many more specific subtopics for detailed information.
2. In shallow directory structures (such as novel directories), directory items are usually linear, and the content of the next item is likely based on the content of the previous item. If there is foreshadowing, it needs to be based on earlier plots or settings.
For example:
    {"id": i-1, "heading": "A", "dep": [i-6], "level": 1},
    {"id": i, "heading": "B", "dep": [i-1], "level": 1},
    {"id": i+1, "heading": "C", "dep": [i], "level": 1},
3. On Medium and Deep levels, parent directory items typically depend on their child directory items. This is because, in such cases, a larger theme or viewpoint is broken down into multiple sub-themes or viewpoints, and each sub-theme or viewpoint supports the parent theme or viewpoint. This follows a hierarchical writing logic.
For example:
    {"id": i, "heading": "A", "dep": [i+1, i+2, i+3], "level": 1},
    {"id": i+1, "heading": "A", "dep": [-1], "level": 1},
    {"id": i+2, "heading": "B", "dep": [-1], "level": 1},
    {"id": i+3, "heading": "C", "dep": [-1], "level": 1},
4. For the introduction and conclusion sections of an article, they typically have no dependencies, but the conclusion may require readers to have an understanding of the entire article's content. However, if the conclusion summarizes the preceding key points, it can be considered dependent on those key points.
5. None of the directory items' dependencies will depend on (id:0) because (id:0) represents a top-level directory item, indicating the title of the article.
6. Finally, it's worth noting that the dependency relationships in the directory are not necessarily linear. Depending on the content of the article, some directory items may need to depend on multiple other directory items simultaneously.


Q: I want to write a science fiction novel with the theme of the moon titled "Under the Moonlight." Could you generate the table of contents for the novel "Under the Moonlight" and provide a detailed explanation of the dependencies between the items in the table of contents?
A:
### Analysis:
The novel falls under the Shallow type of text, with levels ranging from 0 to 1, and does not contain multiple levels of directory items. To make the plot more exciting, I'll use foreshadowing, where some plot points will depend on earlier events or settings.
### Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "Under the Moonlight", "dep": [-1], "level": 0},
        {"id": 1, "heading": "Prologue", "dep": [-1], "level": 1},
        {"id": 2, "heading": "The Mysterious Invitation", "dep": [-1], "level": 1},
        {"id": 3, "heading": "Preparation on Earth", "dep": [2], "level": 1},
        {"id": 4, "heading": "Embarking on the Space Journey", "dep": [3], "level": 1},
        {"id": 5, "heading": "Anomalies in Space", "dep": [4, 2], "level": 1},
        {"id": 6, "heading": "The Moon's Invitation", "dep": [5], "level": 1},
        {"id": 7, "heading": "Secrets of the Falling Moon", "dep": [6], "level": 1},
        {"id": 8, "heading": "Moonshadow Village", "dep": [7], "level": 1},
        {"id": 9, "heading": "Moonshadow Tribe", "dep": [8], "level": 1},
        {"id": 10, "heading": "Mysterious Legends", "dep": [9,2], "level": 1},
        {"id": 11, "heading": "The Secret of Moon Ore", "dep": [10], "level": 1},
        {"id": 12, "heading": "Dangerous Decision", "dep": [11,2], "level": 1},
        {"id": 13, "heading": "Farewell, Earth", "dep": [12], "level": 1},
        {"id": 14, "heading": "Challenges During Return Journey", "dep": [13,2], "level": 1},
        {"id": 15, "heading": "Brave Sacrifice", "dep": [14], "level": 1},
        {"id": 16, "heading": "Safe Return", "dep": [15], "level": 1},
        {"id": 17, "heading": "After the Return", "dep": [16], "level": 1},
        {"id": 18, "heading": "New Horizons", "dep": [17], "level": 1},
        {"id": 19, "heading": "Unveiling Secrets", "dep": [18,2], "level": 1},
        {"id": 20, "heading": "Conclusion", "dep": [-1], "level": 1}
    ]
}
</JSON>
### Explanation:
1. "The Mysterious Invitation" (id:2) contains the foreshadowing of the story, which unfolds and explains in subsequent plots, showcasing unknown worlds and hidden secrets to the audience.
2. "Preparation on Earth" (id:3) depends on "The Mysterious Invitation" (id:2). In this chapter, the protagonists receive a mysterious invitation and begin their preparations for the space journey.
3. "Anomalies in Space" (id:5) The plot here not only depends on their journey commencement but also relates back to the initial mysterious invitation, serving to reveal foreshadowing.
4. "Mysterious Legends" (id:10) This chapter depends on their entry into Moonshadow Village and the initial mysterious invitation, as the legends are related to the secrets in both the invitation and the village.
5. "Dangerous Decision" (id:12) This chapter's plot also depends on the mysterious invitation, which presents them with the decision they face at that moment and becomes one of the main reasons for their inner struggles.
6. "Challenges During Return Journey" (id:14) The plot of this chapter is built upon their impending return to Earth, and these challenges are related to the received mysterious invitation.
7. "New Horizons" (id:17) and "Unveiling Secrets" (id:18), The plots of these two chapters are established after the return, where the protagonists deal with their lives and reveal the mysterious secrets encountered during their journey.
8. "Conclusion" (id:20) summarizes the journey, foreshadows new beginnings, and is an independent ending, but readers need a rough understanding of the main content of the entire work.


Q: I want to write an opinion article about Trump's defeat in the 2020 US presidential election, titled "2020 US Election | Three Reasons for Trump's Defeat." Could you generate the table of contents for the opinion article and provide a detailed explanation of the dependencies between the items in the table of contents?
A:
### Analysis:
Opinion articles belong to the Medium category of text, with levels typically ranging from 0 to 3. When writing this opinion article, I believe setting the maximum level to 2 is more appropriate, i.e., level = 0~2. When composing an opinion article, the main goal is to elucidate and support our viewpoints. In this article about Trump's defeat, all three reasons are major points of discussion, while specific examples and arguments serve as sub-points that support these major points. Therefore, each reason (parent entry) should depend on the detailed items used to explain or support it (child entries).
### Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "2020 US Election | Three Reasons for Trump's Defeat", "dep": [-1], "level": 0},
        {"id": 1, "heading": "Introduction", "dep": [-1], "level": 1},
        {"id": 2, "heading": "First Reason: Handling of the COVID-19 Pandemic", "dep": [3,4,5], "level": 1},
        {"id": 3, "heading": "Severity of the COVID-19 Pandemic", "dep": [-1], "level": 2},
        {"id": 4, "heading": "Trump Administration's Response Measures and Issues", "dep": [-1], "level": 2},
        {"id": 5, "heading": "Public Perception of the Trump Administration's Handling of the Pandemic", "dep": [-1], "level": 2},
        {"id": 6, "heading": "Second Reason: Trade War Issues", "dep": [7,8,9], "level": 1},
        {"id": 7, "heading": "Trade Policies Implemented by the Trump Administration", "dep": [-1], "level": 2},
        {"id": 8, "heading": "Impact of Trade Policies", "dep": [-1], "level": 2},
        {"id": 9, "heading": "Public Reaction to Trump's Trade War", "dep": [-1], "level": 2},
        {"id": 10, "heading": "Third Reason: Racial Issues", "dep": [11,12,13], "level": 1},
        {"id": 11, "heading": "Racial Tensions under the Trump Administration", "dep": [-1], "level": 2},
        {"id": 12, "heading": "Impact of Racial Issues on Voters", "dep": [-1], "level": 2},
        {"id": 13, "heading": "Public Perception of Trump's Stance on Racial Issues", "dep": [-1], "level": 2},
        {"id": 14, "heading": "Conclusion", "dep": [2,6,10], "level": 1}
    ]
}
</JSON>
### Explanation:
1. "Introduction" (id:1) marks the beginning of the article and has no dependencies.
2. "First Reason: Handling of the COVID-19 Pandemic" (id:2) is a parent entry that depends on three child entries: "Severity of the COVID-19 Pandemic" (id:3), "Trump Administration's Response Measures and Issues" (id:4), and "Public Perception of the Trump Administration's Handling of the Pandemic" (id:5). These three child entries provide specific examples and data to support the viewpoint of the "First Reason." The writing sequence should involve completing the three child entries before writing "First Reason: Handling of the COVID-19 Pandemic" (id:2).
3. "Second Reason: Trade War Issues" (id:6) is a parent entry that heavily relies on its three child entries: "Trade Policies Implemented by the Trump Administration" (id:7), "Impact of Trade Policies" (id:8), and "Public Reaction to Trump's Trade War" (id:9). This hierarchical structure is crucial for maintaining readability, logic, and the completeness of arguments. The writing sequence should involve completing the three child entries before writing "Second Reason: Trade War Issues" (id:6).
4. "Third Reason: Racial Issues" (id:10) is a parent entry that depends on its three child entries: "Racial Tensions under the Trump Administration" (id:11), "Impact of Racial Issues on Voters" (id:12), and "Public Perception of Trump's Stance on Racial Issues" (id:13). This structured approach requires a clear and organized writing style, with content unfolding in the sequence of the child entries. The writing sequence should involve completing the three child entries before writing "Third Reason: Racial Issues" (id:10).
5. "Conclusion" (id:14) serves as the end of the article and depends on all the preceding viewpoints or reasons: "First Reason: Handling of the COVID-19 Pandemic" (id:2), "Second Reason: Trade War Issues" (id:6), and "Third Reason: Racial Issues" (id:10). In the conclusion, the author should summarize all the arguments presented earlier and provide commentary or insights.

Q: I want to write an Environmental Impact Assessment Report, titled "Environmental Impact Report of the Hua Rong City Flood Drainage Project at the Six-Gate Sluice in the Dongting Lake Area, Hunan Province", and I have written the table of contents for you. Please provide `### Explanation:` for me.\n""" + prompt_en + "\nA:"


# print(prompt_template)

# --- chat --- 
# Key01：sk-o1DRfeJuLNNisw2VCeAbEfDf2b0c42Eb890eAd5fC0C3D92c
# Key02: sk-WgLd2UkCvs5i95cRB8C67f7d773c4b1bBdEd9c4a2195B93f
# key03: sk-FF1K83E40qOybOvBAeC6BfFf7262424e89Ca977337E0105d
# Key04: sk-3mvPeWqNOhGpfgsUF2265bDe62Dd4028821a37575b3eBa15
# key05: sk-QJUI3EgaSm07iRnv9b93B31a71C24c78972f96527a96824c
import os
os.environ["OPENAI_API_KEY"] = "sk-QJUI3EgaSm07iRnv9b93B31a71C24c78972f96527a96824c" #输入网站发给你的转发key
os.environ["OPENAI_BASE_URL"] = "https://api.gptapi.us/v1/chat/completions"
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"}
    # {"role": "user", "content": prompt}
    # {"role": "user", "content": fake_history}
  ]
)
response = completion.choices[0].message.content
print(response)

# --- write ---
# prompt = prompt_template
# import os
# os.environ["OPENAI_API_KEY"] = "sk-JlMLbWkryswSpPygBf8eA723Aa0b4a49A7747eAb9986B71e" #输入网站发给你的转发key
# os.environ["OPENAI_BASE_URL"] = "https://api.gptapi.us/v1/chat/completions"
# from openai import OpenAI
# client = OpenAI()
# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": prompt}
#     # {"role": "user", "content": prompt}
#     # {"role": "user", "content": fake_history}
#   ]
# )
# response = completion.choices[0].message.content
# print(response)


# from LLMs import ChatGLM
# from core.Agent import ContentExpert
# from DocDoc_EMNLP import Heading

# llm = ChatGLM()
# contentExpert = ContentExpert(llm)

# xlsx_file_path = "/root/AI4E/lzd/DocDoc/test/GPT4_test/content 湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书.xlsx"
# content:list[Heading] = contentExpert.read_content_from_xlsx(xlsx_file_path)
# content_json:str = contentExpert.content_to_jsonStr(content)

# print(content_json)





# c:\Users\lzd\Desktop\目录\content 湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书.xlsx


prompt_ch = """
<JSON>
{
    "content": [
        {"id": 0, "heading": "湖南省洞庭湖区华容护城涝区六门闸排涝工程环境影响报告书", "dep": [-1], "level": 0},
        {"id": 1, "heading": "概述", "dep": [2,3,4,5,6], "level": 1},
        {"id": 2, "heading": "项目背景及项目建设特点", "dep": [-1], "level": 2},
        {"id": 3, "heading": "环境影响评价工作过程", "dep": [-1], "level": 2},
        {"id": 4, "heading": "分析判定相关情况", "dep": [-1], "level": 2},
        {"id": 5, "heading": "关注的主要环境问题", "dep": [-1], "level": 2},
        {"id": 6, "heading": "报告书主要评价结论", "dep": [-1], "level": 2},
        {"id": 7, "heading": "总则", "dep": [-1], "level": 1},
        {"id": 8, "heading": "建设项目工程分析", "dep": [-1], "level": 1},
        {"id": 9, "heading": "环境现状调查与评价", "dep": [-1], "level": 1},
        {"id": 10, "heading": "环境影响预测与评价", "dep": [11,12,17,20,23,29,35,41,44,45,48], "level": 1},
        {"id": 11, "heading": "生态环境影响预测和评价", "dep": [-1], "level": 2},
        {"id": 12, "heading": "水文情势预测和评价", "dep": [13,16], "level": 2},
        {"id": 13, "heading": "施工期水文情势", "dep": [14,15], "level": 3},
        {"id": 14, "heading": "对河段地表水文情势的影响", "dep": [-1], "level": 4},
        {"id": 15, "heading": "对河段周边地下水文情势的影响", "dep": [-1], "level": 4},
        {"id": 16, "heading": "运行期水文情势", "dep": [-1], "level": 3},
        {"id": 17, "heading": "水环境影响预测和评价", "dep": [18,19], "level": 2},
        {"id": 18, "heading": "施工期地表水环境影响", "dep": [-1], "level": 3},
        {"id": 19, "heading": "运行期地表水环境影响", "dep": [-1], "level": 3},
        {"id": 20, "heading": "地下水环境影响预测和评价", "dep": [21,22], "level": 2},
        {"id": 21, "heading": "施工期地下水环境影响", "dep": [-1], "level": 3},
        {"id": 22, "heading": "运行期地下水环境影响", "dep": [-1], "level": 3},
        {"id": 23, "heading": "水土流失预测和评价", "dep": [24,25,26], "level": 2},
        {"id": 24, "heading": "影响范围及预测时段", "dep": [-1], "level": 3},
        {"id": 25, "heading": "水土流失预测内容和方法", "dep": [-1], "level": 3},
        {"id": 26, "heading": "预测结果", "dep": [27,28], "level": 3},
        {"id": 27, "heading": "可能造成的水土流失危害", "dep": [-1], "level": 4},
        {"id": 28, "heading": "水土流失预测分析与结果", "dep": [-1], "level": 4},
        {"id": 29, "heading": "大气环境影响预测评价", "dep": [30,34], "level": 2},
        {"id": 30, "heading": "施工期环境影响分析", "dep": [31,32,33], "level": 3},
        {"id": 31, "heading": "施工扬尘影响分析", "dep": [-1], "level": 4},
        {"id": 32, "heading": "施工废气影响分析", "dep": [-1], "level": 4},
        {"id": 33, "heading": "施工营地食堂油烟废气影响分析", "dep": [-1], "level": 4},
        {"id": 34, "heading": "运行期环境影响分析", "dep": [-1], "level": 3},
        {"id": 35, "heading": "声环境影响预测和评价", "dep": [36,40], "level": 2},
        {"id": 36, "heading": "施工期噪声影响评价", "dep": [37,38,39], "level": 3},
        {"id": 37, "heading": "固定噪声源影响", "dep": [-1], "level": 4},
        {"id": 38, "heading": "流动噪声影响", "dep": [-1], "level": 4},
        {"id": 39, "heading": "声环境敏感点噪声影响预测", "dep": [-1], "level": 4},
        {"id": 40, "heading": "运行期噪声影响评价", "dep": [-1], "level": 3},
        {"id": 41, "heading": "固体废弃物的环境影响", "dep": [42,43], "level": 2},
        {"id": 42, "heading": "施工期固体废物的环境影响评价", "dep": [-1], "level": 3},
        {"id": 43, "heading": "运行期固体废物的环境影响评价", "dep": [-1], "level": 3},
        {"id": 44, "heading": "移民安置环境影响评价", "dep": [-1], "level": 2},
        {"id": 45, "heading": "社会环境影响评价", "dep": [46,47], "level": 2},
        {"id": 46, "heading": "施工期对社会环境影响", "dep": [-1], "level": 3},
        {"id": 47, "heading": "运行期对社会环境的影响", "dep": [-1], "level": 3},
        {"id": 48, "heading": "对人群健康的影响", "dep": [-1], "level": 2},
        {"id": 49, "heading": "环境影响评价结论", "dep": [50,51,53,61,62,63,64,65], "level": 1},
        {"id": 50, "heading": "工程概况", "dep": [-1], "level": 2},
        {"id": 51, "heading": "环境现状评价结论", "dep": [52], "level": 2},
        {"id": 52, "heading": "环境质量现状", "dep": [-1], "level": 3},
        {"id": 53, "heading": "环境影响评价结论", "dep": [54,55,56,57,58,59,60], "level": 2},
        {"id": 54, "heading": "水文情势", "dep": [-1], "level": 3},
        {"id": 55, "heading": "水环境影响", "dep": [-1], "level": 3},
        {"id": 56, "heading": "生态环境影响", "dep": [-1], "level": 3},
        {"id": 57, "heading": "水土流失影响", "dep": [-1], "level": 3},
        {"id": 58, "heading": "大气和声环境影响", "dep": [-1], "level": 3},
        {"id": 59, "heading": "移民安置环境影响", "dep": [-1], "level": 3},
        {"id": 60, "heading": "社会环境影响", "dep": [-1], "level": 3},
        {"id": 61, "heading": "主要环境保护措施", "dep": [-1], "level": 2},
        {"id": 62, "heading": "环境保护投资概算与效益分析", "dep": [-1], "level": 2},
        {"id": 63, "heading": "公众参与结论", "dep": [-1], "level": 2},
        {"id": 64, "heading": "综合评价结论", "dep": [-1], "level": 2},
        {"id": 65, "heading": "建议", "dep": [-1], "level": 2}
    ]
}
</JSON>
"""