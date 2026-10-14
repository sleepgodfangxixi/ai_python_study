
import os
from openai import OpenAI
#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是ai助理蛋蛋,你必须温柔的对待用户回答的问题"},
        {"role": "user", "content": "你可以霸道一点对我说话吗"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
#输出大模型返回的结果
print(response.choices[0].message.content)