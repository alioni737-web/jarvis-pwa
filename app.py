import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Jarvis AI", page_icon="⚡")
st.title("⚡ Jarvis AI")
st.caption("Online & Ready, Sir.")

client = genai.Client(api_key="AQ.Ab8RN6K5XwUjgOt91iiyPAGn2ZktvbqZAvnTtK_fo6V-b96XIg")

config = types.GenerateContentConfig(
    system_instruction="You are an advanced, witty AI assistant named Jarvis. Always address the user as 'Sir'. Keep responses direct and conversational."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("How can I assist you, Sir?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        res = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_input,
            config=config
        )
        st.write(res.text)
        st.session_state.messages.append({"role": "assistant", "content": res.text})