from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    /DocDoc2
cur_path = Path(__file__).parent    # 当前目录    /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))

def func(title:str) -> str:
    text = f"{title}'s text"
    return text

if __name__ == "__main__":
    text_list = ["ACM", "ICLR", "ICML"]
    full_text = ""
    for t in text_list:
        full_text += func(t + "\n")
        
    # 生成唯一的文件名，使用时间戳
    import time
    timestamp = time.strftime("%Y%m%d%H%M%S")
    txt = str(cur_path) + f'/output/promptLog_{timestamp}.txt'
    print(txt)
    with open(txt, 'w', encoding='utf-8') as file:
        file.write(full_text)   
