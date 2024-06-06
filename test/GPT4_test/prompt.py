json = """{
        "content":[
                {"id": 0, "heading": "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", "dep": [-1], "level": 0},
                {"id": 1, "heading": "概述", "dep": [-1], "level": 1},
                {"id": 2, "heading": "分析判定相关环保政策", "dep": [-1], "level": 2},
                {"id": 3, "heading": "产业政策相符性分析", "dep": [-1], "level": 3},
                {"id": 4, "heading": "法律法规符合性分析", "dep": [-1], "level": 3},
                {"id": 5, "heading": "与相关规划符合性分析", "dep": [-1], "level": 3},
                {"id": 6, "heading": "项目环评报告书的主要结论", "dep": [12], "level": 2},
                {"id": 7, "heading": "结论与建议", "dep": [-1], "level": 1},
                {"id": 8, "heading": "项目概况", "dep": [-1], "level": 2},
                {"id": 9, "heading": "环境管理", "dep": [3], "level": 3},
                {"id": 10, "heading": "主要环保措施", "dep": [-1], "level": 2},
                {"id": 11, "heading": "环境影响经济损益分析", "dep": [-1], "level": 3},
                {"id": 12, "heading": "环评总结论", "dep": [-1], "level": 3}
        ]
}"""

#  -- paper -- 
# Q: 我想写一篇计算机视觉领域的论文，标题为《Deep Residual Learning for Image Recognition》, 大致内容为：[更深层次的神经网络更难训练。我们提出了一个残差学习框架，以简化比以前使用的网络更深的网络的训练。我们显式地将层重新表示为参考层输入的学习残差函数，而不是学习未引用的函数。我们提供了全面的经验证据，表明这些残差网络更容易优化，并且可以从显著增加的深度中获得准确性。在ImageNet数据集上，我们评估了深度高达152层的残差网络-比VGG网络深8倍，但仍然具有较低的复杂性。这些残差网络的集合在ImageNet测试集上实现了3.57%的误差。这一结果在ILSVRC 2015年的分类任务中获得了第一名。我们还分析了CIFAR-10与100和1000层。表征的深度对于许多视觉识别任务是至关重要的。仅仅由于我们非常深入的表示，我们在COCO对象检测数据集上获得了28%的相对改进。深度残差网络是我们提交ILSVRC和COCO 2015竞赛的基础，我们还赢得了ImageNet检测，ImageNet本地化，COCO检测和COCO分割任务的第一名。]。请你帮我生成具备依赖项的目录结构。
# A: 

# -- encyclopedia --
# Q: 我想写一则用于Wikipedia的Encyclopedia article，标题为《丰臣秀吉》，请你生成目录，并详细说明目录项的依赖关系。
# A: 

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



Q: I want to write an Environmental Impact Assessment Report, titled "Environmental Impact Report of the Hua Rong City Flood Drainage Project at the Six-Gate Sluice in the Dongting Lake Area, Hunan Province". Please Write a table of contents for me.
A:
### Analysis:
Environmental Impact Assessment Report generally has a deep catalog structure, so I think it should belong to the Deep type Text. Given this theme, I set the max level to 4, whose category structure can fit well with this report.
<JSON>
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
</JSON>
### Explanation:
1. **Overview (id: 1)**: This section provides a general introduction to the project and its environmental impact assessment. It depends on several detailed sections that provide the necessary background and context:
   - **Project Background and Project Construction Characteristics (id: 2)**
   - **Environmental Impact Assessment Work Process (id: 3)**
   - **Analysis and Determination of Relevant Situations (id: 4)**
   - **Main Environmental Issues of Concern (id: 5)**
   - **Main Evaluation Conclusions of the Report (id: 6)**
2. **General Provisions (id: 7)**: This section outlines the general guidelines and provisions for the environmental impact assessment. It stands alone and does not depend on other sections.
3. **Construction Project Engineering Analysis (id: 8)**: This section analyzes the engineering aspects of the construction project. It is independent and does not rely on other sections.
4. **Environmental Status Survey and Evaluation (id: 9)**: This section surveys and evaluates the current environmental status. It is also independent.
5. **Prediction and Evaluation of Environmental Impacts (id: 10)**: This is a comprehensive section that predicts and evaluates various environmental impacts. It depends on multiple detailed subsections:
   - **Prediction and Evaluation of Ecological Environmental Impacts (id: 11)**
   - **Prediction and Evaluation of Hydrological Conditions (id: 12)**
   - **Prediction and Evaluation of Water Environment Impacts (id: 17)**
   - **Prediction and Evaluation of Groundwater Environment Impacts (id: 20)**
   - **Prediction and Evaluation of Soil Erosion (id: 23)**
   - **Prediction and Evaluation of Atmospheric Environment Impacts (id: 29)**
   - **Prediction and Evaluation of Sound Environment Impacts (id: 35)**
   - **Environmental Impacts of Solid Waste (id: 41)**
   - **Environmental Impact Assessment of Resettlement (id: 44)**
   - **Environmental Impact Assessment of Social Environment (id: 45)**
   - **Impact on Public Health (id: 48)**
6. **Prediction and Evaluation of Hydrological Conditions (id: 12)**: This section depends on:
   - **Hydrological Conditions during Construction Period (id: 13)**
   - **Hydrological Conditions during Operation Period (id: 16)**
7. **Hydrological Conditions during Construction Period (id: 13)**: This section further depends on:
   - **Impact on Surface Hydrological Conditions of River Sections (id: 14)**
   - **Impact on Surrounding Groundwater Hydrological Conditions of River Sections (id: 15)**
8. **Prediction and Evaluation of Water Environment Impacts (id: 17)**: This section depends on:
   - **Surface Water Environment Impacts during Construction Period (id: 18)**
   - **Surface Water Environment Impacts during Operation Period (id: 19)**
9. **Prediction and Evaluation of Groundwater Environment Impacts (id: 20)**: This section depends on:
   - **Groundwater Environment Impacts during Construction Period (id: 21)**
   - **Groundwater Environment Impacts during Operation Period (id: 22)**
10. **Prediction and Evaluation of Soil Erosion (id: 23)**: This section depends on:
    - **Affected Range and Prediction Period (id: 24)**
    - **Content and Methods of Soil Erosion Prediction (id: 25)**
    - **Prediction Results (id: 26)**
11. **Prediction Results (id: 26)**: This section further depends on:
    - **Potential Hazards of Soil Erosion (id: 27)**
    - **Analysis and Results of Soil Erosion Prediction (id: 28)**
12. **Prediction and Evaluation of Atmospheric Environment Impacts (id: 29)**: This section depends on:
    - **Analysis of Environmental Impacts during Construction Period (id: 30)**
    - **Analysis of Environmental Impacts during Operation Period (id: 34)**
13. **Analysis of Environmental Impacts during Construction Period (id: 30)**: This section further depends on:
    - **Analysis of Construction Dust Impact (id: 31)**
    - **Analysis of Construction Exhaust Gas Impact (id: 32)**
    - **Analysis of Construction Camp Canteen Fume Impact (id: 33)**
