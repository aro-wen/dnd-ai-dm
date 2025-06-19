# 🎲 D&D 5e AI Dungeon Master

An AI-powered Dungeon Master for Dungeons & Dragons 5e, built with **Streamlit** and powered by **Google Gemini Pro**. Create your character, roll dice, and chat with an AI DM who remembers your story!

---

## ✨ Features

- 🧙‍♂️ Character creation: name, race, class, stats, background
- 💬 AI Dungeon Master with memory (last 10 messages + character sheet)
- 🎲 Dice roll support via `/roll 2d6+1` commands
- 🔁 Reset and reroll options

---

## 🚀 Getting Started

### 1. Clone the project
git clone https://github.com/your-username/dnd-ai-dm.git
cd dnd-ai-dm

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your .env file
Create a .env file in the root with:

GEMINI_API_KEY=your_google_api_key

MODEL_NAME=models

## ▶️ Run the App
streamlit run app.py

## 📦 Requirements

- streamlit
- google-generativeai
- python-dotenv

Install them with:

pip install -r requirements.txt

## 🧠 Memory
The AI uses your character info + the last 10 messages to guide its responses and maintain story continuity.

## 🔮 Ideas for the Future

* Save/load characters
* Support for parties and multiplayer
* Session export/logging
* Richer prompt injection

🐉 Enjoy your adventure!
Let the dice (and the AI) decide your fate...

