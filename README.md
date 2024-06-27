## 1. Introduction
Human writing is inherently non-autoregressive, involving planning, editing, and maintaining hierarchical structures. Based on this philosophy, we present DocDoc, a general open-ended long text generation framework that simulates the human writing process.

Our framework begins by generating a content tree with dependencies, representing the hierarchical structure of the text. These dependencies indicate reference relationships between sections, ensuring coherence and structure. By traversing the content tree in post-order, DocDoc mimics the human approach of developing detailed parts before integrating them into the whole.

![fig](D:\论文相关存档\EMNLP 2024\DocDoc\assets\fig.png)



## 2. Dataset

### Type of long text

Based on the hierarchical structure of the table of contents, long texts can be categorized into three types:

- **Shallow**: The table of contents exhibits a shallow structure, characterized by linear narration with a single-level depth, devoid of multi-level items.
  - Examples: Fiction, News, Opinion articles
- **Medium**: The table of contents demonstrates a moderate hierarchical depth, extending beyond a single level but not exceeding three levels.
  - Examples: Academic papers, Encyclopedia articles
- **Deep**: The table of contents features a highly intricate structure, with a depth exceeding four levels.
  - Examples:
    - IT: Software Development Reports
    - Medicine: Clinical Study Reports
    - Finance: Risk Assessment Reports
    - Education: Course Evaluation Reports
    - Law: Case Assessment Reports
    - Management: Project Management Reports
    - Manufacturing: Manufacturing Process Reports



### LongTextPrompts

We release a dataset specifically designed for open-ended long text generation across various topics, named **LongTextPrompts**. It includes 100 long text titles along with the corresponding prompts used to generate the long texts, covering 48 different categories of long texts. Detailed information is shown in the table below:

---

