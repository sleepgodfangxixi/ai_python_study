from platform import system

import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐣",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.bilibili.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "xiexie"
    }
)
#系统提示词
system_prompt = "你是一个温柔的AI助手，你叫蛋蛋，对待用户的问题必须温柔的回答"

st.title('AI智能伴侣')

st.logo('./resource/蛋.jpg')

prompt = st.chat_input("快来和我聊天吧!")
if prompt:
    st.chat_message('user').write(prompt)
    print(f'------------------->调用AI大模型，提示词：{prompt}')

#调用大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print(f'------------------->大模型返回结果：{response.choices[0].message.content}')
    #大模型返回的结果
    st.chat_message('assistant').write(response.choices[0].message.content)