14. **Prediction and Evaluation of Sound Environment Impacts (id: 35)**: This section depends on:
    - **Evaluation of Noise Impact during Construction Period (id: 36)**
    - **Evaluation of Noise Impact during Operation Period (id: 40)**
15. **Evaluation of Noise Impact during Construction Period (id: 36)**: This section further depends on:
    - **Impact of Fixed Noise Sources (id: 37)**
    - **Impact of Mobile Noise Sources (id: 38)**
    - **Prediction of Noise Impact on Sound Environment Sensitive Points (id: 39)**
16. **Environmental Impacts of Solid Waste (id: 41)**: This section depends on:
    - **Environmental Impact Assessment of Solid Waste during Construction Period (id: 42)**
    - **Environmental Impact Assessment of Solid Waste during Operation Period (id: 43)**
17. **Environmental Impact Assessment of Social Environment (id: 45)**: This section depends on:
    - **Impact on Social Environment during Construction Period (id: 46)**
    - **Impact on Social Environment during Operation Period (id: 47)**
18. **Conclusion of Environmental Impact Assessment (id: 49)**: This section summarizes the entire assessment and depends on multiple detailed conclusions:
    - **Project Overview (id: 50)**
    - **Conclusion of Environmental Status Assessment (id: 51)**
    - **Conclusion of Environmental Impact Assessment (id: 53)**
    - **Main Environmental Protection Measures (id: 61)**
    - **Environmental Protection Investment Budget and Benefit Analysis (id: 62)**
    - **Conclusion of Public Participation (id: 63)**
    - **Comprehensive Evaluation Conclusion (id: 64)**
    - **Recommendations (id: 65)**
19. **Conclusion of Environmental Status Assessment (id: 51)**: This section depends on:
    - **Current Status of Environmental Quality (id: 52)**
20. **Conclusion of Environmental Impact Assessment (id: 53)**: This section depends on:
    - **Hydrological Conditions (id: 54)**
    - **Water Environment Impact (id: 55)**
    - **Ecological Environment Impact (id: 56)**
    - **Soil Erosion Impact (id: 57)**
    - **Atmospheric and Sound Environment Impact (id: 58)**
    - **Resettlement Environmental Impact (id: 59)**
    - **Social Environment Impact (id: 60)**
This detailed explanation outlines the dependencies between the various sections of the Environmental Impact Assessment Report, ensuring a logical and comprehensive structure for the document.
"""

prompt = """ 
## 目录结构说明：
目录存储于json数据结构中，并用<JSON></JSON>封装，例如：
<JSON>
{
        "content":[
                {"id": 0, "heading": "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", "dep": [-1], "level": 0},
                {"id": 1, "heading": "概述", "dep": [-1], "level": 1},
                {"id": 2, "heading": "分析判定相关环保政策", "dep": [-1], "level": 2},
                {"id": 3, "heading": "产业政策相符性分析", "dep": [-1], "level": 3},
                {"id": 4, "heading": "法律法规符合性分析", "dep": [-1], "level": 3},
                {"id": 5, "heading": "与相关规划符合性分析", "dep": [-1], "level": 3},
                {"id": 6, "heading": "项目环评报告书的主要结论", "dep": [12], "level": 2},
                {"id": 7, "heading": "结论与建议", "dep": [-1], "level": 1},
                {"id": 8, "heading": "项目概况", "dep": [-1], "level": 2},
                {"id": 9, "heading": "环境管理", "dep": [3], "level": 3},
                {"id": 10, "heading": "主要环保措施", "dep": [-1], "level": 2},
                {"id": 11, "heading": "环境影响经济损益分析", "dep": [-1], "level": 3},
                {"id": 12, "heading": "环评总结论", "dep": [-1], "level": 3}
        ]
}
<JSON>

各个字段的含义
- "id"：表示每个目录项的唯一标识符，可以用来区别不同的目录项。
- "heading"：表示每个目录项的标题，描述了目录项的内容。
- "dep"：代表当前目录项的依赖项，这是一个数组，包含了当前目录项所依赖或关联的其他目录项的id。"-1"通常表示当前目录项是一个顶级项，也就是说它不依赖任何其他项。例如，id为6的"项目环评报告书的主要结论"这一目录项，它的dep值为[12]，表示它依赖于id为12的"环评总结论"这一目录项。
(注意：任何目录项的 dep 都不会依赖于 (id:0), 因为 (id:0) 是一个顶级目录项，表示文章的标题。)
- "level"：代表目录项的等级或深度。"0"通常表示这是一级目录，"1"表示二级目录，"2"表示三级目录，以此类推。比如"id"为0的目录项的"level"为0, 它是文本的title; "id"为1的目录项的"level"为1, 它是一级标题。这个字段可以帮助我们了解目录的层次结构。

### 目录结构规律
所有的文本都可以按目录深度来分类：
- Shallow：浅层目录结构，level 为 0~1 , 线性叙事，不包含多级目录项。。
  - Fiction、News、Opinion articlle
- Medium：多级目录结构,level 为 0~3，包含多级目录项。
  - Academic paper、Encyclopedia article
- Deep：深层目录结构 level 为 0~6，包含深度多级目录项。
  - IT: Software Development Report
  - Medicine: Clinical Study Report
  - Finance: Risk Assessment Report
  - Education: Course Evaluation Report
  - Law: Case Assessment Report
  - Management: Project Management Report
  - Manufacturing: Manufacturing Process Report

### 目录项依赖规则：
1. 在目录结构中，一个目录项可以依赖于一个或者多个其它目录项。这种依赖关系表示写作时需要参考被依赖的文本。
比如在小说中，一个情节的写作需要依赖上一个情节或者更早期的情节。又或者在多级目录文本中，一个更广泛的主题可能依赖于许多更具体的子主题的详细信息。
2. 在浅层目录中（比如小说目录），目录项通常是线性的，下一项的内容大概率会基于上一项的内容。如果存在伏笔手法，则需要基于更初期的情节或者设定。
例如:
    {"id": i-1, "heading": "A", "dep": [i-6], "level": 1},
    {"id": i, "heading": "B", "dep": [i-1], "level": 1},
    {"id": i+1, "heading": "C", "dep": [i], "level": 1},
3. 在多级或者深层目录中（比如分析文章、研究报告等），父目录项（更高级别的目录项）通常依赖于它的子目录项（更详细或者更具体的目录项）。因为在这种情况下，一个大的主题或观点被分解为多个子主题或观点，并且每个子主题或观点都会为父主题或观点提供支持。这符合总-分的写作逻辑。
例如：
    {"id": i, "heading": "A", "dep": [i+1, i+2, i+3], "level": 1},
    {"id": i+1, "heading": "A", "dep": [-1], "level": 1},
    {"id": i+2, "heading": "B", "dep": [-1], "level": 1},
    {"id": i+3, "heading": "C", "dep": [-1], "level": 1},
