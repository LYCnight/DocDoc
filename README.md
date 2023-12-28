hello!  
This an AI project of PKU.

## 使用方法
To use this project, you shoud:
```
git clone https://github.com/LYCnight/DocDoc.git
cd DocDoc
```

then (You should hava anaconda or minconda installed in your device first)
```
conda create -n DocDoc python=3.10.13
conda activate DocDoc
```

and
```
pip install -r requirements.txt
```

finally, we can have a test, try:
```
python flowcontrol.py
```

and you'll get:
![实现原理图](img/运行截图.png)

## 系统架构
![实现原理图](img/大框架.jpg)
![实现原理图](img/细框架.jpg)


## 开发计划
- [ ] 大模型和 embedding模型 接入
    - [] ChatGLM3-6B
- [ ] 数据接入 loader
    - [ ] pdf
    - [ ] word
    - [ ] txt
    - [ ] Excel
- [ ] 文档分割 spliter
    - [ ] NLTK
    - [ ] spaCy
    - [ ] SentenceTransformers
    - [ ] CharacterTextSplitter
    - [ ] RecursiveCharacterTextSplitter
    - [ ] tiktoken
    - [ ] GPT2TokenizerFast
    - [ ] LongContextReorder
- [ ] 向量数据库 embedding and vectorDb
    - [ ] Fasis
    - [ ] Chromadb
- [ ] 检索器  retriever
    - [ ] simple retriever
- [ ] 提示模板  prompt
- [ ] 产品生成
    - [ ] pdf
    - [ ] word
    - [ ] PPT
- [ ] 模型微调
- [ ] API部署
    - [ ] FastAPI
- [ ] 模型托管
    - [ ] FastChat
- [ ] webUI
