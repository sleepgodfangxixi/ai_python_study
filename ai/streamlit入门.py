import streamlit as st

st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.bilibili.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "这是一个streamlit入门页面"
    }
)

st.title('蛋蛋')

st.write("鸡蛋就是鸡的卵，我们日常吃的一般是母鸡产下的未受精蛋，就算没有公鸡，母鸡也能下这种蛋，不会孵出小鸡。")

st.logo('./resource/蛋.jpg')