4. 对于文章的引言和结论部分，它们通常没有依赖，但结论可能需要读者对整个文章的内容有所了解。然而，如果结论是对前面几个关键点的总结，那么它可以视作依赖于那些关键点。
5. 目录项的 dep 都不会依赖于 (id:0), 因为 id:0 是一个顶级目录项，表示文章的标题。
6. 最后，值得注意的是，目录的依赖关系并不一定是线性的。根据文章内容的不同，某些目录项可能需要同时依赖于多个其他目录项。

Q: 我想写一本以月球为主题的科幻小说《月影之下》，请你生成小说《月影之下》的目录，并详细说明目录项的依赖关系。
A: 
### 分析：
小说属于Shallow类型的文本，level为 0~1，不包含多级目录项。
为了让情节更精彩，我将使用伏笔手法，一些情节会依赖于早期的情节或设定。
### 目录
<JSON>
{
    "content":[
        {"id": 0, "heading": "月影之下", "dep": [-1], "level": 0},
        {"id": 1, "heading": "序言", "dep": [-1], "level": 1},
        {"id": 2, "heading": "神秘的邀请函", "dep": [-1], "level": 1},
        {"id": 3, "heading": "地球上的准备", "dep": [2], "level": 1},
        {"id": 4, "heading": "太空之旅启程", "dep": [3], "level": 1},
        {"id": 5, "heading": "宇宙中的异样", "dep": [4, 2], "level": 1},
        {"id": 6, "heading": "月亮的邀请", "dep": [5], "level": 1},
        {"id": 7, "heading": "落月的秘密", "dep": [6], "level": 1},
        {"id": 8, "heading": "月影村落", "dep": [7], "level": 1},
        {"id": 9, "heading": "月影族人", "dep": [8], "level": 1},
        {"id": 10, "heading": "神秘的传说", "dep": [9,2], "level": 1},
        {"id": 11, "heading": "月亮矿石的秘密", "dep": [10], "level": 1},
        {"id": 12, "heading": "危险的决定", "dep": [11,2], "level": 1},
        {"id": 13, "heading": "再见，地球", "dep": [12], "level": 1},
        {"id": 14, "heading": "归航中的挑战", "dep": [13,2], "level": 1},
        {"id": 15, "heading": "勇敢的牺牲", "dep": [14], "level": 1},
        {"id": 16, "heading": "安全归航", "dep": [15], "level": 1},
        {"id": 17, "heading": "回归之后", "dep": [16], "level": 1},
        {"id": 18, "heading": "新的前景", "dep": [17], "level": 1},
        {"id": 19, "heading": "解开的秘密", "dep": [18,2], "level": 1},
        {"id": 20, "heading": "结语", "dep": [-1], "level": 1}
    ]
}
</JSON>
### 说明：
1. "神秘的邀请函"(id:2)包含了故事的伏笔，这一伏笔在后面的情节中会不断展开和解释，为听众展示了未知的世界和隐藏的秘密。
2. "地球上的准备"(id:3)依赖于id为2的"神秘的邀请函"，在这一章中，主角们接收到了神秘的邀请，开始准备他们的太空旅行。
3. "宇宙中的异样"(id:5)这里的情节不只是依赖于他们已经启程，更是和最初的那份神秘邀请函有所关联，这也是为了揭示伏笔。
4. "神秘的传说"(id:10)这一章节依赖于他们已经进入月影村落和最初的神秘邀请函，传说和邀请函中的秘密有关。
5. "危险的决定"(id:12)，这一章的情节也依赖于神秘的邀请函，那份邀请函让他们面临此刻的决定，也成为了他们内心挣扎的主要原因之一。
6. "归航中的挑战"(id:14)，这个章节的情节是建立在他们即将回地球的情景之上，并且这份挑战和收到的那份神秘邀请函有关。
7. "新的前景"(id:17)和"解开的秘密"(id:18)，这两章的情节建立在归航之后，主角们处理了他们的生活并揭示了他们旅途中的神秘秘密。
8. "结语"(id:20)，总结了这次的旅程，预示了新的开始，它是无依赖的结尾，但是读者需要对全篇的主要内容有大致的了解。

Q: 我想写一则以关于特朗普在2020美国总统大选中落选的Opinion article，标题为《美国大选2020|特朗普落选的三个原因》，请你生成Opinion article的目录，并详细说明目录项的依赖关系。
A:
### 分析：
对于一篇关于特朗普落选的Opinion article，主要内容应包括对特朗普竞选失败的理由的分析。在此，我们设定每个原因（或观点）作为二级目录，三级目录为支持每个观点的详细解释或实例。

### 分析：
Opinion article属于Medium类型的文本，level通常为 0~3。在写作这篇Opinion article时，我认为最大level设置为2更为合适，即：level = 0~2
当我们撰写一篇观点文章时，主要目标是阐明和支持我们的观点。在这篇关于特朗普落选的文章中，3个原因均为大的议论点，而具体的例证和论述则为支撑这些议论点的子点。因此，每一个原因（父目录项）应该依赖于那些用来解释或支持其的详细条目（子目录项）。
### 目录
<JSON>
{
    "content":[
        {"id": 0, "heading": "美国大选2020|特朗普落选的三个原因", "dep": [-1], "level": 0},
        {"id": 1, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 2, "heading": "第一原因：新冠疫情的处理", "dep": [3,4,5], "level": 1},
        {"id": 3, "heading": "新冠疫情的严重性", "dep": [-1], "level": 2},
        {"id": 4, "heading": "特朗普政府的应对措施和问题", "dep": [-1], "level": 2},
        {"id": 5, "heading": "公众对特朗普政府应对疫情的评价", "dep": [-1], "level": 2},
        {"id": 6, "heading": "第二原因：贸易战问题", "dep": [7,8,9], "level": 1},
        {"id": 7, "heading": "特朗普政权实施的贸易政策", "dep": [-1], "level": 2},
        {"id": 8, "heading": "贸易政策带来的影响", "dep": [-1], "level": 2},
        {"id": 9, "heading": "公众对特朗普贸易战的反应", "dep": [-1], "level": 2},
        {"id": 10, "heading": "第三原因：种族问题", "dep": [11,12,13], "level": 1},
        {"id": 11, "heading": "特朗普政府下的种族紧张", "dep": [-1], "level": 2},
        {"id": 12, "heading": "种族问题对选民的影响", "dep": [-1], "level": 2},
        {"id": 13, "heading": "美国公众对特朗普种族问题立场的评价", "dep": [-1], "level": 2},
        {"id": 14, "heading": "结论", "dep": [2,6,10], "level": 1}
    ]
}
</JSON>
### 说明：
1. "引言" (id:1)是文章的开始，没有依赖性。
2. "第一原因：新冠疫情的处理" (id:2) 是父目录项，其内容依赖于下面的三个子目录项 "新冠疫情的严重性" (id:3)， "特朗普政府的应对措施和问题" (id:4) 和 "公众对特朗普政府应对疫情的评价" (id:5)。这三个子目录项都会提供具体的例子和数据以支持 "第一原因" 的观点。写作顺序应该是先写完三个子目录项，再写"第一原因：新冠疫情的处理" (id:2)。
3. "第二原因：贸易战问题" (id:6) 是父目录项，易读性、逻辑性及论证的完整性都严重依赖于其下的三个子目录项，即"特朗普政权实施的贸易政策" (id:7)， "贸易政策带来的影响" (id:8) 和 "公众对特朗普贸易战的反应" (id:9)。这在写作联系凝练、有力的观点时尤其重要。写作顺序应该是先写完三个子目录项，再写"第二原因：贸易战问题" (id:6)。
4. "第三原因：种族问题" (id:10)，作为一个父目录项，其完整性和深度离不开以下三个子目录项："特朗普政府下的种族紧张" (id:11)， "种族问题对选民的影响" (id:12) 和 "美国公众对特朗普种族问题立场的评价" (id:13)。这个目录员要求一种层次分明的写作方式，内容的展开方式应按照子目录项的顺序来进一步支持父目录项的论述。写作顺序应该是先写完三个子目录项，再写"第三原因：种族问题" (id:10)。
5. "结论" (id:14)，作为文章的结束，需要依赖于前面所有的观点或原因，即 "第一原因：新冠疫情的处理" (id:2)， "第二原因：贸易战问题" (id:6)，和 "第三原因：种族问题" (id:10)。在结论中，作者应根据前面论述的所有观点来对问题进行总结，并加以评论或者提出见解。

