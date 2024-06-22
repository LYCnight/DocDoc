---- prompt_log for contentExpert ----

The directory is stored in a JSON data structure and encapsulated within <JSON></JSON>, for example:
<JSON>
{
    "content": [
        {"id": 0, "heading": "Environmental Impact Assessment Report on the Construction Project of Comprehensive Treatment of Water System Connection and Rural Water System in Yueyang County", "level": 0},
        {"id": 1, "heading": "Overview", "level": 1},
        {"id": 2, "heading": "Analysis and Judgment of Relevant Environmental Protection Policies", "level": 2},
        {"id": 3, "heading": "Analysis of Consistency with Industrial Policies", "level": 3},
        {"id": 4, "heading": "Analysis of Compliance with Laws and Regulations", "level": 3},
        {"id": 5, "heading": "Analysis of Consistency with Relevant Plans", "level": 3},
        {"id": 6, "heading": "Main Conclusions of the Project's Environmental Impact Assessment Report", "level": 2},
        {"id": 7, "heading": "Conclusions and Recommendations", "level": 1},
        {"id": 8, "heading": "Project Overview", "level": 2},
        {"id": 9, "heading": "Environmental Management", "level": 3},
        {"id": 10, "heading": "Main Environmental Protection Measures", "level": 2},
        {"id": 11, "heading": "Economic Analysis of Environmental Impacts", "level": 3},
        {"id": 12, "heading": "Summary of Environmental Impact Assessment", "level": 3}
    ]
}
</JSON>

### Meaning of Each Field:
- "id": Represents the unique identifier of each directory item, used to distinguish between different directory items.
- "heading": Represents the title of each directory item, describing its content.
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

### Examples: 
Q: I want to write a science fiction novel with the theme of the moon titled "Under the Moonlight." Could you generate the table of contents for the novel "Under the Moonlight"?
A:
-- Analysis:
The novel falls under the Shallow type of text, with levels ranging from 0 to 1.
-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "Under the Moonlight", "level": 0},
        {"id": 1, "heading": "Prologue", "level": 1},
        {"id": 2, "heading": "The Mysterious Invitation", "level": 1},
        {"id": 3, "heading": "Preparation on Earth", "level": 1},
        {"id": 4, "heading": "Embarking on the Space Journey", "level": 1},
        {"id": 5, "heading": "Anomalies in Space", "level": 1},
        {"id": 6, "heading": "The Moon's Invitation", "level": 1},
        {"id": 7, "heading": "Secrets of the Falling Moon", "level": 1},
        {"id": 8, "heading": "Moonshadow Village", "level": 1},
        {"id": 9, "heading": "Moonshadow Tribe", "level": 1},
        {"id": 10, "heading": "Mysterious Legends", "level": 1},
        {"id": 11, "heading": "The Secret of Moon Ore", "level": 1},
        {"id": 12, "heading": "Dangerous Decision", "level": 1},
        {"id": 13, "heading": "Farewell, Earth", "level": 1},
        {"id": 14, "heading": "Challenges During Return Journey", "level": 1},
        {"id": 15, "heading": "Brave Sacrifice", "level": 1},
        {"id": 16, "heading": "Safe Return", "level": 1},
        {"id": 17, "heading": "After the Return", "level": 1},
        {"id": 18, "heading": "New Horizons", "level": 1},
        {"id": 19, "heading": "Unveiling Secrets", "level": 1},
        {"id": 20, "heading": "Conclusion", "level": 1}
    ]
}
</JSON>

