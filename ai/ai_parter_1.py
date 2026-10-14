import os
from pathlib import Path

import streamlit as st
from openai import OpenAI


def get_api_key():
    """优先读 Streamlit Secrets（部署到云端时用），其次读环境变量（本地用）。"""
    try:
        if "DEEPSEEK_API_KEY" in st.secrets:
            return st.secrets["DEEPSEEK_API_KEY"]
    except Exception:
        pass  # 本地没有 .streamlit/secrets.toml 时会走到这里
    return os.environ.get("DEEPSEEK_API_KEY")


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

api_key = get_api_key()
if not api_key:
    st.error("没有找到 DEEPSEEK_API_KEY。本地：设置环境变量；云端：在 Streamlit 的 Secrets 里配置。")
    st.stop()

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

#系统提示词
system_prompt = "你是一个温柔的AI助手，你叫蛋蛋，对待用户的问题必须温柔的回答"

st.title('AI智能伴侣')

# 用脚本所在目录定位图片，这样在哪个目录启动都不会找不到
logo_path = Path(__file__).resolve().parent / "resource" / "蛋.jpg"
if logo_path.exists():
    st.logo(str(logo_path))

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
