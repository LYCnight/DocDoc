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
from config import MODEL_PATH, TOKENIZER_PATH, EMBEDDING_PATH
from LLMs import ChatGLM
llm = ChatGLM() # 使用 GPT-4

# 加载 Agent[Writer]
from core.Agent import Writer
writer = Writer(llm)

# 加载 Agent[Investigator]
from core.Agent import Investigator
investigator = Investigator(llm, load_index_From_last_time=False)

# 加载 Agent[ContentExpert]
from core.Agent import ContentExpert
contentExpert = ContentExpert(llm)

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

def gen_doc_pre(cur, title, mutation_prob, content:list[Heading]):
    global digest
    global content_response
    heading:str = cur.heading.heading
    dep:list[int] = cur.heading.dep
    id:int = cur.heading.id
    
    # 归来（如果是叶子节点，则归来）
    if not cur.childlist:
        if dep == [-1]:
            # 获取参考资料
            retrieved_knowledge = None
            # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
            # 获取目录（json形式，类型为string）
            # 获取 last_heading 的文本内容
            last_heading:str = get_last_heading(id, content)
            # 先生成 text
            new_text = write_without_dep(title, heading, content_response, digest, last_heading, retrieved_knowledge)  # 先生成 text
            # 再更新 digest
            digest = write_digest(title, heading, new_text, digest, content)  
            # 最后存储写作好的文本。
            cur.heading.text = new_text   
        else:
            if is_gen_post(cur.heading.dep, cur.heading.id):
                return
            # 获取参考资料
            retrieved_knowledge = None
            # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
            # 获取目录（json形式，类型为string）
            # 获取 last_heading 的文本内容
            last_heading:str = get_last_heading(id, content)
            # 获取依赖文本的内容
            dep_text = get_dep_text(content, dep)
            # 先生成text
            new_text = write_with_dep(title, heading, content_response, digest, last_heading, dep_text, retrieved_knowledge)
            # 再更新 digest
            digest = write_digest(title, heading, new_text, digest, content)   
            # 最后存储写作好的文本和对应的依赖文本
            cur.heading.text = new_text
            cur.heading.dep_text = dep_text
        return
    
    # 子递出
    for child_node in cur.childlist:
        gen_doc_pre(child_node, title, mutation_prob, content)

def gen_doc_post(title, cur, content:list[Heading]):
    global digest
    global content_response
    heading:str = cur.heading.heading
    dep:list[int] = cur.heading.dep
    id:int = cur.heading.id
    
    # 中处理
    if not cur.childlist:  # 如果是叶子节点
        if is_gen_post(dep, id):
            # 获取参考资料
            retrieved_knowledge = None
            # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
            # 获取目录（json形式，类型为string）
            # 获取 last_heading 的文本内容
            last_heading:str = get_last_heading(id, content)
            # 获取依赖文本的内容
            dep_text = get_dep_text(content, dep)
            # 先生成text
            new_text = write_with_dep(title, heading, content_response, digest, last_heading, dep_text, retrieved_knowledge)
            # 再更新 digest
            digest = write_digest(title, heading, new_text, digest, content)  
            # 最后存储写作好的文本和对应的依赖文本
            cur.heading.text = new_text
            cur.heading.dep_text = dep_text
        return
    
    # 子递出
    for i in range(len(cur.childlist)-1, -1, -1):
        gen_doc_post(title, cur.childlist[i], content)

def gen_doc_mutation(cur, title, mutation_prob, content):
    global digest
    global content_response
    heading = cur.heading.heading
    dep = cur.heading.dep
    id:int = cur.heading.id
    
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
        # 获取参考资料
        retrieved_knowledge = None
        # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
        # 获取目录（json形式，类型为string）
        # 获取 last_heading 的文本内容
        last_heading:str = get_last_heading(id, content)
        # 获取依赖文本的内容，并生成摘要
        dep_text = get_dep_text(content, dep)
        
        # 先生成text
        new_text = write_mutation(title, heading, content_response, digest, last_heading, dep_text, retrieved_knowledge)
        # 再更新 digest
        digest = write_digest(title, heading, new_text, digest, content)  
        # 最后存储写作好的文本和对应的依赖文本
        cur.heading.dep_text = dep_text
        cur.heading.text = new_text
        # 最后要更新一下依赖
        cur.heading.dep = dep
        

def mutation(mutation_prob):
    # 生成一个介于0到1之间的随机概率
    pro = random.random()
    if pro <= mutation_prob:
        return True
    else:
        return False

