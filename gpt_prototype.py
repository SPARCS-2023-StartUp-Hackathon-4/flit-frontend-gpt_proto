import streamlit as st
import requests
import json


st.set_page_config(
    page_title='Flit Automatic Biz Plan'
)


# Set Max Width
def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

with st.sidebar:
    st.markdown("""
    # About 
    <Flit>'s Biz Plan Supporter is a helper tool built on GPT-3.. 
    """)
    st.markdown("""
    # How does it work
    작성하던 사업계획서의 부분을 입력하고 엔터를 누르면 텍스트가 생성됩니다
    """)
    st.markdown("""
    Made by [@junseokangofficial] at SPARCS Hackathon
    """,
    unsafe_allow_html=True,
    )

st.image('ico.png')


st.title('Flit Automatic Biz Plan')
st.header("")

st.markdown("### Team A - Flit's Biz Plan Generator")
st.markdown("") # 구분선

input_prompt = None

if 'output' not in st.session_state:
    st.session_state['output'] = 1

if st.session_state['output'] != 0:
    st.markdown("""
    # Biz Plan Prompter
    """)
    input_prompt = st.text_input("Input your Biz Plan", disabled=False, placeholder="What's on your mind?")
    st.session_state['output'] = st.session_state['output'] + 1


if input_prompt:
    prompt = "Here is suggestion for you.."

    result = requests.get(
        url="http://ec2-43-201-42-19.ap-northeast-2.compute.amazonaws.com:9000/generate/{0}".format(input_prompt),
    ).json()['suggestion']

    st.info(result)
