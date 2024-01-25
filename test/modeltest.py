ProjectPath = "/remote-home/yy/lzd/DocDoc" 
MODEL_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
TOKENIZER_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"

import sys
print(sys.path)
'''
['/remote-home/yy/lzd/DocDoc2/test', 
'/opt/conda/envs/DocDoc/lib/python310.zip', 
'/opt/conda/envs/DocDoc/lib/python3.10', 
'/opt/conda/envs/DocDoc/lib/python3.10/lib-dynload', 
'/opt/conda/envs/DocDoc/lib/python3.10/site-packages']
'''

from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录
sys.path.append(str(root_path))

import sys
print(sys.path)
'''
['/remote-home/yy/lzd/DocDoc2/test', 
'/opt/conda/envs/DocDoc/lib/python310.zip', 
'/opt/conda/envs/DocDoc/lib/python3.10', 
'/opt/conda/envs/DocDoc/lib/python3.10/lib-dynload', 
'/opt/conda/envs/DocDoc/lib/python3.10/site-packages',
'/remote-home/yy/lzd/DocDoc2']
'''


# from LLMs import ChatGLM
# llm= ChatGLM()
# llm.load_model(MODEL_PATH, TOKENIZER_PATH)

# prompt = """
#     ---
#     你好
#     我是
#     北大
#     ---
#     重复上面的模式三次
# """

# print(prompt)

# print(llm(prompt))



''' log
(DocDoc) (base) root@05af8eebcd95:/remote-home/yy/lzd/DocDoc2# python test/modeltest.py

['/remote-home/yy/lzd/DocDoc2/test', '/opt/conda/envs/DocDoc/lib/python310.zip', '/opt/conda/envs/DocDoc/lib/python3.10', '/opt/conda/envs/DocDoc/lib/python3.10/lib-dynload', '/opt/conda/envs/DocDoc/lib/python3.10/site-packages']
['/remote-home/yy/lzd/DocDoc2/test', '/opt/conda/envs/DocDoc/lib/python310.zip', '/opt/conda/envs/DocDoc/lib/python3.10', '/opt/conda/envs/DocDoc/lib/python3.10/lib-dynload', '/opt/conda/envs/DocDoc/lib/python3.10/site-packages', '/remote-home/yy/lzd/DocDoc2']

Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:34<00:00,  4.89s/it]

    ---
    你好
    我是
    北大
    ---
    重复上面的模式三次

您好，我是人工智能助手。
您好，我是人工智能助手。
您好，我是人工智能助手。

'''