Q: I want to write an opinion article about Trump's defeat in the 2020 US presidential election, titled "2020 US Election | Three Reasons for Trump's Defeat." Please generate the table of contents for me.
A:
-- Analysis:
Opinion articles belong to the Medium category of text, with levels typically ranging from 0 to 3. When writing this opinion article, I believe setting the maximum level to 2 is more appropriate, i.e., level = 0~2. When composing an opinion article, the main goal is to elucidate and support our viewpoints. In this article about Trump's defeat, all three reasons are major points of discussion, while specific examples and arguments serve as sub-points that support these major points. Therefore, each reason (parent entry) should depend on the detailed items used to explain or support it (child entries).
-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "2020 US Election | Three Reasons for Trump's Defeat", "level": 0},
        {"id": 1, "heading": "Introduction", "level": 1},
        {"id": 2, "heading": "First Reason: Handling of the COVID-19 Pandemic", "level": 1},
        {"id": 3, "heading": "Severity of the COVID-19 Pandemic", "level": 2},
        {"id": 4, "heading": "Trump Administration's Response Measures and Issues", "level": 2},
        {"id": 5, "heading": "Public Perception of the Trump Administration's Handling of the Pandemic", "level": 2},
        {"id": 6, "heading": "Second Reason: Trade War Issues", "level": 1},
        {"id": 7, "heading": "Trade Policies Implemented by the Trump Administration", "level": 2},
        {"id": 8, "heading": "Impact of Trade Policies", "level": 2},
        {"id": 9, "heading": "Public Reaction to Trump's Trade War", "level": 2},
        {"id": 10, "heading": "Third Reason: Racial Issues", "level": 1},
        {"id": 11, "heading": "Racial Tensions under the Trump Administration", "level": 2},
        {"id": 12, "heading": "Impact of Racial Issues on Voters", "level": 2},
        {"id": 13, "heading": "Public Perception of Trump's Stance on Racial Issues", "level": 2},
        {"id": 14, "heading": "Conclusion", "level": 1}
    ]
}
</JSON>


### Attention:
1. Please wrap your table of contents within <JSON></JSON> tags. 
2. Make sure your json format is correct

### Task:
Q: I want to write one Sociology Paper, titled "The Evolution of Social Norms: A Comparative Analysis". Please generate the table of content for me.
A:
-- Analysis:
A sociology paper typically falls into the Medium category of text, with levels typically ranging from 0 to 3. This structure allows the inclusion of a comprehensive abstract, literature review, methodology, analysis, and conclusions. Particular sections may contain sub-sections for in-depth discussion.

-- Directory:
<JSON>
{
    "content": [
        {"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis", "level": 0},
        {"id": 1, "heading": "Abstract", "level": 1},
        {"id": 2, "heading": "Introduction", "level": 1},
        {"id": 3, "heading": "Literature Review", "level": 1},
        {"id": 4, "heading": "Definition of Social Norms", "level": 2},
        {"id": 5, "heading": "Historical Evolution of Social Norms", "level": 2},
        {"id": 6, "heading": "Comparative Studies on Social Norms", "level": 2},
        {"id": 7, "heading": "Methodology", "level": 1},
        {"id": 8, "heading": "Research Design", "level": 2},
        {"id": 9, "heading": "Data Collection Methods", "level": 2},
        {"id": 10, "heading": "Data Analysis Techniques", "level": 2},
        {"id": 11, "heading": "Results and Discussion", "level": 1},
        {"id": 12, "heading": "Findings from Comparative Analysis", "level": 2},
        {"id": 13, "heading": "Impact of Social Norms on Society", "level": 2},
        {"id": 14, "heading": "Case Studies", "level": 2},
        {"id": 15, "heading": "Conclusion", "level": 1},
        {"id": 16, "heading": "Summary of Findings", "level": 2},
        {"id": 17, "heading": "Implications for Future Research", "level": 2},
        {"id": 18, "heading": "References", "level": 1},
        {"id": 19, "heading": "Appendix", "level": 1}
    ]
}
</JSON>

---- prompt_log for write_one_round of heading: `Abstract` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Abstract` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Abstract` based on the content.
A:


---- prompt_log for write_one_round of heading: `Introduction` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Introduction` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Introduction` based on the content.
A:


---- prompt_log for write_one_round of heading: `Literature Review` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Literature Review` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Literature Review` based on the content.
A:


