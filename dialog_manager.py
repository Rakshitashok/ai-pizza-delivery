# dialog_manager.py
import os
import json
from typing import Dict, Any
from pydantic import BaseModel
#import openai
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")

MENU_PATH = "menu.json"
PROMPT_PATH = "prompt.txt"

def load_menu():
    with open(MENU_PATH, "r") as f:
        return json.load(f)

def load_prompt():
    with open(PROMPT_PATH, "r") as f:
        return f.read()

from openai import OpenAI
client = OpenAI()

def call_model(messages, model="gpt-4o-mini", temperature=0.2):
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=800
    )
    return resp.choices[0].message.content

def start_system():
    system = load_prompt()
    return [{"role": "system", "content": system}]

def build_user_message(user_text):
    return {"role": "user", "content": user_text}

# Basic helper: ask the model a question with context
def ask_agent(history, user_text):
    messages = history + [build_user_message(user_text)]
    out = call_model(messages)
    return out
