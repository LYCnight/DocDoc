from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 
import re

def text2html(text: str) -> str:
    # 将 ### 标题转换为对应的 <h6> 标签
    text = re.sub(r'^######\s*(.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    # 将 ## 标题转换为对应的 <h5> 标签
    text = re.sub(r'^#####\s*(.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    # 将 # 标题转换为对应的 <h4> 标签
    text = re.sub(r'^####\s*(.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    # 将 ### 标题转换为对应的 <h3> 标签
    text = re.sub(r'^###\s*(.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    # 将 ## 标题转换为对应的 <h2> 标签
    text = re.sub(r'^##\s*(.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    # 将 # 标题转换为对应的 <h1> 标签
    text = re.sub(r'^#\s*(.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    # 将 - 列表转换为对应的 <ul> 和 <li> 标签
    text = re.sub(r'^-\s*(.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>[\r\n]*)+', r'<ul>\n\g<0>\n</ul>', text, flags=re.DOTALL)
    # 将普通文本转换为对应的 <p> 标签
    text = re.sub(r'^(?!<)(.*)$', r'<p>\1</p>', text, flags=re.MULTILINE)
    return text




# 测试
if __name__ == "__main__":
    # 测试示例
    text = """# 北京大学

    北京大学，简称“北大”，位于中国北京市海淀区颐和园路5号，是中国著名的综合性研究型大学之一，也是国家“双一流”、“985工程”、“211工程”的重点支持高校之一。

    ## 学术声誉

    北京大学拥有悠久的历史和优良的学术声誉。其学科涵盖人文、社会科学、自然科学、工程技术、医学等多个领域，并在许多领域内具有国际影响力。

    #### 校训

    - 自强不息
    - 厚德载物

    ### 校园

    校园位于北京西北郊，毗邻颐和园和圆明园，占地约274万平方米，校园环境优美，古朴典雅。"""


    html = text2html(text)
    print(html)

    ''' -- log
    (DocDoc) (base) root@77e886b634e6:/remote-home/yy/lzd/DocDoc# python backend/util.py 
    <h1>北京大学</h1>
    <p></p>
    <p>    北京大学，简称“北大”，位于中国北京市海淀区颐和园路5号，是中国著名的综合性研究型大学之一，也是国家“双一流”、“985工程”、“211工程”的重点支持高校之一。</p>
    <p></p>
    <p>    ## 学术声誉</p>
    <p></p>
    <p>    北京大学拥有悠久的历史和优良的学术声誉。其学科涵盖人文、社会科学、自然科学、工程技术、医学等多个领域，并在许多领域内具有国际影响力。</p>
    <p></p>
    <p>    #### 校训</p>
    <p></p>
    <p>    - 自强不息</p>
    <p>    - 厚德载物</p>
    <p></p>
    <p>    ### 校园</p>
    <p></p>
    <p>    校园位于北京西北郊，毗邻颐和园和圆明园，占地约274万平方米，校园环境优美，古朴典雅。</p>
    '''