def write_without_dep(title, heading, content_jsonStr:str, digest, last_heading:str, retrieved_knowledge:str):
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_without_dep(title, heading, content_jsonStr, digest, last_heading, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_without_dep for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def write_with_dep(title, heading, content_jsonStr:str, digest, last_heading:str, dep_text:str, retrieved_knowledge:str) -> str:
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_with_dep(title, heading, content_jsonStr, digest, last_heading, dep_text, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_with_dep for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def write_mutation(title, heading, content_jsonStr:str, digest, last_heading:str, dep_text:str, retrieved_knowledge:str) -> str:
    # retrieved_knowledge = investigator.get_retrieved_knowledge(title, heading)
    new_text, prompt = writer.write_mutation(title, heading, content_jsonStr, digest, last_heading, dep_text, retrieved_knowledge)
    new_text = writer.formulate(new_text)
    # 记录 prompt
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"-------------------- write_mutation for '{heading}' --------------------\n" + prompt + "\n")
    return new_text

def write_digest(title:str, heading:str, new_text:str, digest:str, content:str) -> str:
    digest, prompt = writer.write_digest(title, heading, new_text, digest, content)
    return digest

def get_heading_id(heading:str, content:list[Heading]) -> int:
    '''获取指定heading的目录项的id，返回id'''
    

def get_last_heading(id:int, content: list[Heading]) -> str:
    '''获取指定id的目录项的上一个目录项的文本，拼接返回prompt'''
    assert id >= 1, "ID must be greater than or equal to 1"
    LastHeading: Heading = content[id - 1]
    last_heading_heading = LastHeading.heading
    last_heading_text = LastHeading.text
    prompt:str = f"""上一个目录项: `{last_heading_heading}`\n内容:\n{last_heading_text}"""
    return prompt    
    
    
def get_dep_text(content:list[Heading], dep:list[int]) -> str:
    '''
    获取指定id的目录项的依赖目录项的文本，拼接返回prompt
    '''
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



import random
import time

def main():
    random.seed(time.time())  # 设置随机种子
    
    # 生成唯一的文件名，使用时间戳
    timestamp = time.strftime("%Y%m%d%H%M%S")
    
    # prompt日志文件路径
    global promptLog_output_path    # 声明全局变量
    promptLog_output_path = str(cur_path) + f'/output/promptLog_{timestamp}.txt'
     # 初始化 prompt 日志
    with open(promptLog_output_path, 'a', encoding='utf-8') as file:
        file.write(f"运行开始自: {get_current_time()}\n" + f"所用模型：{MODEL_PATH}, 所用Embed_model:{EMBEDDING_PATH}\n")
    
    # 生成Doc的文件路径
    markdown_file_path = str(cur_path) + f'/output/genDoc_{timestamp}.md'

    # 读取目录
    from utils import read_content, print_content, get_stats
    # # 测试读取 level 范围在 min_level 到 max_level 之间的内容
    # # file_path = 'test/content.xlsx'
    # file_path = 'test/content.xlsx'
    # content = read_content(file_path, min_level=0, max_level=4) # 由于算法设计缘故，min_level must be 0
    # print_content(content)

    # global view
    global digest
    digest = ""
    
    # 生成目录
    from GPT4_test.prompt import prompt_template
    prompt = """
我想写一本玄幻小说，名为《斗破苍穹》。我想以第一人称视角进行写作，请你生成目录，并详细说明目录项的依赖关系。
大致的故事为：
《斗破苍穹》的故事发生在一个充满“斗气”的大陆上，讲述了名为萧炎的少年，年少时被视为废物（无法修炼斗气），接着奋起抗争，展开冒险（修炼）之旅，凭借自身努力、高人指导、奇珍异宝的帮助，不断收集“异火”（一种威力极大的火焰），持续提升丹药炼制水平（成为顶级炼药师）和斗气（战斗能量）修炼水平，战斗能力逐步加强。最后，主角萧炎不仅洗刷当年的耻辱，还一跃成为斗气大陆上的最强者——“斗帝”，成为该世界秩序守护者和最高权力拥有者。
任务设定：
萧炎
本书主角，穿越者，带着成年人的记忆从地球转生到斗气大陆。 [2]本为天才少年，但从十一岁那年开始连续三年多莫名其妙地退化成斗之气三段，从此逐渐沦为遭人白眼的废柴。之后得知原因竟是有一个神秘的灵魂“药老”藏在萧炎母亲的遗物戒指中不断吸收他的斗之气，在药老停止吸收斗之气并答应帮他重展天资后，一年时间内突破至斗之气九段，震惊全城。后来萧炎踏上了修炼之旅，以他的执着与信念闯荡大陆，一路历经坎坷，向着巅峰强者之途迈进，最终收服天下万火，成为万火之帝，号"炎帝"。自尊心强，恩怨分明，早期饱受冷眼与嘲讽，性格较为激进，冲动易怒，后期随着实力的增强与阅历的丰富，逐渐成长为性格沉稳冷静，处事周全的强者
药尘
男主角萧炎的老师。人称药老、药尊者，后称药圣，拥有“骨灵冷火”（后赠与萧炎）。星陨阁极少露面的阁主（副阁主为至交好友风尊者--风闲），初为九转斗尊巅峰强者，九品炼药宗师。因遭叛徒韩枫出卖而落难成为灵魂状态，潜伏于一个戒指中，后戒指辗转落入萧炎之手，在吸收萧炎三年斗之气后恢复意识。之后药尘一路帮助萧炎成长，将毕生斗技和炼药术倾囊相授，多次救萧炎于危难之中，成为萧炎一生中最敬重的老师。经萧炎炼制斗尊强者骨骸外加造化圣者手臂骨而复活，其实力提升至半圣，在服用了萧炎带回来的黄泉妖圣精血后晋阶成一星斗圣。
萧薰儿（古熏儿）
萧炎的两位妻子之一，清纯可人，高傲冷漠。古族的大小姐，自小在萧家长大，与萧炎无血缘关系，其父在她幼年时将她送往萧家，命她暗中查询萧家“陀舍古帝玉”碎片的下落并暗中夺得。因为幼时萧炎偷偷进入其房间，被其误会是在用斗气帮她温养身体而爱上他。在萧炎被视为废物的三年里从未放弃他，自始至终相信萧炎会成为超越巅峰的强者。一直鼓励萧炎并且尽自己最大可能地帮助他，萧炎也因为薰儿的不离不弃而被感动。
其身份背景为古族族长（古元）千金，是古族难得神品血脉拥有者，天赋异禀，拥有异火“金帝焚天炎”，依靠传承的斗帝血脉和古族家族力量实力暴涨得很快。先在迦南学院等萧炎两年，后又为保护萧炎而返回古界。在得知萧炎踏足中州时，第一时间前往与萧炎相见，并于冰河谷谷主（冰尊者）与魂殿青海尊者手中救下萧炎和天火尊者等人。后因家族原因，又不得不离开。主角实力提升后前往古界，两人终于再次相见，并获得其父的默许。书末尾和主角以及彩鳞一起举办了一场盛大的婚礼。
彩鳞（美杜莎女王）
萧炎的两位妻子之一，冷艳绝美，倾国倾城。加玛帝国塔戈尔大沙漠中的蛇人部落女王，其凶名与艳名在加玛帝国几乎人尽皆知。在夺取利用“青莲地心火”冲击斗宗时进化为上古异兽七彩吞天蟒，随后本体被萧炎收入带走，从此与七彩吞天蟒成为共生状态并陪伴在萧炎身边。
萧炎前往云岚宗赴三年之约时美杜莎现身将云山惊退，后为取得丹药而与萧炎达成协议，常常成为萧炎的保命符。在天焚练气塔底部时受到“陨落心炎”的煅烧而与七彩吞天蟒的灵魂融为一体，但同时不幸地被主角强暴， [3]并因此怀孕。本想杀了主角，但由于融合了吞天蟒灵魂使其受到吞天蟒影响而无法对主角下手。 在经历了一系列事件后最终认命决定跟随主角，并且在萧炎面前显露出女人的一面。
在萧炎冲击斗皇时为其护法，后萧炎离开西北前往中州后由彩鳞坐镇炎盟，一个人扛起炎盟，不惜性命守着他的亲人和加玛帝国，之后生下了他们的女儿萧潇。一晃十数年光阴，加玛帝国遭魂殿势力入侵，彩鳞率领炎盟抵抗魂殿的侵略，实力此时已达八星斗尊（化为七彩吞天蟒后的实力），所幸萧炎在危机关头赶到，事后彩鳞与萧炎办了一场简单婚礼并随萧炎返回星陨阁。在九幽地冥蟒族的九幽黄泉闭关数年后，彩鳞成功突破至四星斗圣，并进化为九彩吞天蟒。出关后与萧炎一起对抗天妖凰族。与萧炎生有一女，名为萧潇（本体与吞天蟒共生），是萧炎最天赋惊人的孩子，惊才绝艳。书末尾和主角以及古薰儿一起举办了一场盛大的婚礼。
小医仙
萧炎在魔兽山脉历练时认识的少女，对萧炎有特殊的感情，萧炎的红颜知己之一。体质为“厄难毒体”，万毒不侵，修炼《七彩毒经》，无需苦修，只需要不间断地吃毒药，便能快速地提升实力，但体内的毒素会不断累积，导致终有一天会彻底爆发出来。
曾与萧炎在魔兽山谷中共同生活过一段时间，后来独自前往出云帝国历练。再次登场时已成为毒宗宗主天毒女，实力达到四星斗宗。与萧炎前往中州时遭遇了空间风暴而分离，后因“厄难毒体”而被冰河谷追杀，留难到落神涧，被萧炎所救，此时已是六星斗宗。随后在萧炎的帮助下凝练毒丹，成功控制“厄难毒体”并晋阶至二星斗尊。经药老指点，小医仙在一位同样拥有“厄难毒体”的前辈墓前修炼其自创的控制“厄难毒体”之功法，将“厄难毒体”彻底炼化，实力提升至七星斗尊。后来服用了黄泉妖圣精血，顺利晋阶成一星斗圣。大结局时小医仙独自回到青山镇行医，后被萧炎邀请回乌坦城。
纳兰嫣然
纳兰家族的大小姐，云岚宗的少宗主，曾与萧炎指腹为婚。个性独立，主张自由恋爱，极端反感长辈包办婚姻。为了拥有自己的幸福与选择命运的权利，十五岁那年在爷爷纳兰桀的不知情下前往萧家退婚，使得萧炎颜面大失。萧炎一怒之下休妻，并发誓三年之后上云岚宗一洗当日之辱。
加玛帝国炼药师大会时纳兰嫣然对萧炎假扮的岩枭萌生了情愫，但萧炎的冷漠让其不思其解。后在与萧炎的三年之约一战中落败，期间发现了岩枭的身份并认识到自己的感情，但依旧不后悔自己当初退婚的决定。 [7-9]（番外中明确表明不后悔退婚 [10]）。
云岚宗被灭后和云韵一起离开了加玛帝国，后与老师一起加入了花宗。在天目山脉历练时与萧炎重逢，经过时间的冲刷，二人对当初的过节早已淡然。途中在萧炎的帮助下通过了“鼠潮音波阵”的闯关，得到了进入天山血潭中洗礼的名额，实力晋阶到斗宗。大结局时萧炎邀请云韵回到加玛帝国，纳兰嫣然也跟着云韵回去。
云韵
纳兰嫣然的老师，美丽高雅，萧炎的红颜知己之一。曾任云岚宗宗主，初登场时为三星斗皇，于魔兽山谷中与萧炎邂逅，是主角认识的第一个斗皇强者。在实力被封印的情况下被主角所救，分别时将贴身内甲赠与主角。
对萧炎很有好感，萧炎初期亦对其怀有些许情愫，两人之间的感情错综复杂。萧炎与云岚宗决战前夕，云山为了拉拢丹王古河而控制住云韵并将她许配给古河，婚礼当天萧炎杀上云岚宗，打败古河并击杀云山，宗门被灭后云韵与萧炎在云岚山上相处了几天，最后在内心挣扎下离开了加玛帝国。
云韵到达中州后在一次偶然间得到了花宗宗主花婆婆传承毕生斗气和宗主之位，但却遭到花婆婆养女花锦迫害，后在萧炎的帮助下夺回宗主之位，成为花宗宗主。在将花婆婆传承的斗气完全炼化后实力晋级为八星斗尊。后来率领花宗加入天府联盟，共同抵抗魂殿。大结局时萧炎邀请云韵回到加玛帝国。
    """
    prompt = "Q: " + prompt + "\nA: "
    prompt = prompt_template + prompt
    # print(prompt)
    # 生成完整目录
    global content_response 
    content, content_response = contentExpert.gen_content(prompt)
    # 提取根节点
    root = TreeNode(content[0])
    
    i:list = [1]    # 设置为 list 是为了模拟 c++ 函数中的引用传值 &
    build_tree(content, i, root)  # 构建N叉树
    print_tree(root)  # 层序遍历打印
    print()

    title = content[0].heading  # 获取文章标题
    mutation_prob = 1  # 突变概率
    
    
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

    print(markdown_file_path)   # Doc
    print(promptLog_output_path)    # prompts for generating Doc
    print(contentExpert.trace_log_file_path)   # process log for generating content   
    with open(markdown_file_path, 'a', encoding='utf-8') as file:
        file.write(f"运行开始自: {get_current_time()}\n" + f"所用模型：`{MODEL_PATH}`, 所用Embed_model:`{EMBEDDING_PATH}`\n") 
        file.write(full_text)   
        
if __name__ == "__main__":
    main()
