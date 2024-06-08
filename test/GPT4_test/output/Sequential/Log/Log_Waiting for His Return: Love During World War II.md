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
Q: I want to write one Romance Fiction, titled "Waiting for His Return: Love During World War II". Please generate the table of content for me.
A:
Based on the genre of your book, "Romance Fiction," the directory structure falls under the "Shallow" category, with levels ranging from 0 to 1. Here is the table of contents for "Waiting for His Return: Love During World War II":

<JSON>
{
    "content": [
        {"id": 0, "heading": "Waiting for His Return: Love During World War II", "level": 0},
        {"id": 1, "heading": "Prologue: Before the War", "level": 1},
        {"id": 2, "heading": "Parting Ways", "level": 1},
        {"id": 3, "heading": "Letters from the Front", "level": 1},
        {"id": 4, "heading": "Life on the Home Front", "level": 1},
        {"id": 5, "heading": "The Promise", "level": 1},
        {"id": 6, "heading": "Uncertain Times", "level": 1},
        {"id": 7, "heading": "News of Battle", "level": 1},
        {"id": 8, "heading": "Enduring Hope", "level": 1},
        {"id": 9, "heading": "The Long Wait", "level": 1},
        {"id": 10, "heading": "Reunion", "level": 1},
        {"id": 11, "heading": "Epilogue: A New Beginning", "level": 1}
    ]
}
</JSON>

---- prompt_log for write_one_round of heading: `Prologue: Before the War` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Prologue: Before the War` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Prologue: Before the War` based on the content.
A:


---- prompt_log for write_one_round of heading: `Parting Ways` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Parting Ways` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Parting Ways` based on the content.
A:


---- prompt_log for write_one_round of heading: `Letters from the Front` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Letters from the Front` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Letters from the Front` based on the content.
A:


---- prompt_log for write_one_round of heading: `Life on the Home Front` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Life on the Home Front` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Life on the Home Front` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Promise` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Promise` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Promise` based on the content.
A:


---- prompt_log for write_one_round of heading: `Uncertain Times` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Uncertain Times` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Uncertain Times` based on the content.
A:


---- prompt_log for write_one_round of heading: `News of Battle` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `News of Battle` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `News of Battle` based on the content.
A:


---- prompt_log for write_one_round of heading: `Enduring Hope` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Enduring Hope` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Enduring Hope` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Long Wait` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Long Wait` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Long Wait` based on the content.
A:


---- prompt_log for write_one_round of heading: `Reunion` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Reunion` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Reunion` based on the content.
A:


---- prompt_log for write_one_round of heading: `Epilogue: A New Beginning` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Epilogue: A New Beginning` of the article `<Waiting for His Return: Love During World War II>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Waiting for His Return: Love During World War II, "level": 0},
		{"id": 1, "heading": "Prologue: Before the War, "level": 1},
		{"id": 2, "heading": "Parting Ways, "level": 1},
		{"id": 3, "heading": "Letters from the Front, "level": 1},
		{"id": 4, "heading": "Life on the Home Front, "level": 1},
		{"id": 5, "heading": "The Promise, "level": 1},
		{"id": 6, "heading": "Uncertain Times, "level": 1},
		{"id": 7, "heading": "News of Battle, "level": 1},
		{"id": 8, "heading": "Enduring Hope, "level": 1},
		{"id": 9, "heading": "The Long Wait, "level": 1},
		{"id": 10, "heading": "Reunion, "level": 1},
		{"id": 11, "heading": "Epilogue: A New Beginning, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Epilogue: A New Beginning` based on the content.
A:


