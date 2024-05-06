import pandas as pd

class Heading:
    def __init__(self, id, heading, dep, level):
        self.id = id
        self.heading = heading
        self.dep = dep
        self.level = level
        self.text = None
        self.dep_text = []

content = [Heading(1, "北大", [-1], 1), Heading(1, "清华", [2,3,4], 2)]

def persist_to_xlsx(content):
    # 将数据转换为字典列表
    data = [{"id": item.id, "heading": item.heading, "dep": item.dep, "level": item.level} for item in content]
    
    # 创建 DataFrame 对象
    df = pd.DataFrame(data)
    
    # 将数据写入 Excel 文件
    df.to_excel("xlsxoutput.xlsx", index=False)

# 调用函数
persist_to_xlsx(content)
