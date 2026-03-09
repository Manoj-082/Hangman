import streamlit as st
import random

WORDS = {
    "apple": "A common fruit 🍎",
    "tiger": "A big wild cat 🐅",
    "chair": "Furniture to sit on 🪑",
    "house": "A place to live 🏠",
    "table": "Used for eating or working",
    "water": "Essential liquid for life 💧",
}

STAGES = ["🙂","😐","😟","😨","😰","😵","💀"]

st.set_page_config(page_title="Hangman", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

body{
background-color:#0f172a;
}

.title{
text-align:center;
font-size:48px;
font-weight:700;
color:#facc15;
}

.hang{
text-align:center;
font-size:80px;
}

.word{
text-align:center;
font-size:40px;
letter-spacing:10px;
color:#34d399;
margin-bottom:20px;
}

.hint{
text-align:center;
background:#1e293b;
padding:10px;
border-radius:10px;
color:#cbd5f5;
margin-bottom:20px;
}

.stButton>button{
width:50px;
height:50px;
border-radius:10px;
background:#1e293b;
color:white;
border:1px solid #334155;
font-weight:bold;
}

.stButton>button:hover{
background:#334155;
}

.newword button{
width:200px;
height:50px;
font-size:18px;
background:#facc15;
color:black;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "word" not in st.session_state:
    st.session_state.word = random.choice(list(WORDS.keys()))
    st.session_state.guessed = []
    st.session_state.attempts = 6

word = st.session_state.word
hint = WORDS[word]

# ---------- TITLE ----------
st.markdown('<div class="title">🎮 Hangman</div>', unsafe_allow_html=True)

# ---------- EMOJI ----------
st.markdown(f'<div class="hang">{STAGES[6-st.session_state.attempts]}</div>', unsafe_allow_html=True)

# ---------- WORD DISPLAY ----------
display_word=""

for letter in word:
    if letter in st.session_state.guessed:
        display_word+=letter+" "
    else:
        display_word+="_ "

st.markdown(f'<div class="word">{display_word}</div>', unsafe_allow_html=True)

# ---------- HINT ----------
st.markdown(f'<div class="hint">💡 {hint}</div>', unsafe_allow_html=True)

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cols = st.columns(8)

for i,letter in enumerate(alphabet):

    if cols[i%8].button(letter):

        letter=letter.lower()

        if letter not in st.session_state.guessed:

            st.session_state.guessed.append(letter)

            if letter not in word:
                st.session_state.attempts-=1

# ---------- GAME STATUS ----------
if all(l in st.session_state.guessed for l in word):
    st.success("🎉 You Won!")

if st.session_state.attempts==0:
    st.error("💀 You Lost! Word: "+word)

# ---------- NEW WORD ----------
st.markdown('<div class="newword">', unsafe_allow_html=True)

if st.button("🔄 New Word"):
    st.session_state.word=random.choice(list(WORDS.keys()))
    st.session_state.guessed=[]
    st.session_state.attempts=6
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)