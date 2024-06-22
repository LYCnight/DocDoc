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
Q: I want to write one History Textbook, titled "The Comprehensive Guide to World History". Please generate the table of content for me.
A:
-- Analysis:
A history textbook typically falls under the Medium category of text, with levels ranging from 0 to 3. This allows for a structured and detailed presentation of historical events, themes, and analyses.

-- Directory:
<JSON>
{
    "content":[
        {"id": 0, "heading": "The Comprehensive Guide to World History", "level": 0},
        {"id": 1, "heading": "Introduction", "level": 1},
        {"id": 2, "heading": "Ancient Civilizations", "level": 1},
        {"id": 3, "heading": "Mesopotamia", "level": 2},
        {"id": 4, "heading": "Ancient Egypt", "level": 2},
        {"id": 5, "heading": "Indus Valley Civilization", "level": 2},
        {"id": 6, "heading": "Ancient China", "level": 2},
        {"id": 7, "heading": "Classical Antiquity", "level": 1},
        {"id": 8, "heading": "Ancient Greece", "level": 2},
        {"id": 9, "heading": "The Roman Empire", "level": 2},
        {"id": 10, "heading": "The Middle Ages", "level": 1},
        {"id": 11, "heading": "Feudal Europe", "level": 2},
        {"id": 12, "heading": "The Byzantine Empire", "level": 2},
        {"id": 13, "heading": "The Islamic Golden Age", "level": 2},
        {"id": 14, "heading": "The Renaissance", "level": 1},
        {"id": 15, "heading": "Origins and Key Figures", "level": 2},
        {"id": 16, "heading": "Cultural and Scientific Advancements", "level": 2},
        {"id": 17, "heading": "The Age of Exploration", "level": 1},
        {"id": 18, "heading": "Major Explorers", "level": 2},
        {"id": 19, "heading": "Impact on Indigenous Cultures", "level": 2},
        {"id": 20, "heading": "The Modern Era", "level": 1},
        {"id": 21, "heading": "The Industrial Revolution", "level": 2},
        {"id": 22, "heading": "World Wars I and II", "level": 2},
        {"id": 23, "heading": "The Cold War", "level": 2},
        {"id": 24, "heading": "Contemporary History", "level": 1},
        {"id": 25, "heading": "Globalization", "level": 2},
        {"id": 26, "heading": "Technological Advancements", "level": 2},
        {"id": 27, "heading": "Major Political Movements", "level": 2},
        {"id": 28, "heading": "Conclusion", "level": 1}
    ]
}
</JSON>

---- prompt_log for write_one_round of heading: `Introduction` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Introduction` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Introduction` based on the content.
A:


---- prompt_log for write_one_round of heading: `Ancient Civilizations` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Ancient Civilizations` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Ancient Civilizations` based on the content.
A:


---- prompt_log for write_one_round of heading: `Mesopotamia` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Mesopotamia` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Mesopotamia` based on the content.
A:


---- prompt_log for write_one_round of heading: `Ancient Egypt` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Ancient Egypt` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Ancient Egypt` based on the content.
A:


---- prompt_log for write_one_round of heading: `Indus Valley Civilization` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Indus Valley Civilization` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Indus Valley Civilization` based on the content.
A:


---- prompt_log for write_one_round of heading: `Ancient China` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Ancient China` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Ancient China` based on the content.
A:


---- prompt_log for write_one_round of heading: `Classical Antiquity` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Classical Antiquity` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Classical Antiquity` based on the content.
A:


---- prompt_log for write_one_round of heading: `Ancient Greece` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Ancient Greece` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Ancient Greece` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Roman Empire` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Roman Empire` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Roman Empire` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Middle Ages` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Middle Ages` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Middle Ages` based on the content.
A:


