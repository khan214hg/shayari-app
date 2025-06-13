import streamlit as st
import random

templates = [
    "Tere {word1} ka {word2} yaad aata hai, \nHar lamha mujhe rulata hai. 😢",
    "{word1} ki galiyon mein {word2} dhoondhta hoon, \nApni tanhaayi se mooh modhta hoon. 🌙",
    "Jab bhi {word1} ka zikr aata hai, \nMera {word2} udas ho jaata hai. 💔",
    "{word1} ka dard hai, {word2} ki baat hai, \nZindagi bas ek mulaqat hai. 🕊️",
    "{word1} ki chahat mein {word2} gawa baitha hoon, \nAb to khud ko hi bhool baitha hoon. 🥀"
]

st.title("🌟 Instant Shayari Maker 🌟")

word1 = st.text_input("Pehla lafz (e.g. pyaar, gham)")
word2 = st.text_input("Doosra lafz (e.g. tanhaayi, yaad)")

if st.button("Shayari Banaao"):
    if word1.strip() == "" or word2.strip() == "":
        st.warning("Dono lafz daalo boss! 😎")
    else:
        template = random.choice(templates)
        shayari = template.format(word1=word1, word2=word2)
        st.success(shayari)
