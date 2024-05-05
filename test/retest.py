import re

def convert_to_format(input_str):
    # 用正则表达式提取每一项
    pattern = r"-([^:]+):(.*?)(?=\s*-(?:[^:]+):|$)"
    matches = re.findall(pattern, input_str)

    # 初始化 ID 和 Level
    id_count = 1
    level = 1

    # 遍历每一项，输出格式化结果
    for match in matches:
        heading = match[1].strip()
        dep = -1 if match[0].strip() == "概述" else 1
        print(f"ID: {id_count}, Heading: {heading}, Dep: {dep}, Level: {level}")
        id_count += 1
        if match[0].strip() == "项目目标":
            level += 1

# 输入的字符串
input_str = """- 概述
    - 项目背景及项目建设特点
    - 项目目标
        - 子目标1
        - 子目标2
    - 项目范围"""

# 调用函数进行转换
convert_to_format(input_str)
