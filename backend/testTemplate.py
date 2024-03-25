from pathlib import Path
import sys
root_path = Path(__file__).parent.parent  # /DocDoc 项目根目录
sys.path.append(str(root_path))

from util import text2html

testMarkdown:str = """# 北京大学
北京大学，简称“北大”，位于中国北京市海淀区颐和园路5号，是中国著名的综合性研究型大学之一，也是国家“双一流”、“985工程”、“211工程”的重点支持高校之一。
## 学术声誉
北京大学拥有悠久的历史和优良的学术声誉。其学科涵盖人文、社会科学、自然科学、工程技术、医学等多个领域，并在许多领域内具有国际影响力。
#### 校训
- 自强不息
- 厚德载物
### 校园
校园位于北京西北郊，毗邻颐和园和圆明园，占地约274万平方米，校园环境优美，古朴典雅。"""

if __name__ == "__main__":
    # test
    print(text2html(testMarkdown))