|   id | Title                                                                                                                 | Category                             | Type   |
|------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------|--------|
|    1 | The Quest for the Golden Relic                                                                                        | Adventure Fiction                    | Shallow|
|    2 | The Lost Underwater City                                                                                              | Adventure Fiction                    | Shallow|
|    3 | Waiting for His Return: Love During World War II                                                                      | Romance Fiction                      | Shallow|
|    4 | Love in Paris                                                                                                         | Romance Fiction                      | Shallow|
|    5 | The Last Colony on Mars                                                                                               | Science Fiction                      | Shallow|
|    6 | Chronicles of the Galactic Empire                                                                                     | Science Fiction                      | Shallow|
|    7 | Artificial Intelligence Crisis                                                                                        | Science Fiction                      | Shallow|
|    8 | The Dark Side of the Moon                                                                                             | Science Fiction                      | Shallow|
|    9 | The Dragon's Prophecy                                                                                                 | Fantasy Fiction                      | Shallow|
|   10 | The Enchanted Realm                                                                                                   | Fantasy Fiction                      | Shallow|
|   11 | The Shadows in the Basement                                                                                           | Horror Fiction                       | Shallow|
|   12 | Echoes of the Night                                                                                                   | Horror Fiction                       | Shallow|
|   13 | Night of Terror at the Inn                                                                                            | Thriller Fiction                     | Shallow|
|   14 | Crossing the Deserted Streets                                                                                         | Thriller Fiction                     | Shallow|
|   15 | Murder by the Lake                                                                                                    | Mystery Fiction                      | Shallow|
|   16 | The Secret of Ravenclaw Hall                                                                                          | Mystery Fiction                      | Shallow|
|   17 | The Museum Murder Mystery                                                                                             | Mystery Fiction                      | Shallow|
|   18 | The Tragedy Aboard the Train                                                                                          | Mystery Fiction                      | Shallow|
|   19 | The Ambition of Oda Nobunaga                                                                                          | Historical Fiction                   | Shallow|
|   20 | The Last Emperor                                                                                                      | Historical Fiction                   | Shallow|
|   21 | Legend of the Western Cowboy                                                                                          | Drama                                | Shallow|
|   22 | Battle of Two Cities                                                                                                  | Drama                                | Shallow|
|   23 | 2024 Election: Pennsylvania and Wisconsin Emerge as Pivotal Swing States                                              | Political News                       | Shallow|
|   24 | Pentagon Releases Indo-Pacific Strategy: Focuses on Countering China's Military Expansion                             | Political News                       | Shallow|
|   25 | Global Markets Rally Amid Economic Recovery Hopes                                                                     | Business and Economy News            | Shallow|
|   26 | Housing Market Bubble Warning: Home Prices Soar as Inventory Hits Record Lows                                         | Business and Economy News            | Shallow|
|   27 | Breakthrough in Quantum Computing: What It Means for the Future                                                       | Technology News                      | Shallow|
|   28 | The Rise of Artificial Intelligence: Transforming Our Daily Lives                                                     | Technology News                      | Shallow|
|   29 | World Cup Qualifiers: Latest Results and Highlights                                                                   | Sports News                          | Shallow|
|   30 | Olympic Games Recap: Medal Tally and Memorabilia                                                                      | Sports News                          | Shallow|
|   31 | Coldplay Announces Global Tour Kickoff in Tokyo, Japan for 2024                                                       | Entertainment News                   | Shallow|
|   32 | Dating Rumors? Taylor Swift Declares They Are Just Friends                                                            | Entertainment News                   | Shallow|
|   33 | Breakthrough in Cancer Research: New Treatment Shows Promising Results                                                | Science and Health News              | Shallow|
|   34 | The Rising Concern of Mental Health Issues Among Teenagers                                                            | Science and Health News              | Shallow|
|   35 | The Impact of Plastic Waste on Marine Life                                                                            | Environment News                     | Shallow|
|   36 | Climate Change: The Global Call to Action                                                                             | Environment News                     | Shallow|
|   37 | Modi Wins Third Term: Domestic Challenges and Global Ambitions of Indian Prime Minister                               | Political Opinion                    | Shallow|
|   38 | American Immigration: Analyzing the Similarities and Differences Between Biden and Trump's Border Policies            | Political Opinion                    | Shallow|
|   39 | The Aging Population: Rethinking Retirement and Elder Care in the 21st Century                                        | Social Commentary                    | Shallow|
|   40 | The Impact of Social Media on Society                                                                                 | Social Commentary                    | Shallow|
|   41 | Japanese businesses are trapped between America and China                                                             | Economic Opinion                     | Shallow|
|   42 | Tourism Industry Recovery: Challenges and Opportunities After the COVID-19 Pandemic                                   | Economic Opinion                     | Shallow|
|   43 | The Absurdity of Modern Office Life                                                                                   | Satire and Humor Opinion             | Shallow|
|   44 | Breaking: Nation Shocked as Study Reveals Money Can't Buy Happiness, But It Can Rent a Jet Ski                        | Satire and Humor Opinion             | Shallow|
|   45 | A Deep Dive into 'Inception': A Movie Review                                                                          | Movie review or Book review          | Shallow|
|   46 | Exploring the Magic of 'Harry Potter and the Sorcerer's Stone': A Book Review                                         | Movie review or Book review          | Shallow|
|   47 | Theoretical Research and Stability Analysis of K-essence Dark Energy Model in Cosmological Evolution.                | Physics Paper                        | Medium |
|   48 | Research on the Influence and Physical Mechanism of Magnetic Field Disturbances on the Behavior of High-Energy Particles in EAST Device. | Physics Paper                        | Medium |
|   49 | Research on the Application and Performance of Nanotechnology-Modified Polymer Membranes in Oil-Water Separation      | Chemistry Paper                      | Medium |
|   50 | Operando Spectroscopic and Electrokinetic Analysis of Formic Acid Oxidation on Copper Surfaces                        | Chemistry Paper                      | Medium |
|   51 | The Protective Effect of Interleukin-4 on Retinal Ganglion Cells and Its Role in Promoting Axon Regeneration          | Biology Paper                        | Medium |
|   52 | The Impact of the Gut Microbiota in Aged Rats on Spontaneous Seizure-like Discharges and Seizure Threshold: Mechanisms Involving Macrophages and Microglia | Biology Paper                        | Medium |
|   53 | Evaluating the Impact of Deforestation on Biodiversity                                                                | Environment Paper                    | Medium |
|   54 | The Impact of Salinity on Membrane Surface Properties and Fouling Behavior: Real-Time Analysis of Dynamic Interfaces  | Environment Paper                    | Medium |
|   55 | NG-Sort: An Efficient Algorithm for Large-Scale Data Sorting                                                          | Computer Science Paper               | Medium |
|   56 | Research on Reliability Modeling and Optimization of Large-Scale Cloud Computing Systems                              | Computer Science Paper               | Medium |
|   57 | KOLO: a improved neural nextwork architecture for image recognition                                                   | Artificial Intelligence Paper        | Medium |
|   58 | Research on long text generation algorithm based on improved RNN architecture                                         | Artificial Intelligence Paper        | Medium |
|   59 | The Ethics of Artificial Intelligence: A Kantian Perspective                                                          | Philosophy Paper                     | Medium |
|   60 | Nihilism and Existentialism: A Comparative Study                                                                      | Philosophy Paper                     | Medium |
|   61 | The Cognitive Impact of Social Media Usage: A Comprehensive Study                                                     | Psychology Paper                     | Medium |
|   62 | Behavioral Analysis of Anxiety Disorders: Current Trends and Future Directions                                        | Psychology Paper                     | Medium |
|   63 | The Rise and Fall of the Roman Empire                                                                                 | History Paper                        | Medium |
|   64 | The Impact of the Industrial Revolution on European Society                                                           | History Paper                        | Medium |
|   65 | The Evolution of Social Norms: A Comparative Analysis                                                                 | Sociology Paper                      | Medium |
|   66 | Impact of Social Media on Interpersonal Relationships                                                                 | Sociology Paper                      | Medium |
|   67 | Alexander the Great                                                                                                   | a historical figure's encyclopedia articles | Medium |
|   68 | Napoleon Bonaparte                                                                                                    | a historical figure's encyclopedia articles | Medium |
|   69 | Battle of Gettysburg                                                                                                  | a historical event's encyclopedia articles | Medium |
|   70 | Berlin Wall                                                                                                           | a historical event's encyclopedia articles | Medium |
|   71 | Quantum Mechanics                                                                                                     | a terminology's encyclopedia articles | Medium |
|   72 | Genetic Engineering                                                                                                   | a terminology's encyclopedia articles | Medium |
|   73 | League_of_Legends                                                                                                     | a computer game's encyclopedia articles | Medium |
|   74 | Minecraft                                                                                                             | a computer game's encyclopedia articles | Medium |
|   75 | Microsoft Corporation                                                                                                 | a company's encyclopedia articles    | Medium |
|   76 | Apple Inc.                                                                                                            | a company's encyclopedia articles    | Medium |
|   77 | Japan                                                                                                                 | a country's encyclopedia articles    | Medium |
|   78 | United States of America                                                                                              | a country's encyclopedia articles    | Medium |
|   79 | Development Technical Report on an Automatic License Plate Recognition System Based on Python and YOLOv8             | IT Report                            | Deep   |
|   80 | Technical Report on the Development of an E-commerce System Based on Java Spring and React                            | IT Report                            | Deep   |
|   81 | Comprehensive Clinical Study Report on Novel Cardiovascular Therapies                                                 | Medicine Report                      | Deep   |
|   82 | In-depth Analysis of COVID-19 Vaccine Efficacy: A Clinical Study Report                                               | Medicine Report                      | Deep   |
|   83 | Annual Financial Risk Assessment Report of Banabi Company                                                             | Finance Report                       | Deep   |
|   84 | Canon Company's Financial Analysis Report for the Fall of 2023                                                        | Finance Report                       | Deep   |
|   85 | Course Evaluation Report on Modern Education Practices                                                                | Education Report                     | Deep   |
|   86 | Project-Based Learning: An In-depth Course Evaluation Report                                                          | Education Report                     | Deep   |
|   87 | Case Assessment Report on Corporate Fraud Investigations                                                              | Law Report                           | Deep   |
|   88 | Legal Analysis of Intellectual Property Disputes: A Comprehensive Study                                               | Law Report                           | Deep   |
|   89 | Chicago Bridge Construction Project Management Report                                                                 | Management Report                    | Deep   |
|   90 | Narto Company's Annual Management Report: Strategic Growth and Development                                            | Management Report                    | Deep   |
|   91 | Analysis of the Efficiency of Lean Manufacturing Processes in Automotive Industries: A Case Study of the Tesla Factory in Shanghai | Manufacturing Report              | Deep   |
|   92 | A Case Study on Production Line Optimization for Assembly Line Balancing in Electronics Manufacturing: The Foxconn Example | Manufacturing Report              | Deep   |
|   93 | Environmental Impact Assessment Report on the Hydropower Plant Construction Project in the Upper Nile River           | Environment Report                   | Deep   |
|   94 | Environmental Impact Assessment Report for the New Soccer Stadium Construction Project on Elm Street, New York City   | Environment Report                   | Deep   |
|   95 | Advanced Data Structures and Algorithms                                                                               | Computer Science Textbook            | Deep   |
|   96 | Mastering Python Programming: From Basics to Advanced Applications                                                    | Computer Science Textbook            | Deep   |
|   97 | Grammar Comprehensive Guide: From Basics to Advanced                                                                  | English Textbook                     | Deep   |
|   98 | Mastering English Writing Techniques: Essays, Reports, and Creative Writing                                           | English Textbook                     | Deep   |
|   99 | The Comprehensive Guide to World History                                                                              | History Textbook                     | Deep   |
|  100 | American History: From Colonization to the 21st Century                                                               | History Textbook                     | Deep   |






## 3. Experiment

In the experiments, each method generated 100 long texts using the LongTextPrompts dataset.



### 3.1 Automated Evaluation

For each title in LongTextPrompts, we employed GPT-4o as the judge to assess the quality of the long texts generated by different methods based on the proposed metrics, and then to determine the winner. We calculated the win rate, lose rate, and draw rate as automated evaluation results.



### 3.2 Human Evaluation

We hired six evaluators to evaluate all the generated texts based on our metrics, where each metric is scored from 1 to 5, with higher scores indicating better performance. 



### 3.3 Ablation Study

We conducted an ablation experiment to study the effectiveness of various components of our framework. We sampled 30 titles and corresponding writing prompts from **LongTextPrompts** for our ablation study, and each variant of our method generated 30 long texts based on these prompts.



### 3.4 Turing Test

To evaluate the ability of our framework to generate human-like long texts, we conducted a Turing test. The long texts generated by different methods were shuffled and presented to evaluators to determine if the generated texts could convincingly be mistaken for those written by real humans.





















