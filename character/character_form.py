import streamlit as st
import random

def roll_4d6_drop_lowest():
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])  # Drop the lowest

def character_creation():
    st.header("🧝 Character Creation")

    name = st.text_input("Name")
    char_class = st.selectbox("Class", ["Fighter", "Wizard", "Rogue", "Cleric", "Ranger", "Paladin"])
    race = st.selectbox("Race", ["Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Tiefling"])
    background = st.text_input("Background", value="A mysterious past...")
    alignment = st.selectbox("Alignment", [
        "Lawful Good", "Neutral Good", "Chaotic Good",
        "Lawful Neutral", "True Neutral", "Chaotic Neutral",
        "Lawful Evil", "Neutral Evil", "Chaotic Evil"
    ])

    st.subheader("🎲 Ability Scores")
    
    if "rolled_stats" not in st.session_state:
        st.session_state.rolled_stats = []

    if st.button("Roll Stats (4d6 drop lowest x6)"):
        st.session_state.rolled_stats = [roll_4d6_drop_lowest() for _ in range(6)]
    
    if st.session_state.rolled_stats:
        stat_labels = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        stat_values = st.session_state.rolled_stats

        stats = {}
        for i in range(6):
            stats[stat_labels[i]] = st.number_input(
                f"{stat_labels[i]}", value=stat_values[i], step=1, min_value=3, max_value=18
            )
    else:
        st.info("Click the button above to roll your ability scores.")
        return  # Wait for stat roll before continuing

    if st.button("Start Adventure"):
        st.session_state.character = {
            "name": name,
            "class": char_class,
            "race": race,
            "background": background,
            "alignment": alignment,
            "stats": {
                "STR": stats["Strength"],
                "DEX": stats["Dexterity"],
                "CON": stats["Constitution"],
                "INT": stats["Intelligence"],
                "WIS": stats["Wisdom"],
                "CHA": stats["Charisma"],
            }
        }
        st.session_state.chat = []  # reset chat log
        st.success("Character created! Let the adventure begin.")
        st.rerun()