Q: 我想写一份《阿司匹林在健康志愿者中的药代动力学和药效学研究》。请你生成目录，并详细说明目录项的依赖关系。
A:
"""

fake_history = """<HUMAN>:
目录存储于json数据结构中，例如：
{
        "content":[
                {"id": 0, "heading": "岳阳县水系连通及农村水系综合整治工程建设项目环境影响报告书", "dep": [-1], "level": 0},
                {"id": 1, "heading": "概述", "dep": [-1], "level": 1},
                {"id": 2, "heading": "分析判定相关环保政策", "dep": [-1], "level": 2},
                {"id": 3, "heading": "产业政策相符性分析", "dep": [-1], "level": 3},
                {"id": 4, "heading": "法律法规符合性分析", "dep": [-1], "level": 3},
                {"id": 5, "heading": "与相关规划符合性分析", "dep": [-1], "level": 3},
                {"id": 6, "heading": "项目环评报告书的主要结论", "dep": [12], "level": 2},
                {"id": 7, "heading": "结论与建议", "dep": [-1], "level": 1},
                {"id": 8, "heading": "项目概况", "dep": [-1], "level": 2},
                {"id": 9, "heading": "环境管理", "dep": [3], "level": 3},
                {"id": 10, "heading": "主要环保措施", "dep": [-1], "level": 2},
                {"id": 11, "heading": "环境影响经济损益分析", "dep": [-1], "level": 3},
                {"id": 12, "heading": "环评总结论", "dep": [-1], "level": 3}
        ]
}

各个字段的含义
- "id"：表示每个目录项的唯一标识符，可以用来区别不同的目录项。
- "heading"：表示每个目录项的标题，描述了目录项的内容。
- "dep"：代表当前目录项的依赖项，这是一个数组，包含了当前目录项所依赖或关联的其他目录项的id。"-1"通常表示当前目录项是一个顶级项，也就是说它不依赖任何其他项。例如，id为6的"项目环评报告书的主要结论"这一目录项，它的dep值为[12]，表示它依赖于id为12的"环评总结论"这一目录项。
(注意：任何目录项的 dep 都不会依赖于 (id:0), 因为 (id:0) 是一个顶级目录项，表示文章的标题。)
- "level"：代表目录项的等级或深度。"0"通常表示这是一级目录，"1"表示二级目录，"2"表示三级目录，以此类推。比如"id"为0的目录项的"level"为0, 它是文本的title; "id"为1的目录项的"level"为1, 它是一级标题。这个字段可以帮助我们了解目录的层次结构。

### 目录结构规律
所有的文本都可以按目录深度来分类：
- Shallow：浅层目录结构，level 为[0,1] , 线性叙事，只有1级目录项，不包含多级目录项。。
  - Fiction、News、Opinion articlle
- Medium：多级目录结构,level 为 [0,3]，包含多级目录项。
  - Academic paper、Encyclopedia article
- Deep：深层目录结构 level 为[0,6]，包含深度多级目录项。
  - IT: Software Development Report
  - Medicine: Clinical Study Report
  - Finance: Risk Assessment Report
  - Education: Course Evaluation Report
  - Law: Case Assessment Report
  - Management: Project Management Report
  - Manufacturing: Manufacturing Process Report

### 目录项依赖规则：
1. 在目录结构中，一个目录项可以依赖于一个或者多个其它目录项。这种依赖关系表示写作时需要参考被依赖的文本。
比如在小说中，一个情节的写作需要依赖上一个情节或者更早期的情节。又或者在多级目录文本中，一个更广泛的主题可能依赖于许多更具体的子主题的详细信息。
2. 在浅层目录中（比如小说目录），目录项通常是线性的，下一项的内容大概率会基于上一项的内容。如果存在伏笔手法，则需要基于更初期的情节或者设定。
例如:
    {"id": i-1, "heading": "A", "dep": [i-6], "level": 1},
    {"id": i, "heading": "B", "dep": [i-1], "level": 1},
    {"id": i+1, "heading": "C", "dep": [i], "level": 1},
3. 在多级或者深层目录中（比如分析文章、研究报告等），父目录项（更高级别的目录项）通常依赖于它的子目录项（更详细或者更具体的目录项）。因为在这种情况下，一个大的主题或观点被分解为多个子主题或观点，并且每个子主题或观点都会为父主题或观点提供支持。这符合总-分的写作逻辑。
例如：
    {"id": i, "heading": "A", "dep": [i+1, i+2, i+3], "level": 1},
    {"id": i+1, "heading": "A", "dep": [-1], "level": 1},
    {"id": i+2, "heading": "B", "dep": [-1], "level": 1},
    {"id": i+3, "heading": "C", "dep": [-1], "level": 1},
4. 对于文章的引言和结论部分，它们通常没有依赖，但结论可能需要读者对整个文章的内容有所了解。然而，如果结论是对前面几个关键点的总结，那么它可以视作依赖于那些关键点。
5. 目录项的 dep 都不会依赖于 (id:0), 因为 id:0 是一个顶级目录项，表示文章的标题。
6. 最后，值得注意的是，目录的依赖关系并不一定是线性的。根据文章内容的不同，某些目录项可能需要同时依赖于多个其他目录项。