---- prompt_log for write_one_round of heading: `Definition of Social Norms` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Definition of Social Norms` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Definition of Social Norms` based on the content.
A:


---- prompt_log for write_one_round of heading: `Historical Evolution of Social Norms` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Historical Evolution of Social Norms` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Historical Evolution of Social Norms` based on the content.
A:


---- prompt_log for write_one_round of heading: `Comparative Studies on Social Norms` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Comparative Studies on Social Norms` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Comparative Studies on Social Norms` based on the content.
A:


---- prompt_log for write_one_round of heading: `Methodology` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Methodology` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Methodology` based on the content.
A:


---- prompt_log for write_one_round of heading: `Research Design` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Research Design` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Research Design` based on the content.
A:


---- prompt_log for write_one_round of heading: `Data Collection Methods` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Data Collection Methods` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Data Collection Methods` based on the content.
A:


---- prompt_log for write_one_round of heading: `Data Analysis Techniques` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Data Analysis Techniques` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Data Analysis Techniques` based on the content.
A:


---- prompt_log for write_one_round of heading: `Results and Discussion` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Results and Discussion` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Results and Discussion` based on the content.
A:


---- prompt_log for write_one_round of heading: `Findings from Comparative Analysis` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Findings from Comparative Analysis` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Findings from Comparative Analysis` based on the content.
A:


---- prompt_log for write_one_round of heading: `Impact of Social Norms on Society` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Impact of Social Norms on Society` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Impact of Social Norms on Society` based on the content.
A:


---- prompt_log for write_one_round of heading: `Case Studies` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Case Studies` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Case Studies` based on the content.
A:


---- prompt_log for write_one_round of heading: `Conclusion` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Conclusion` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Conclusion` based on the content.
A:


---- prompt_log for write_one_round of heading: `Summary of Findings` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Summary of Findings` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Summary of Findings` based on the content.
A:


---- prompt_log for write_one_round of heading: `Implications for Future Research` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Implications for Future Research` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Implications for Future Research` based on the content.
A:


---- prompt_log for write_one_round of heading: `References` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `References` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `References` based on the content.
A:


---- prompt_log for write_one_round of heading: `Appendix` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Appendix` of the article `<The Evolution of Social Norms: A Comparative Analysis>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
3. You can use markdown to draw some tables or stick paper when needed.
4. Don't write anything unrelevant, e.g. "I hope you enjoy this! Let me know if there's anything else you'd like to add or change."
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "The Evolution of Social Norms: A Comparative Analysis, "level": 0},
		{"id": 1, "heading": "Abstract, "level": 1},
		{"id": 2, "heading": "Introduction, "level": 1},
		{"id": 3, "heading": "Literature Review, "level": 1},
		{"id": 4, "heading": "Definition of Social Norms, "level": 2},
		{"id": 5, "heading": "Historical Evolution of Social Norms, "level": 2},
		{"id": 6, "heading": "Comparative Studies on Social Norms, "level": 2},
		{"id": 7, "heading": "Methodology, "level": 1},
		{"id": 8, "heading": "Research Design, "level": 2},
		{"id": 9, "heading": "Data Collection Methods, "level": 2},
		{"id": 10, "heading": "Data Analysis Techniques, "level": 2},
		{"id": 11, "heading": "Results and Discussion, "level": 1},
		{"id": 12, "heading": "Findings from Comparative Analysis, "level": 2},
		{"id": 13, "heading": "Impact of Social Norms on Society, "level": 2},
		{"id": 14, "heading": "Case Studies, "level": 2},
		{"id": 15, "heading": "Conclusion, "level": 1},
		{"id": 16, "heading": "Summary of Findings, "level": 2},
		{"id": 17, "heading": "Implications for Future Research, "level": 2},
		{"id": 18, "heading": "References, "level": 1},
		{"id": 19, "heading": "Appendix, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Appendix` based on the content.
A:


