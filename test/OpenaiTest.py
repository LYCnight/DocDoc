import os
from openai import OpenAI

# jupyter notebook 中翻墙
# os.environ['http_proxy'] = '127.0.0.1:7890'
# os.environ['https_proxy'] = '127.0.0.1:7890'

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello! Who are you?",
        }
    ],
    model="gpt-3.5-turbo",
)

print("_"*60)
print(chat_completion.choices[0].message.content)
print("_"*60)
print("如果👆有回复，则说明API有效")