Q: 我想写一本以月球为主题的科幻小说《月影之下》，请你生成小说《月影之下》的目录，并详细说明目录项的依赖关系。
A: 
### 分析：
小说属于Shallow类型的文本，level为[0,1]，包含1级目录项，不包含多级目录项。
为了让情节更精彩，我将使用伏笔手法，一些情节会依赖于早期的情节或设定。
### 目录
{
    "content":[
        {"id": 0, "heading": "月影之下", "dep": [-1], "level": 0},
        {"id": 1, "heading": "序言", "dep": [-1], "level": 1},
        {"id": 2, "heading": "神秘的邀请函", "dep": [-1], "level": 1},
        {"id": 3, "heading": "地球上的准备", "dep": [2], "level": 1},
        {"id": 4, "heading": "太空之旅启程", "dep": [3], "level": 1},
        {"id": 5, "heading": "宇宙中的异样", "dep": [4, 2], "level": 1},
        {"id": 6, "heading": "月亮的邀请", "dep": [5], "level": 1},
        {"id": 7, "heading": "落月的秘密", "dep": [6], "level": 1},
        {"id": 8, "heading": "月影村落", "dep": [7], "level": 1},
        {"id": 9, "heading": "月影族人", "dep": [8], "level": 1},
        {"id": 10, "heading": "神秘的传说", "dep": [9,2], "level": 1},
        {"id": 11, "heading": "月亮矿石的秘密", "dep": [10], "level": 1},
        {"id": 12, "heading": "危险的决定", "dep": [11,2], "level": 1},
        {"id": 13, "heading": "再见，地球", "dep": [12], "level": 1},
        {"id": 14, "heading": "归航中的挑战", "dep": [13,2], "level": 1},
        {"id": 15, "heading": "勇敢的牺牲", "dep": [14], "level": 1},
        {"id": 16, "heading": "安全归航", "dep": [15], "level": 1},
        {"id": 17, "heading": "回归之后", "dep": [16], "level": 1},
        {"id": 18, "heading": "新的前景", "dep": [17], "level": 1},
        {"id": 19, "heading": "解开的秘密", "dep": [18,2], "level": 1},
        {"id": 20, "heading": "结语", "dep": [-1], "level": 1}
    ]
}
### 说明：
1. "神秘的邀请函"(id:2)包含了故事的伏笔，这一伏笔在后面的情节中会不断展开和解释，为听众展示了未知的世界和隐藏的秘密。
2. "地球上的准备"(id:3)依赖于id为2的"神秘的邀请函"，在这一章中，主角们接收到了神秘的邀请，开始准备他们的太空旅行。
3. "宇宙中的异样"(id:5)这里的情节不只是依赖于他们已经启程，更是和最初的那份神秘邀请函有所关联，这也是为了揭示伏笔。
4. "神秘的传说"(id:10)这一章节依赖于他们已经进入月影村落和最初的神秘邀请函，传说和邀请函中的秘密有关。
5. "危险的决定"(id:12)，这一章的情节也依赖于神秘的邀请函，那份邀请函让他们面临此刻的决定，也成为了他们内心挣扎的主要原因之一。
6. "归航中的挑战"(id:14)，这个章节的情节是建立在他们即将回地球的情景之上，并且这份挑战和收到的那份神秘邀请函有关。
7. "新的前景"(id:17)和"解开的秘密"(id:18)，这两章的情节建立在归航之后，主角们处理了他们的生活并揭示了他们旅途中的神秘秘密。
8. "结语"(id:20)，总结了这次的旅程，预示了新的开始，它是无依赖的结尾，但是读者需要对全篇的主要内容有大致的了解。


Q: 我现在想写一则以关于特朗普在2020美国总统大选中落选的Opinion article，标题为《美国大选2020|特朗普落选的三个原因》，请你生成Opinion article的目录，并详细说明目录项的依赖关系。
A:
---
<ASSISTANT>:
### 分析：
对于一篇关于特朗普落选的Opinion article，主要内容应包括对特朗普竞选失败的理由的分析。在此，我们设定每个原因（或观点）作为二级目录，三级目录为支持每个观点的详细解释或实例。

### 目录
{
    "content":[
        {"id": 0, "heading": "美国大选2020|特朗普落选的三个原因", "dep": [-1], "level": 0},
        {"id": 1, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 2, "heading": "第一原因：新冠疫情的处理", "dep": [-1], "level": 1},
        {"id": 3, "heading": "新冠疫情的严重性", "dep": [2], "level": 2},
        {"id": 4, "heading": "特朗普政府的应对措施和问题", "dep": [2], "level": 2},
        {"id": 5, "heading": "公众对特朗普政府应对疫情的评价", "dep": [2], "level": 2},
        {"id": 6, "heading": "第二原因：贸易战问题", "dep": [-1], "level": 1},
        {"id": 7, "heading": "特朗普政权实施的贸易政策", "dep": [6], "level": 2},
        {"id": 8, "heading": "贸易政策带来的影响", "dep": [6], "level": 2},
        {"id": 9, "heading": "公众对特朗普贸易战的反应", "dep": [6], "level": 2},
        {"id": 10, "heading": "第三原因：种族问题", "dep": [-1], "level": 1},
        {"id": 11, "heading": "特朗普政府下的种族紧张", "dep": [10], "level": 2},
        {"id": 12, "heading": "种族问题对选民的影响", "dep": [10], "level": 2},
        {"id": 13, "heading": "美国公众对特朗普种族问题立场的评价", "dep": [10], "level": 2},
        {"id": 14, "heading": "结论", "dep": [-1], "level": 1}
    ]
}
### 说明：
1. "引言" (id:1) 是文章的开头，对文章进行简要介绍，没有依赖。
2. "新冠疫情的严重性" (id:3)、"特朗普政府的应对措施和问题" (id:4) 和 "公众对特朗普政府应对疫情的评价" (id:5) 都是 "第一原因：新冠疫情的处理" (id:2) 的下级目录，即这三个小标题都是用来支持 "新冠疫情的处理" 这一原因的。
3. 同样，"特朗普政权实施的贸易政策" (id:7)、"贸易政策带来的影响" (id:8) 和 "公众对特朗普贸易战的反应" (id:9) 都是 "第二原因：贸易战问题" (id:6) 的下级目录，即这三个小标题都是用来支持 "贸易战问题" 这一原因的。
4. "特朗普政府下的种族紧张" (id:11)、"种族问题对选民的影响" (id:12) 和 "美国公众对特朗普种族问题立场的评价" (id:13) 都是 " 第三原因：种族问题" (id:10) 的下级目录，即这三个小标题都是用来支持 "种族问题" 这一原因的。
5. "结论" (id:14) 是文章的结尾，总结全文，提出观点，没有依赖。
---
<HUMAN>: 
Q: 不错，但是你要注意到。你这次生成的目录结构深度大于1，说明这是一个多级目录。
不同于小说这样的目录结构为1，线性叙事为主的浅层目录，在多级目录中，应该是父目录项依赖于子目录项的内容，即：总-分结构。具体来说，应该是这样：
    {"id": 10, "heading": "第三原因：种族问题", "dep": [11,12,13], "level": 1},
    {"id": 11, "heading": "特朗普政府下的种族紧张", "dep": [-1], "level": 2},
    {"id": 12, "heading": "种族问题对选民的影响", "dep": [-1], "level": 2},
    {"id": 13, "heading": "美国公众对特朗普种族问题立场的评价", "dep": [-1], "level": 2},
