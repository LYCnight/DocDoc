from pathlib import Path
import sys
import time

# 获取项目根目录和当前目录
root_path = Path(__file__).parent.parent  # 项目根目录 /DocDoc2
cur_path = Path(__file__).parent  # 当前目录 /DocDoc2/test
sys.path.append(str(cur_path))
sys.path.append(str(root_path))


def func(title: str) -> tuple[str, str]:
    prompt = f"{title}'s prompt"
    text = f"{title}'s text"
    # global output_path
    with open(output_path, 'a', encoding='utf-8') as file:  # 使用 'a' 模式，即追加模式
        file.write(text + "\n")  # 直接写入文件
    return text, prompt

def main():
    text_list = ["ACM", "ICLR", "ICML"]
    
    # 生成唯一的文件名，使用时间戳
    timestamp = time.strftime("%Y%m%d%H%M%S")
    global output_path 
    output_path = str(cur_path) + f'/output/promptLog_{timestamp}.txt'

    for t in text_list:
        func(t)
        time.sleep(3)
    
    print(f"All texts have been written to {output_path}")

if __name__ == "__main__":
    main()