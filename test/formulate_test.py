import re

def formulate(text: str) -> str:
    # 替换 #, ##, ###, ####, #####, ###### 等Markdown heading命令
    text = re.sub(r'#+\s*(.*)', r'\1', text)
    return text

# 测试用例
text = """### 项目环评报告书主要结论

经过详细的环境影响评估，岳阳县水系连通及农村水系综合整治工程建设项目总体上呈现如下结论：

1. **正面影响**：
   - 项目实施后，预期的水资源优化配置和区域水系连通得以实现，有助于提高水资源利用效率，缓解局部地区的水资源短缺问题。
   - 农村水系整治改善了农村居民的生活用水条件，提升了农村生态环境质量。

2. **中性影响**：
   - 在一定程度上，项目通过改善水体流速和水体交换，可能对局部水生生态系统产生一定积极影响，但具体效果取决于工程设计和运营维护的合理性。

3. **负面/潜在问题**：
   - 报告指出，部分监测点的水环境质量指标未完全达到预期，特别是总磷含量超标，表明在项目实施过程中可能存在污水处理和排放控制方面的不足，需要加强管理以减少对水体的污染。
   
4. **环境风险与建议**：
   - 存在环境风险，如施工期间的噪声、尘土和废水处理不当等问题，需要采取严格的环保措施并制定应急预案。
   - 对于未达标的水环境指标，建议进一步优化工艺流程，提升污水处理设施的效能，并强化监管，确保长期稳定达标。

综上所述，虽然项目在整体上有利于区域水资源管理和农村环境改善，但仍需密切关注并解决存在的环境问题，以确保项目的环境可持续性。"""

print(formulate(text))