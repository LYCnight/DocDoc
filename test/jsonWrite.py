import json

# 定义 JSON 数据
data = [
    {"id": 0, "heading": "概述", "dep": -1, "level": 0},
    {"id": 1, "heading": "项目背景以及项目建设特点", "dep": -1, "level": 0}
]

# 指定文件路径
file_path = "data.json"

# 将数据写入文件
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=2)  # indent 参数用于指定缩进，使 JSON 文件更易读