---- prompt_log for write_one_round of heading: `Feudal Europe` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Feudal Europe` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Feudal Europe` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Byzantine Empire` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Byzantine Empire` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Byzantine Empire` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Islamic Golden Age` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Islamic Golden Age` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Islamic Golden Age` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Renaissance` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Renaissance` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Renaissance` based on the content.
A:


---- prompt_log for write_one_round of heading: `Origins and Key Figures` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Origins and Key Figures` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Origins and Key Figures` based on the content.
A:


---- prompt_log for write_one_round of heading: `Cultural and Scientific Advancements` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Cultural and Scientific Advancements` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Cultural and Scientific Advancements` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Age of Exploration` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Age of Exploration` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Age of Exploration` based on the content.
A:


---- prompt_log for write_one_round of heading: `Major Explorers` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Major Explorers` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Major Explorers` based on the content.
A:


---- prompt_log for write_one_round of heading: `Impact on Indigenous Cultures` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Impact on Indigenous Cultures` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Impact on Indigenous Cultures` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Modern Era` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Modern Era` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Modern Era` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Industrial Revolution` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Industrial Revolution` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Industrial Revolution` based on the content.
A:


---- prompt_log for write_one_round of heading: `World Wars I and II` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `World Wars I and II` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `World Wars I and II` based on the content.
A:


---- prompt_log for write_one_round of heading: `The Cold War` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `The Cold War` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `The Cold War` based on the content.
A:


---- prompt_log for write_one_round of heading: `Contemporary History` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Contemporary History` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Contemporary History` based on the content.
A:


---- prompt_log for write_one_round of heading: `Globalization` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Globalization` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Globalization` based on the content.
A:


---- prompt_log for write_one_round of heading: `Technological Advancements` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Technological Advancements` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Technological Advancements` based on the content.
A:


---- prompt_log for write_one_round of heading: `Major Political Movements` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Major Political Movements` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Major Political Movements` based on the content.
A:


---- prompt_log for write_one_round of heading: `Conclusion` ----

<role>
You are a writing expert.
</role>
<rule>
You are writing the body content for the table of contents item `Conclusion` of the article `<The Comprehensive Guide to World History>`.
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
		{"id": 0, "heading": "The Comprehensive Guide to World History, "level": 0},
		{"id": 1, "heading": "Introduction, "level": 1},
		{"id": 2, "heading": "Ancient Civilizations, "level": 1},
		{"id": 3, "heading": "Mesopotamia, "level": 2},
		{"id": 4, "heading": "Ancient Egypt, "level": 2},
		{"id": 5, "heading": "Indus Valley Civilization, "level": 2},
		{"id": 6, "heading": "Ancient China, "level": 2},
		{"id": 7, "heading": "Classical Antiquity, "level": 1},
		{"id": 8, "heading": "Ancient Greece, "level": 2},
		{"id": 9, "heading": "The Roman Empire, "level": 2},
		{"id": 10, "heading": "The Middle Ages, "level": 1},
		{"id": 11, "heading": "Feudal Europe, "level": 2},
		{"id": 12, "heading": "The Byzantine Empire, "level": 2},
		{"id": 13, "heading": "The Islamic Golden Age, "level": 2},
		{"id": 14, "heading": "The Renaissance, "level": 1},
		{"id": 15, "heading": "Origins and Key Figures, "level": 2},
		{"id": 16, "heading": "Cultural and Scientific Advancements, "level": 2},
		{"id": 17, "heading": "The Age of Exploration, "level": 1},
		{"id": 18, "heading": "Major Explorers, "level": 2},
		{"id": 19, "heading": "Impact on Indigenous Cultures, "level": 2},
		{"id": 20, "heading": "The Modern Era, "level": 1},
		{"id": 21, "heading": "The Industrial Revolution, "level": 2},
		{"id": 22, "heading": "World Wars I and II, "level": 2},
		{"id": 23, "heading": "The Cold War, "level": 2},
		{"id": 24, "heading": "Contemporary History, "level": 1},
		{"id": 25, "heading": "Globalization, "level": 2},
		{"id": 26, "heading": "Technological Advancements, "level": 2},
		{"id": 27, "heading": "Major Political Movements, "level": 2},
		{"id": 28, "heading": "Conclusion, "level": 1}
	]
}
</content>
<task>
Q: Please write the body content for the table of contents item `Conclusion` based on the content.
A:


