import json

# 指定文件路径
file_path = "data.json"

# 从文件中读取数据并解析
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# 遍历打印数据
for item in data:
    print("id:", item["id"])
    print("heading:", item["heading"])
    print("dep:", item["dep"])
    print("level:", item["level"])
    print()
