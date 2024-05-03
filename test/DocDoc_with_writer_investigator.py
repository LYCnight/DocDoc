from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc2
cur_path = Path(__file__).parent    # 当前目录    /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))
from core.prompt import RETRIEVED_KNOWLEDGE
import random
import time


# 记录程序开始时间
start_time = time.time()

# 加载 LLM 模型
from config import MODEL_PATH, TOKENIZER_PATH
from LLMs import ChatGLM
llm = ChatGLM()
llm.load_model(MODEL_PATH, TOKENIZER_PATH)

# 加载 Agent[Writer]
from core.Agent import Writer
writer = Writer(llm)

# 加载 Agent[Investigator]
from core.Agent import Investigator
investigator = Investigator(llm)

class Heading:
    def __init__(self, id, heading, dep, level):
        self.id = id
        self.heading = heading
        self.dep = dep
        self.level = level
        self.text = None
        self.dep_text = []

class TreeNode:
    def __init__(self, heading):
        self.heading = heading
        self.childlist = []


def build_tree(content, i:list, cur):
    # 归来
    if i[0] >= len(content):
        return
    
    # 不能纳为孩子，则向上返回
    if content[i[0]].level <= cur.heading.level:
        return
    
    # 可以纳为孩子，则继续向深层递归
    while i[0] < len(content) and content[i[0]].level > cur.heading.level:
        child_node = TreeNode(content[i[0]])
        cur.childlist.append(child_node)
        i[0] += 1
        build_tree(content, i, child_node)


from collections import deque
def order(root):
    result = []
    que = deque([root])
    while que:
        size = len(que)
        vec = []
        for _ in range(size):
            cur = que.popleft()
            vec.append(cur.heading.heading)
            for node in cur.childlist:
                que.append(node)
        result.append(vec)
    return result


def print_tree(root):
    result = order(root)
    for vec in result:
        print("[", end="")
        for j in range(len(vec)-1):
            print(vec[j] + ",", end="")
        print(vec[-1] + "]", end="")

def gen_doc_pre(cur, title, mutation_prob, content):
    heading = cur.heading.heading
    dep = cur.heading.dep
    
    # 归来（如果是叶子节点，则归来）
    if not cur.childlist:
        if dep == [-1]:
            retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
            new_text = write_without_dep(title, heading, retrieved_knowledge)
            cur.heading.text = new_text
        else:
            if is_gen_post(cur.heading.dep, cur.heading.id):
                return
            dep_text = get_dep_text(content, dep)
            retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
            new_text = write_with_dep(title, heading, dep_text, retrieved_knowledge)
            cur.heading.text = new_text
            cur.heading.dep_text = dep_text
        return
    
    # 子递出
    for child_node in cur.childlist:
        gen_doc_pre(child_node, title, mutation_prob, content)

def gen_doc_post(title, cur, content):
    # 中处理
    if not cur.childlist:  # 如果是叶子节点
        if is_gen_post(cur.heading.dep, cur.heading.id):
            dep_text = get_dep_text(content, cur.heading.dep)
            retrieved_knowledge = None
            # retrieved_knowledge = investigator.get_retrieved_knowledge(title, cur.heading.heading)
            new_text = write_with_dep(title, cur.heading.heading, dep_text, retrieved_knowledge)
            cur.heading.dep_text = dep_text
            cur.heading.text = new_text
        return
    
    # 子递出
    for i in range(len(cur.childlist)-1, -1, -1):
        gen_doc_post(title, cur.childlist[i], content)

def gen_doc_mutation(cur, title, mutation_prob, content):
    heading = cur.heading.heading
    dep = cur.heading.dep
    
    # 归来（为叶子节点，则归来）
    if not cur.childlist:
        return
    
    # 子递出
    for child_node in cur.childlist:
        gen_doc_mutation(child_node, title, mutation_prob, content)
    
    # 回溯，处理突变节点
    if cur.heading.level > 0 and mutation(mutation_prob):
        dep.clear()  # 发生突变，则清空当前节点的依赖
        # 获取下一层所有子节点的id，作为当前节点的依赖
        dep.extend([node.heading.id for node in cur.childlist])
        dep_text:str = get_dep_text(content, dep)
        retrieved_knowledge = None
        # retrieved_knowledge = investigator.get_retrieved_knowledge(title, cur.heading.heading)
        new_text = write_mutation(title, heading, dep_text, retrieved_knowledge)
        # 更新依赖
        cur.heading.dep = dep
        cur.heading.dep_text = dep_text
        cur.heading.text = new_text

def mutation(mutation_prob):
    # 生成一个介于0到1之间的随机概率
    pro = random.random()
    if pro <= mutation_prob:
        return True
    else:
        return False

