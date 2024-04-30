import re

text = """
1. 岳阳县的地理、地质和水文地质现状数据是什么？
2. 岳阳县的水系分布情况和水文特征是什么？
3. 岳阳县地下水环境质量现状如何？
4. 岳阳县地下水环境质量监测数据和评价结果是什么？
5. 岳阳县地下水环境治理和保护措施的技术可行性和经济成本如何？
6. 岳阳县地下水环境治理和保护措施的实施效果监测数据是什么？
7. 岳阳县地下水环境治理和保护措施的实施效果评估方法和技术路线是怎样的？
8. 岳阳县地下水环境治理和保护措施的实施效果监测数据和评估结果呢？
9. 岳阳县地下水环境治理和保护措施对周边生态环境、居民生活和经济社会的影响预测和评估如何？
"""

# Regular expression pattern to extract questions
# pattern = r'\d+\.\s*(.*?)\？' # 不带 ？
pattern = r'\d+\.\s*(.*?\？)'   # 带 ？

# Extracting questions using findall method
questions = re.findall(pattern, text)

print(questions)