你觉得呢？
A: 
---
<ASSISTANT>:
非常正确，我的回答确实有误。在多级目录中，父目录项应该依赖于子目录项的内容。感谢你的指正。这反映了一种逻辑，即我们在理解一个更大的主题或概念时，需要理解它的各个部分或子主题。你提供的关于"第三原因：种族问题"与它的子目录项的依赖关系就是一个很好的例子。
---
<HUMAN>:
Q: 请你改写目录的dep，适应这条规则，并重新给出`分析`、`目录`和`原因`
A: 
---
<ASSISTANT>:
---
### 分析：
当我们撰写一篇观点文章时，主要目标是阐明和支持我们的观点。在这篇关于特朗普落选的文章中，3个原因均为大的议论点，而具体的例证和论述则为支撑这些议论点的子点。因此，每一个原因（父目录项）应该依赖于那些用来解释或支持其的详细条目（子目录项）。
### 目录
{
    "content":[
        {"id": 0, "heading": "美国大选2020|特朗普落选的三个原因", "dep": [-1], "level": 0},
        {"id": 1, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 2, "heading": "第一原因：新冠疫情的处理", "dep": [3,4,5], "level": 1},
        {"id": 3, "heading": "新冠疫情的严重性", "dep": [-1], "level": 2},
        {"id": 4, "heading": "特朗普政府的应对措施和问题", "dep": [-1], "level": 2},
        {"id": 5, "heading": "公众对特朗普政府应对疫情的评价", "dep": [-1], "level": 2},
        {"id": 6, "heading": "第二原因：贸易战问题", "dep": [7,8,9], "level": 1},
        {"id": 7, "heading": "特朗普政权实施的贸易政策", "dep": [-1], "level": 2},
        {"id": 8, "heading": "贸易政策带来的影响", "dep": [-1], "level": 2},
        {"id": 9, "heading": "公众对特朗普贸易战的反应", "dep": [-1], "level": 2},
        {"id": 10, "heading": "第三原因：种族问题", "dep": [11,12,13], "level": 1},
        {"id": 11, "heading": "特朗普政府下的种族紧张", "dep": [-1], "level": 2},
        {"id": 12, "heading": "种族问题对选民的影响", "dep": [-1], "level": 2},
        {"id": 13, "heading": "美国公众对特朗普种族问题立场的评价", "dep": [-1], "level": 2},
        {"id": 14, "heading": "结论", "dep": [2,6,10], "level": 1}
    ]
}
### 说明：
根据你的反馈，我更改了目录的依赖关系以符合规则。

1. "引言" (id:1)是文章的开始，没有依赖性。
2. "第一原因：新冠疫情的处理" (id:2) 是父目录项，其内容依赖于下面的三个子目录项 "新冠疫情的严重性" (id:3)， "特朗普政府的应对措施和问题" (id:4) 和 "公众对特朗普政府应对疫情的评价" (id:5)。这三个子目录项都会提供具体的例子和数据以支持 "第一原因" 的观点。写作顺序应该是先写完三个子目录项，再写"第一原因：新冠疫情的处理" (id:2)。
3. "第二原因：贸易战问题" (id:6) 是父目录项，易读性、逻辑性及论证的完整性都严重依赖于其下的三个子目录项，即"特朗普政权实施的贸易政策" (id:7)， "贸易政策带来的影响" (id:8) 和 "公众对特朗普贸易战的反应" (id:9)。这在写作联系凝练、有力的观点时尤其重要。写作顺序应该是先写完三个子目录项，再写"第二原因：贸易战问题" (id:6)。
4. "第三原因：种族问题" (id:10)，作为一个父目录项，其完整性和深度离不开以下三个子目录项："特朗普政府下的种族紧张" (id:11)， "种族问题对选民的影响" (id:12) 和 "美国公众对特朗普种族问题立场的评价" (id:13)。这个目录员要求一种层次分明的写作方式，内容的展开方式应按照子目录项的顺序来进一步支持父目录项的论述。写作顺序应该是先写完三个子目录项，再写"第三原因：种族问题" (id:10)。
5. "结论" (id:14)，作为文章的结束，需要依赖于前面所有的观点或原因，即 "第一原因：新冠疫情的处理" (id:2)， "第二原因：贸易战问题" (id:6)，和 "第三原因：种族问题" (id:10)。在结论中，作者应根据前面论述的所有观点来对问题进行总结，并加以评论或者提出见解。
这样，顶层的目录项依赖于更深层次的目录项，反映了文章的主要结构。
---
<Human>:
Q: 不错，能帮我把这条规则明确一下吗？这样我就不用每一次都逐步指出并修正了
A:
"""


fake_result = """
### 分析：
阿司匹林在健康志愿者中的药代动力学和药效学研究，这是一篇科研论文，所属类型应该是Medium，level通常为[0,3]。然而，考虑到药代动力学和药效学研究可能需要更详细的说明，我们采用最大层级为3的目录结构，即level=[0,4]。
这篇论文的主题是研究阿司匹林在健康志愿者体内的药代动力学和药效学行为。其实验内容会包括实验设计、测试方法、数据收集和分析等步骤。在这种情况下，应当严格按照实验的步骤来组织论文结构，由总到分，层层递进。父目录项（更广泛的主题）应依赖于子目录项（更详细或具体的信息）。