def write_without_dep(title, heading, retrieved_knowledge):
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_without_dep(title, heading, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_without_dep for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def write_with_dep(title, heading, dep_text, retrieved_knowledge=None) -> str:
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_with_dep(title, heading, dep_text, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_with_dep for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def write_mutation(title, heading, dep_text, retrieved_knowledge=None) -> str:
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_mutation(title, heading, dep_text, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_mutation for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def get_dep_text(content, dep:list[int]) -> str:
    dep_text = ""
    for index, dep_id in enumerate(dep):
        if(dep_id != -1):
            text = content[dep_id].text
            heading = content[dep_id].heading
            if(text is not None):
                dep_text += f"{index + 1}." +  f"{heading}: " + f"[{text}]，" + "\n\n"
    return dep_text

def is_gen_post(dep, id):
    if dep == [-1]:
        return False
    for i in dep:
        if id >= i:
            return False
    return True

def doc_assemble(content):
    full_text = ""
    title = content[0]
    full_text += f"**{title.heading}**\n"
    for heading in content:
        if heading.level > 0:
            # print("heading:", heading.heading, ", heading->level =", heading.level)
            full_text += "#" * heading.level + " " + heading.heading + "\n"
            if heading.text:
                full_text += heading.text + "\n"
    return full_text


import random
import time

def main():
    random.seed(time.time())  # 设置随机种子
    
    # 生成唯一的文件名，使用时间戳
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    # prompt日志文件路径
    global promptLog_output_path    # 声明全局变量
    promptLog_output_path = str(cur_path) + f'/output/promptLog_{timestamp}.txt'
    
    # 生成Doc的文件路径
    markdown_file_path = str(cur_path) + f'/output/genDoc_{timestamp}.md'
    
    # content = [
    #     Heading(0, "root", [-1], 0),
    #     Heading(1, "A", [-1], 1),
    #     Heading(2, "B", [-1], 1),
    #     Heading(3, "C", [-1], 1)
    # ]
    
    # content = [
    #     Heading(0, "root", [-1], 0),
    #     Heading(1, "A", [-1], 1),
    #     Heading(2, "B", [-1], 2),
    #     Heading(3, "C", [-1], 3),
    #     Heading(4, "D", [3], 3),
    #     Heading(5, "E", [4], 3),
    #     Heading(6, "F", [12], 2),
    #     Heading(7, "G", [-1], 1),
    #     Heading(8, "H", [-1], 2),
    #     Heading(9, "L", [-1], 3),
    #     Heading(10, "I", [-1], 2),
    #     Heading(11, "J", [3], 3),
    #     Heading(12, "K", [-1], 3)
    # ]

    from utils import read_content, print_content, get_stats
    # 测试读取 level 范围在 min_level 到 max_level 之间的内容
    # file_path = 'test/content.xlsx'
    file_path = 'test/content.xlsx'
    content = read_content(file_path, min_level=0, max_level=3) # 由于算法设计缘故，min_level must be 0
    print_content(content)

    root = TreeNode(content[0])
    
    i:list = [1]
    build_tree(content, i, root)  # 构建N叉树
    print_tree(root)  # 层序遍历打印
    print()

    title = content[0].heading
    mutation_prob = 0.5  # 突变概率
    gen_doc_pre(root, title, mutation_prob, content)  # 生成文本（反向依赖生成）
    
    # print("genDocPre():")
    # for heading in content:
    #     print(f"{heading.heading}, 依赖于:{heading.dep}, {heading.text}")
    # print()

    gen_doc_post(title, root, content)  # 生成文本（正向依赖生成）

    # print("genDocPost():")
    # for heading in content:
    #     print(f"{heading.heading}, 依赖于:{heading.dep}, {heading.text}")
    # print()

    gen_doc_mutation(root, title, mutation_prob, content)  # 生成文本（突变节点）
    
    # print("genDocMutation():")
    # for heading in content:
    #     print(f"{heading.heading}, 依赖于:{heading.dep}, {heading.text}")
    # print()

    full_text = doc_assemble(content)  # 组装全文

    print(full_text)

    # 计算程序运行时间，并保留两位小数
    end_time = time.time()
    run_time_seconds = round(end_time - start_time, 2) # 秒
    # 将秒数转换为分钟和秒的形式
    minutes = int(run_time_seconds // 60)
    seconds = run_time_seconds % 60
    # 格式化为 n分m秒 的形式
    run_time_formatted = f"{minutes}分{seconds:.2f}秒"
    
    # 记录生成章节数目、程序运行时间
    log =  f"算法耗时：`{run_time_formatted}`，共生成`{len(content)}`个heading\n"
    full_text = log + full_text

    print(markdown_file_path)
    print(promptLog_output_path)
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(full_text)   

if __name__ == "__main__":
    main()
