# 使用Python代码测返回
import requests
import json

base_url = "http://127.0.0.1:8000"


def hello(prompt: str = None):
    response = requests.get(f"{base_url}/hello") # -> response 对象
    print(response.status_code)
    print(response.json())

def chat(prompt: str = "你好"):
    data = {
        "prompt": prompt
    }
    response = requests.post(f"{base_url}/chat", json=data) # -> response 对象
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    # hello() # 打招呼
    chat("请介绍一下北京大学")  # 聊天