### 目录
<JSON>
{
    "content":[
        {"id": 0, "heading": "阿司匹林在健康志愿者中的药代动力学和药效学研究", "dep": [-1], "level": 0},
        {"id": 1, "heading": "摘要", "dep": [-1], "level": 1},
        {"id": 2, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 3, "heading": "材料与方法", "dep": [4,5,6], "level": 1},
        {"id": 4, "heading": "试验设计", "dep": [-1], "level": 2},
        {"id": 5, "heading": "试验材料", "dep": [-1], "level": 2},
        {"id": 6, "heading": "试验方法", "dep": [-1], "level": 2},
        {"id": 7, "heading": "结果", "dep": [8,9,10], "level": 1},
        {"id": 8, "heading": "药代动力学结果", "dep": [-1], "level": 2},
        {"id": 9, "heading": "药效学结果", "dep": [-1], "level": 2},
        {"id": 10, "heading": "副作用和安全性结果","dep": [-1], "level": 2},
        {"id": 11, "heading": "讨论", "dep": [7], "level": 1},
        {"id": 12, "heading": "结论", "dep": [7, 11], "level": 1},
        {"id": 13, "heading": "致谢", "dep": [-1], "level": 1},
        {"id": 14, "heading": "引用文献", "dep": [-1], "level": 1}
    ]
}
</JSON>
### 说明：
1. “摘要”（id:1） 和“引言”（id:2），作为论文的开头，不需要依赖其他部分。
2. "材料与方法"（id:3）这一大章节依赖于其子章节"试验设计"（id:4），"试验材料"（id:5）和"试验方法"（id:6）。这三个子章节的内容为“试验设计”的具体内容。
3. "结果"（id:7）是一个父目录项，依赖于"药代动力学结果"（id:8）,"药效学结果"（id:9）和"副作用和安全性结果"（id:10）这三个子目录项。
4. "讨论"部分（id:11）依赖于“结果”部分（id:7），因为在"讨论"部分需要对"结果"部分做出详细解释和讨论。
5. "结论"（id:12）这个部分则依赖于"结果"（id:7）和"讨论"（id:11）。结论是对研究的最终总结，需要对结果和讨论进行总结。
6. "致谢"（id:13）和"引用文献"（id:14）这两部分不需要依赖于其他部分。
"""

fake_json_str = """
{
    "content":[
        {"id": 0, "heading": "阿司匹林在健康志愿者中的药代动力学和药效学研究", "dep": [-1], "level": 0},
        {"id": 1, "heading": "摘要", "dep": [-1], "level": 1},
        {"id": 2, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 3, "heading": "材料与方法", "dep": [4,5,6], "level": 1},
        {"id": 4, "heading": "试验设计", "dep": [-1], "level": 2},
        {"id": 5, "heading": "试验材料", "dep": [-1], "level": 2},
        {"id": 6, "heading": "试验方法", "dep": [-1], "level": 2},
        {"id": 7, "heading": "结果", "dep": [8,9,10], "level": 1},
        {"id": 8, "heading": "药代动力学结果", "dep": [-1], "level": 2},
        {"id": 9, "heading": "药效学结果", "dep": [-1], "level": 2},
        {"id": 10, "heading": "副作用和安全性结果","dep": [-1], "level": 2},
        {"id": 11, "heading": "讨论", "dep": [7], "level": 1},
        {"id": 12, "heading": "结论", "dep": [7, 11], "level": 1},
        {"id": 13, "heading": "致谢", "dep": [-1], "level": 1},
        {"id": 14, "heading": "引用文献", "dep": [-1], "level": 1}
    ]
}
"""

fake_digest = """从摘要到React组件设计部分的内容总结如下:
本技术报告概述了使用JavaSpring和React技术联合开发云计算平台的方法。报告首先介绍了JavaSpring和React的基础知识及其结合的优势，然后分析了用户需求、系统需求和功能需求，包括数据处理能力、用户界面友好性、扩展性、安全性和可靠性。接着，报告详细讨论了系统架构设计，包括微服务架构、前端后端架构、数据库架构和部署策略。特别指出了Java Spring框架在服务发现、负载均衡、熔断降级和服务网关方面的应用，以及React在组件设计、状态管理和生命周期方法上的重要性。
"""

fake_content = """
{
    "content":[
        {"id": 0, "heading": "基于JavaSprint与React的云计算平台开发技术报告", "dep": [-1], "level": 0},
        {"id": 1, "heading": "摘要", "dep": [-1], "level": 1},
        {"id": 2, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 3, "heading": "需求分析", "dep": [4,5,6], "level": 1},
        {"id": 4, "heading": "用户需求分析", "dep": [-1], "level": 2},
        {"id": 5, "heading": "系统需求分析", "dep": [-1], "level": 2},
        {"id": 6, "heading": "功能需求分析", "dep": [-1], "level": 2},
        {"id": 7, "heading": "系统设计", "dep": [8,9,10,11], "level": 1},
        {"id": 8, "heading": "系统架构设计", "dep": [-1], "level": 2},
        {"id": 9, "heading": "JavaSprint框架应用设计", "dep": [-1], "level": 2},
        {"id": 10, "heading": "React组件设计", "dep": [-1], "level": 2},
        {"id": 11, "heading": "数据库设计", "dep": [-1], "level": 2},
        {"id": 12, "heading": "系统实现", "dep": [13,14,15], "level": 1},
        {"id": 13, "heading": "后端实现", "dep": [-1], "level": 2},
        {"id": 14, "heading": "前端实现", "dep": [-1], "level": 2},
        {"id": 15, "heading": "数据库实现", "dep": [-1], "level": 2},
        {"id": 16, "heading": "系统测试", "dep": [17,18,19], "level": 1},
        {"id": 17, "heading": "集成测试", "dep": [-1], "level": 2},
        {"id": 18, "heading": "性能测试", "dep": [-1], "level": 2},
        {"id": 19, "heading": "用户验收测试", "dep": [-1], "level": 2},
        {"id": 20, "heading": "总结与展望", "dep": [7,12,16], "level": 1}
    ]
}
"""

fake_text = """
## 数据库设计

在开发基于JavaSprint和React的云计算平台时，有效的数据库设计至关重要。以下为该平台的数据库设计内容：

一、**数据库选择**

我们选择MySQL作为主要的关系数据库管理系统(RDBMS)，由于它的高度灵活性以及兼容性，同时考虑到了成本问题。

二、**数据库架构**

我们的数据库架构被划分为三个主要部分：用户，云服务和交易。

- 用户：存储用户信息的表包括用户ID、用户名、密码、电子邮件和角色（用户或管理员）。

- 云服务：这部分将包含与我们提供的云计算服务相关的所有内容。将包含服务ID，服务类型，服务描述，服务成本以及其他相关信息。

- 交易：交易部分将连接用户和云服务部分，用户租用云计算资源将作为交易记录，包含交易ID，用户ID，服务ID，交易时间以及交易价格。

三、**数据库规范化**

为了确保数据库的有效性和准确性，我们采取了数据库规范化的方法。这涉及消除冗余数据，以及在新数据添加到数据库时维持逻辑一致性。

四、**安全性**

我们为数据库实施了一系列安全措施，这包括但不限于: 密码哈希（以防止密码被盗用），在数据库级别上的访问控制，以及防止SQL注入的安全措施。

五、**易用性**

为了方便开发团队，我们使用了ORM（对象关系映射）工具，如Hibernate，来简化数据库操作。同时，我们也采用了JPA（Java持久化API）规范，以实现数据库的简单易用性和可移植性。

六、**扩展性**

考虑到云计算平台可能会快速扩展，我们设计的数据库具有良好的扩展性。可以轻松添加新表，同时不会对现有数据产生影响。

