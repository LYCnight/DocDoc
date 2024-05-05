import re

# 输入的字符串
input_str = """id:1, heading:概述, dep:-1, level:1  
id:2, heading:项目背景及项目建设特点, dep:-1, level:2 
"""

# 正则表达式模式
pattern = r"id:(\d+), heading:(.*?), dep:(.*?), level:(\d+)"

# 使用正则表达式进行匹配
matches = re.findall(pattern, input_str)

print(matches)

# 格式化输出
for match in matches:
    id, heading, dep, level = match
    print(f"ID: {id}, Heading: {heading}, Dep: {dep}, Level: {level}")

import pandas as pd
# 创建 DataFrame
df = pd.DataFrame(matches, columns=['id', 'heading', 'dep', 'level'])

# # 保存为 Excel 文件
# df.to_excel('output.xlsx', index=False)

# 追加数据到现有的 Excel 文件
with pd.ExcelWriter('output.xlsx', mode='a', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, header=None)
