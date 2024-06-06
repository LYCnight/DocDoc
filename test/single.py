single_prompt = """
请你帮我写一篇深度学习领域的论文，标题为`VOLO: Vision Outlooker for Visual Recognition`。
下面是一些参考信息：
- 文章概要：
视觉识别多年来一直由卷积神经网络（CNN）主导。尽管最近流行的视觉变换器（ViT）在ImageNet分类中展示了基于自注意力模型的巨大潜力，但如果不提供额外数据，其性能仍然不及最新的SOTA CNN。在这项工作中，我们尝试缩小性能差距，并证明基于注意力的模型确实能够超越CNN。
我们发现，限制ViT在ImageNet分类中表现的一个主要因素是它们在将细粒度特征编码到标记表示中的低效率。为了解决这个问题，我们引入了一种新颖的展望注意力，并提出了一种简单且通用的架构，称为Vision Outlooker（VOLO）。与关注于粗粒度水平的全局依赖建模的自注意力不同，展望注意力有效地将细粒度特征和上下文编码到标记中，这被证明对识别性能至关重要，但在自注意力中却被很大程度上忽略了。
实验表明，我们的VOLO在ImageNet-1K分类中达到了87.1%的top-1准确率，这是第一个在这个具有竞争力的基准上超过87%准确率的模型，且无需使用任何额外的训练数据。此外，预训练的VOLO在转移到下游任务时表现良好，如语义分割。在Cityscapes验证集上我们达到了84.3%的mIoU得分，在ADE20K验证集上达到了54.3%。
代码可在https://github.com/sail-sg/volo获得。
- Outlook Attention
原理：Outlook Attention 通过局部窗口内的密集空间聚合来有效地编码细粒度信息，与自注意力机制相比，它通过简单的重塑操作生成注意力权重，从而避免了昂贵的点积注意力计算。
实现：对于每个空间位置 (i, j)，Outlook Attention 计算其与以 (i, j) 为中心的局部窗口内所有邻居的相似度。生成的展望权重直接用作聚合值的注意力权重，通过 Softmax 函数进行重塑。
"""

def get_current_time() -> str:
    import time
    import pytz
    from datetime import datetime

    # 获取当前时间的时间戳
    start_time = time.time()

    # 将时间戳转换为datetime对象，并设置时区为UTC
    utc_time = datetime.utcfromtimestamp(start_time).replace(tzinfo=pytz.utc)

    # 强制设置时区为东八区
    tz = pytz.timezone('Asia/Shanghai')
    local_time = utc_time.astimezone(tz)

    # 将强制设置时区后的时间格式化为24小时制的时间字符串
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc
cur_path = Path(__file__).parent    # 当前目录    /DocDoc/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

from LLMs import ChatGLM
from core.Agent import Writer
import time

# 记录程序开始运行时间，使用时间戳生成唯一的文件名
start_time = time.time()
timestamp = time.strftime("%Y%m%d%H%M%S")

# init
llm = ChatGLM()

# writing
full_text = llm(single_prompt)
# 计算程序运行时间，并保留两位小数
end_time = time.time()

# store to disk
markdown_file_path = str(cur_path) + f'/output/single/genDoc_{timestamp}.md'

# -- 计算程序运行时间 -- 
run_time_seconds = round(end_time - start_time, 2) # 秒
# 将秒数转换为分钟和秒的形式
minutes = int(run_time_seconds // 60)
seconds = run_time_seconds % 60
# 格式化为 n分m秒 的形式
run_time_formatted = f"{minutes}分{seconds:.2f}秒"
log =  f"算法耗时：`{run_time_formatted}\n"

print(markdown_file_path)
with open(markdown_file_path, 'a', encoding='utf-8') as file:
        file.write(f"运行开始自: {get_current_time()}\n" + f"所用模型：`gpt-4o-2924-05-13`, 所用Embed_model:`None`\n") 
        file.write(log)
        file.write(full_text)   













