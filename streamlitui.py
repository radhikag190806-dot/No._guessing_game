import streamlit as st
import random

st.title("🎯 Guess the Number Game")
st.write("Guess a number between **1 and 100**")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low 🔽")
    elif guess > st.session_state.number:
        st.warning("Too high 🔼")
    else:
        st.success(f"🎉 You won in {st.session_state.attempts} attempts!")
        st.balloons()   # 🎈🎈🎈 BALLOONS POP UP HERE
        st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False


# to run the game type - python -m streamlit streamlitui.py(your file name) 

