import openai
import streamlit as st
from streamlit_chat import message

with open("API_Key.txt", "r") as file:
    api_key = file.read().strip()

content_assistant = "Soy tu bot financiero de confianza, preguntame tus dudas"

st.title("Chuntaros:blue[Chatbot] :sunglasses:")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": content_assistant}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([10, 2])
    user_input = a.text_input(
        key='user_message',
        label="Your message:",
        placeholder="Pregunta financiera",
        label_visibility='collapsed',
        )
    b.form_submit_button( use_container_width=True, label=":blue[Enviar]")

placeholder = st.empty()
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with placeholder.container():
        with st.spinner('Pensando...'):
            response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=st.session_state.messages,
                        max_tokens = 600,
                        temperature = 1.0
                        )
            msg = response.choices[0].message.content

    st.session_state.messages.append({'role': 'assistant', 'content': msg})

for i, msg in enumerate(reversed(st.session_state.messages)):
    message(msg["content"], 
            is_user= msg["role"] == "user", 
            key=str(i))