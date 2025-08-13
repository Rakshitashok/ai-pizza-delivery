# streamlit_app.py
import streamlit as st
import json
from dialog_manager import start_system, ask_agent, load_menu
from gtts import gTTS
import tempfile
import os
import base64

st.set_page_config(page_title="AI Pizza Delivery", layout="centered")
st.title("PizzaBuddy — AI Pizza Delivery Service (API)")

menu = load_menu()
system_messages = start_system()
if "history" not in st.session_state:
    st.session_state.history = system_messages.copy()
if "chat" not in st.session_state:
    st.session_state.chat = []

def send_to_agent(user_input):
    st.session_state.chat.append(("user", user_input))
    reply = ask_agent(st.session_state.history, user_input)
    st.session_state.chat.append(("agent", reply))
    st.session_state.history.append({"role": "user", "content": user_input})
    st.session_state.history.append({"role": "assistant", "content": reply})
    return reply

st.sidebar.header("Menu (quick)")
for p in menu["pizzas"]:
    st.sidebar.write(f"- {p['name']} (${p['base_price']})")
st.sidebar.write("Sizes: small, medium, large")
st.sidebar.write("Toppings: " + ", ".join([t["name"] for t in menu["toppings"]]))

user_input = st.text_input("Say something to PizzaBuddy", key="input")
if st.button("Send"):
    if user_input.strip():
        reply = send_to_agent(user_input)
        st.markdown(f"**PizzaBuddy:** {reply}")
        # If the reply contains a JSON order code block, extract and show
        if "```" in reply and "{" in reply:
            start = reply.find("```")
            code = reply[reply.find("```", start+3)+3:] if reply.count("```")>=2 else None
            # crude extraction — more robust parsing recommended
            st.success("Agent returned a JSON order. Please copy it from the chat.")
