import streamlit as st
from google import genai

st.set_page_config(page_title="Jarvis AI", page_icon="🤖")

# Fetch key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Initialize official SDK client
client = genai.Client(api_key=api_key)

st.title("Jarvis AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("How can I assist you, Sir?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
