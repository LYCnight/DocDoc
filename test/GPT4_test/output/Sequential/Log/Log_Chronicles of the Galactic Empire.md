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
Q: I want to write one Science Fiction, titled "Chronicles of the Galactic Empire". Please generate the table of content for me.
A:
Based on the genre and title provided, the text "Chronicles of the Galactic Empire" falls under the Shallow category, with levels ranging from 0 to 1. Here's the table of contents for your science fiction novel:

<JSON>
{
    "content": [
        {"id": 0, "heading": "Chronicles of the Galactic Empire", "level": 0},
        {"id": 1, "heading": "The Dawn of Empire", "level": 1},
        {"id": 2, "heading": "Rise of the Rebel Stars", "level": 1},
        {"id": 3, "heading": "The Great Space Battles", "level": 1},
        {"id": 4, "heading": "The Emperor's Vision", "level": 1},
        {"id": 5, "heading": "Rebellion in the Outer Sector", "level": 1},
        {"id": 6, "heading": "The Fall of the Titan Moons", "level": 1},
        {"id": 7, "heading": "The Galactic Council", "level": 1},
        {"id": 8, "heading": "Secrets of the Ancient Aliens", "level": 1},
        {"id": 9, "heading": "The Last Stand", "level": 1},
        {"id": 10, "heading": "A New Hope", "level": 1},
        {"id": 11, "heading": "Epilogue: The Future of the Empire", "level": 1}
    ]
}
</JSON>

---- prompt_log for write_one_round of heading: `The Dawn of Empire` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Dawn of Empire` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "The Dawn of Empire, "level": 1},
		{"id": 2, "heading": "Rise of the Rebel Stars, "level": 1},
		{"id": 3, "heading": "The Great Space Battles, "level": 1},
		{"id": 4, "heading": "The Emperor's Vision, "level": 1},
		{"id": 5, "heading": "Rebellion in the Outer Sector, "level": 1},
		{"id": 6, "heading": "The Fall of the Titan Moons, "level": 1},
		{"id": 7, "heading": "The Galactic Council, "level": 1},
		{"id": 8, "heading": "Secrets of the Ancient Aliens, "level": 1},
		{"id": 9, "heading": "The Last Stand, "level": 1},
		{"id": 10, "heading": "A New Hope, "level": 1},
		{"id": 11, "heading": "Epilogue: The Future of the Empire, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Dawn of Empire` based on the content.
A:


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
Q: I want to write one Science Fiction, titled "Chronicles of the Galactic Empire". Please generate the table of content for me.
A:
-- Analysis:
The novel "Chronicles of the Galactic Empire" falls under the Shallow type of text, with levels ranging from 0 to 1.

-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "Chronicles of the Galactic Empire", "level": 0},
        {"id": 1, "heading": "Prologue", "level": 1},
        {"id": 2, "heading": "The Rise of the Empire", "level": 1},
        {"id": 3, "heading": "The Galactic Senate", "level": 1},
        {"id": 4, "heading": "Rebellion on the Outer Rim", "level": 1},
        {"id": 5, "heading": "The Emperor's Secret", "level": 1},
        {"id": 6, "heading": "The Battle of Orion", "level": 1},
        {"id": 7, "heading": "Allies and Enemies", "level": 1},
        {"id": 8, "heading": "The Fall of the Capital", "level": 1},
        {"id": 9, "heading": "The Last Stand", "level": 1},
        {"id": 10, "heading": "A New Dawn", "level": 1},
        {"id": 11, "heading": "Epilogue", "level": 1}
    ]
}
</JSON>

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
Q: I want to write one Science Fiction, titled "Chronicles of the Galactic Empire". Please generate the table of content for me.
A:
-- Analysis:
This science fiction novel will likely fall under the Shallow type of text, with levels ranging from 0 to 1, as it typically includes linear narrative structures.

-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "Chronicles of the Galactic Empire", "level": 0},
        {"id": 1, "heading": "Prologue", "level": 1},
        {"id": 2, "heading": "The Fall of Earth", "level": 1},
        {"id": 3, "heading": "Escape to the Stars", "level": 1},
        {"id": 4, "heading": "A New Home", "level": 1},
        {"id": 5, "heading": "Rise of the Empire", "level": 1},
        {"id": 6, "heading": "Interstellar Politics", "level": 1},
        {"id": 7, "heading": "Galactic Wars", "level": 1},
        {"id": 8, "heading": "The Rebel Alliance", "level": 1},
        {"id": 9, "heading": "Secrets of the Ancients", "level": 1},
        {"id": 10, "heading": "The Battle for the Throne", "level": 1},
        {"id": 11, "heading": "Voyage to the Unknown", "level": 1},
        {"id": 12, "heading": "The Final Frontier", "level": 1},
        {"id": 13, "heading": "Epilogue", "level": 1}
    ]
}
</JSON>

---- prompt_log for write_one_round of heading: `Prologue` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Prologue` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Prologue` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Fall of Earth` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Fall of Earth` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Fall of Earth` based on the content.
A:


---- prompt_log for write_one_round of heading: `Escape to the Stars` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Escape to the Stars` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Escape to the Stars` based on the content.
A:


---- prompt_log for write_one_round of heading: `A New Home` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `A New Home` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `A New Home` based on the content.
A:


---- prompt_log for write_one_round of heading: `Rise of the Empire` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Rise of the Empire` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Rise of the Empire` based on the content.
A:


---- prompt_log for write_one_round of heading: `Interstellar Politics` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Interstellar Politics` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Interstellar Politics` based on the content.
A:


---- prompt_log for write_one_round of heading: `Galactic Wars` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Galactic Wars` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Galactic Wars` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Rebel Alliance` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Rebel Alliance` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Rebel Alliance` based on the content.
A:


---- prompt_log for write_one_round of heading: `Secrets of the Ancients` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Secrets of the Ancients` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Secrets of the Ancients` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Battle for the Throne` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Battle for the Throne` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Battle for the Throne` based on the content.
A:


---- prompt_log for write_one_round of heading: `Voyage to the Unknown` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Voyage to the Unknown` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Voyage to the Unknown` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Final Frontier` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Final Frontier` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Final Frontier` based on the content.
A:


---- prompt_log for write_one_round of heading: `Epilogue` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Epilogue` of the article `<Chronicles of the Galactic Empire>`.
content: This is the table of contents of the article.
</rule>
<constraints>
1. You can only return text in markdown format.
2. The body content you return must not contain markdown heading commands such as #, ##, ###, ####, #####, ######.
</constraints>
<content>
{
	"content":[
		{"id": 0, "heading": "Chronicles of the Galactic Empire, "level": 0},
		{"id": 1, "heading": "Prologue, "level": 1},
		{"id": 2, "heading": "The Fall of Earth, "level": 1},
		{"id": 3, "heading": "Escape to the Stars, "level": 1},
		{"id": 4, "heading": "A New Home, "level": 1},
		{"id": 5, "heading": "Rise of the Empire, "level": 1},
		{"id": 6, "heading": "Interstellar Politics, "level": 1},
		{"id": 7, "heading": "Galactic Wars, "level": 1},
		{"id": 8, "heading": "The Rebel Alliance, "level": 1},
		{"id": 9, "heading": "Secrets of the Ancients, "level": 1},
		{"id": 10, "heading": "The Battle for the Throne, "level": 1},
		{"id": 11, "heading": "Voyage to the Unknown, "level": 1},
		{"id": 12, "heading": "The Final Frontier, "level": 1},
		{"id": 13, "heading": "Epilogue, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Epilogue` based on the content.
A:


