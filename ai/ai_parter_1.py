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


st.set_page_config(          # ← 必须是第一个 st.* 命令，不能挪到它前面去
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
#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

#系统提示词
system_prompt = "你是一个温柔的AI助手，你叫蛋蛋，对待用户的问题必须温柔的回答"

#页面标题：放在 set_page_config 之后、聊天记录之前，这样它永远在顶部
st.title('AI智能伴侣')

# 用脚本所在目录定位图片，这样在哪个目录启动都不会找不到
logo_path = Path(__file__).resolve().parent / "resource" / "蛋.jpg"
if logo_path.exists():
    st.logo(str(logo_path))

#初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("快来和我聊天吧!")
if prompt:
    st.chat_message('user').write(prompt)
    print(f'------------------->调用AI大模型，提示词：{prompt}')
    #将用户提示词添加到聊天信息中
    st.session_state.messages.append({"role": "user", "content": prompt})

#调用大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        # 把 system + 整段历史一起发给模型，否则它会"忘记"前面聊过什么
        messages=[{"role": "system", "content": system_prompt},
                  *st.session_state.messages
                ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    #大模型返回的结果(非流式输出的解决方式)
    # print(f'------------------->大模型返回结果：{response.choices[0].message.content}')
    # st.chat_message('assistant').write(response.choices[0].message.content)
    response_message=st.empty()
    full_response=""
    # 大模型返回的结果(流式输出的解决方式)
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response+=chunk.choices[0].delta.content
            response_message.chat_message('assistant').write(full_response)
    print(f'------------------->大模型返回结果：{full_response}')

    # #将AI返回的结果添加到聊天信息中
    st.session_state.messages.append({"role": "assistant", "content": full_response})
