# app.py

import streamlit as st
from ai.gemini_api import init_gemini_model, generate_response, chat_sessions
from character.character_form import character_creation
import re
import random

# --- Dice roll handler ---
def handle_roll_command(command):
    match = re.match(r"/roll (\d+)d(\d+)([+-]\d+)?", command)
    if not match:
        return "Invalid roll format. Use `/roll XdY+Z`, like `/roll 2d6+1`."
    num, sides, modifier = match.groups()
    rolls = [random.randint(1, int(sides)) for _ in range(int(num))]
    total = sum(rolls) + (int(modifier) if modifier else 0)
    return f"🎲 You rolled: {rolls} {'+' + modifier if modifier else ''} = **{total}**"

# --- Streamlit config ---
st.set_page_config(page_title="D&D 5e AI Dungeon Master", layout="centered")
st.title("🎲 D&D 5e AI Dungeon Master")

# --- Character creation ---
if "character" not in st.session_state:
    character_creation()
    st.stop()

# --- Sidebar info ---
st.sidebar.header("🧝 Your Character")
char = st.session_state.character
st.sidebar.markdown(f"**{char['name']}** — {char['race']} {char['class']}")
st.sidebar.markdown(f"_{char['alignment']}_")
st.sidebar.markdown(f"**Background**: {char['background']}")
st.sidebar.markdown("**Stats:**")
for stat, value in char["stats"].items():
    st.sidebar.markdown(f"- {stat}: {value}")

# --- Reset character ---
if st.sidebar.button("🗑️ Reset Character"):
    for key in ["character", "chat", "rolled_stats"]:
        st.session_state.pop(key, None)
    chat_sessions.pop("streamlit", None)  # Reset Gemini chat session
    st.experimental_rerun()

# --- Chat logic ---
model = init_gemini_model()

if "chat" not in st.session_state:
    st.session_state.chat = []

# Show past messages
for message in st.session_state.chat:
    if message.startswith("Player:"):
        st.chat_message("user").markdown(message.replace("Player: ", ""))
    elif message.startswith("DM:"):
        st.chat_message("assistant").markdown(message.replace("DM: ", ""))

# --- Chat input ---
prompt = st.chat_input("What does your character do?")

if prompt:
    if prompt.startswith("/roll"):
        reply = handle_roll_command(prompt)
    else:
        st.session_state.chat.append(f"Player: {prompt}")
        
        # --- Build context-aware prompt ---
        context = (
            f"You are a Dungeon Master guiding a D&D 5e game.\n"
            f"The player is {char['name']}, a {char['race']} {char['class']}.\n"
            f"Alignment: {char['alignment']}, Background: {char['background']}.\n"
            f"Stats: {char['stats']}\n\n"
        )
        recent_history = "\n".join(st.session_state.chat[-10:])
        full_prompt = context + recent_history + "\nDM:"

        with st.spinner("The Dungeon Master is thinking..."):
            reply = generate_response(full_prompt, session_id="streamlit")

    st.session_state.chat.append(f"DM: {reply}")
    st.rerun()
