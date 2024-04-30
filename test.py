def count_words_in_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # 假设每个空格分隔的部分都是一个单词
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print(f"发生错误：{e}")

# 测试函数
markdown_file_path = 'your_markdown_file.md'  # 替换为你的 markdown 文件路径
word_count = count_words_in_markdown(markdown_file_path)
if word_count is not None:
    print(f"Markdown 文件中的字数为：{word_count}")
