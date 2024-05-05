import pandas as pd
import json

# 读取 Excel 文件
df = pd.read_excel("dongting_content.xlsx")

# 将 DataFrame 转换为 JSON 格式
json_data = df.to_dict(orient="records")

# 打印带缩进的 JSON 格式
print("[")
for i in range(len(json_data) - 1):
    id = json_data[i]["id"]
    heading = json_data[i]["heading"]
    dep = json_data[i]["dep"]
    level = json_data[i]["level"]
    print(" " + "{" + f"\"id\": {id}, \"heading\": \"{heading}\", \"dep\": {dep}, \"level\": {level}" + "},")# 打印一个空行，用于区分每个对象
print(" " + "{" + f"\"id\": {id}, \"heading\": \"{heading}\", \"dep\": {dep}, \"level\": {level}" + "}")# 打印一个空行，用于区分每个对象
print("]")

# 如果需要将 JSON 字符串写入文件
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, separators=(",", ": "), indent=2, ensure_ascii=False)