以上，就是我们基于JavaSprint和React的云计算平台的数据库设计。
"""

fake_history2 = """<role>
你是一名写作专家, 正在写作<基于JavaSprint与React的云计算平台开发技术报告>
digest 是你迄今为止所写的内容的总结。
text 是目录项'数据库设计'的正文。
</role>
<rule>
digest 为目录项(0~i)的内容摘要。
text 是 第(i+1)个目录项的的正文。
请你总结text(i+1)的重点信息，并融入到digest(0~i)中，形成新的digest(0~i+1)。在此过程中，应避免直接复制前面的内容，而是通过重新组织来提炼信息，确保摘要的最终长度相对稳定，且随着添加的内容逐渐丰富。
</rule>
<content>
{
    "content":[
        {"id": 0, "heading": "基于JavaSprint与React的云计算平台开发技术报告", "dep": [-1], "level": 0},
        {"id": 1, "heading": "摘要", "dep": [-1], "level": 1},
        {"id": 2, "heading": "引言", "dep": [-1], "level": 1},
        {"id": 3, "heading": "需求分析", "dep": [4,5,6], "level": 1},
        {"id": 4, "heading": "用户需求分析", "dep": [-1], "level": 2},
        {"id": 5, "heading": "系统需求分析", "dep": [-1], "level": 2},
        {"id": 6, "heading": "功能需求分析", "dep": [-1], "level": 2},
        {"id": 7, "heading": "系统设计", "dep": [8,9,10,11], "level": 1},
        {"id": 8, "heading": "系统架构设计", "dep": [-1], "level": 2},
        {"id": 9, "heading": "JavaSprint框架应用设计", "dep": [-1], "level": 2},
        {"id": 10, "heading": "React组件设计", "dep": [-1], "level": 2},
        {"id": 11, "heading": "数据库设计", "dep": [-1], "level": 2},
        {"id": 12, "heading": "系统实现", "dep": [13,14,15], "level": 1},
        {"id": 13, "heading": "后端实现", "dep": [-1], "level": 2},
        {"id": 14, "heading": "前端实现", "dep": [-1], "level": 2},
        {"id": 15, "heading": "数据库实现", "dep": [-1], "level": 2},
        {"id": 16, "heading": "系统测试", "dep": [17,18,19], "level": 1},
        {"id": 17, "heading": "集成测试", "dep": [-1], "level": 2},
        {"id": 18, "heading": "性能测试", "dep": [-1], "level": 2},
        {"id": 19, "heading": "用户验收测试", "dep": [-1], "level": 2},
        {"id": 20, "heading": "总结与展望", "dep": [7,12,16], "level": 1}
    ]
}
说明：
1. "需求分析" (id:3) 是一个父目录项，该部分的内容主要是依赖于 "用户需求分析" (id:4)， "系统需求分析" (id:5)，和 "功能需求分析" (id:6) 这三个子目录项。这三个子目录项为 "需求分析" 提供了详尽的需求信息，以供技术人员进行后续开发。
2. "系统设计" (id:7) 这个父目录项，和它下面的四个子目录项，即 "系统架构设计" (id:8)， "JavaSprint框架应用设计" (id:9)， "React组件设计"(id:10) 和 "数据库设计" (id:11) 有着强烈的依赖关系，这四个部分完成了整个系统的设计工作。
3. "系统实现" (id:12) 是基于系统设计和需求分析的实现，该部分的完整性是依赖于 "后端实现" (id:13)， "前端实现" (id:14)，和 "数据库实现" (id:15) 的。
4. "系统测试" (id:16) 部分，包含了对系统实现的全面测试，这个部分的内容依赖于 "集成测试" (id:17)， "性能测试"(id:18) 和 "用户验收测试" (id:19)。
5. "总结与展望" (id:20) 总结了前面的工作内容并对未来进行展望，它依赖了 "系统设计" (id:7)，"系统实现" (id:12)，和 "系统测试" (id:16)，它们是项目工作的关键环节。

</content>
<text>
## 数据库设计

在开发基于JavaSprint和React的云计算平台时，有效的数据库设计至关重要。以下为该平台的数据库设计内容：

一、**数据库选择**

我们选择MySQL作为主要的关系数据库管理系统(RDBMS)，由于它的高度灵活性以及兼容性，同时考虑到了成本问题。

二、**数据库架构**

我们的数据库架构被划分为三个主要部分：用户，云服务和交易。

- 用户：存储用户信息的表包括用户ID、用户名、密码、电子邮件和角色（用户或管理员）。

- 云服务：这部分将包含与我们提供的云计算服务相关的所有内容。将包含服务ID，服务类型，服务描述，服务成本以及其他相关信息。

- 交易：交易部分将连接用户和云服务部分，用户租用云计算资源将作为交易记录，包含交易ID，用户ID，服务ID，交易时间以及交易价格。

三、**数据库规范化**

为了确保数据库的有效性和准确性，我们采取了数据库规范化的方法。这涉及消除冗余数据，以及在新数据添加到数据库时维持逻辑一致性。

四、**安全性**

我们为数据库实施了一系列安全措施，这包括但不限于: 密码哈希（以防止密码被盗用），在数据库级别上的访问控制，以及防止SQL注入的安全措施。

五、**易用性**

为了方便开发团队，我们使用了ORM（对象关系映射）工具，如Hibernate，来简化数据库操作。同时，我们也采用了JPA（Java持久化API）规范，以实现数据库的简单易用性和可移植性。

六、**扩展性**

考虑到云计算平台可能会快速扩展，我们设计的数据库具有良好的扩展性。可以轻松添加新表，同时不会对现有数据产生影响。

以上，就是我们基于JavaSprint和React的云计算平台的数据库设计。
</text>
<digest>
从摘要到React组件设计部分的内容总结如下:
本技术报告概述了使用JavaSpring和React技术联合开发云计算平台的方法。报告首先介绍了JavaSpring和React的基础知识及其结合的优势，然后分析了用户需求、系统需求和功能需求，包括数据处理能力、用户界面友好性、扩展性、安全性和可靠性。接着，报告详细讨论了系统架构设计，包括微服务架构、前端后端架构、数据库架构和部署策略。特别指出了Java Spring框架在服务发现、负载均衡、熔断降级和服务网关方面的应用，以及React在组件设计、状态管理和生命周期方法上的重要性。
</digest>
<task>
Q: 请你根据digest和text，更新digest。
A: 
报告总结了基于JavaSpring和React开发云计算平台的过程，包括从用户需求、系统和功能需求的分析，到系统架构设计，其中详细叙述了Java Spring框架和React在这个过程中的关键角色。在数据库设计部分，我们选择了MySQL作为主要的数据库管理系统，并且布局了一个分为用户、云服务、交易三个主要部分的数据库架构。为了保证数据库的准确性和安全性，我们进行了数据库规范化，并实施了一系列的安全措施，如密码哈希和防止SQL注入。另外，我们还使用了ORM工具，如Hibernate，以及采用了JPA规范，以实现数据库的简易使用和可迁移性。最后，我们的数据库设计留有足够的扩展性，以适应云计算平台快速扩展的需求。
"""




# ----------- prompt for GPT4 to generate data ----------- 
prompt1 = """
<rule>
All texts can be classified based on their directory depth:
- Shallow: The directory structure is relatively shallow, with levels ranging from 0 to 1. It involves linear narratives with only one level of directory items, excluding multi-level directory items.
    - Fiction
    - News
    - Opinion articles
- Medium: The directory structure has a moderate depth, with levels ranging from 0 to 3, including multi-level directory items.
    - Academic papers
    - Encyclopedia articles
- Deep: The directory structure is very deep, with levels ranging from 0 to 6, including deeply nested directory items.
    - IT: Software Development Report
    - Medicine: Clinical Study Report
    - Finance: Risk Assessment Report
    - Education: Course Evaluation Report
    - Law: Case Assessment Report
    - Management: Project Management Report
    - Manufacturing: Manufacturing Process Report
</rule>
<task>
Q: I have an AI algorithm that can generate a directory based on title. Can you generate some fake titles for me based on the rule above?
"""




