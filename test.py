# 假设 dep_text 是一个列表
dep_text = ["apple", "banana", "orange"]

# 修改后的代码
dep_text_str = ""
if dep_text is not None:
    for i in range(len(dep_text) - 1):
        dep_text_str += dep_text[i] + ","
    dep_text_str += dep_text[-1]

# 打印结果
print(dep_text_str)
