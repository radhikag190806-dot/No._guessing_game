import streamlit as st
import random

# Page Config
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Initialize Session State
if "human_score" not in st.session_state:
    st.session_state.human_score = 0

if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0

choices = {
    "Rock 🪨": 1,
    "Paper 📄": 2,
    "Scissors ✂️": 3
}

emoji = {
    1: "🪨 Rock",
    2: "📄 Paper",
    3: "✂️ Scissors"
}

st.title("🎮 Rock Paper Scissors")

st.markdown("---")

# Scoreboard
col1, col2 = st.columns(2)

with col1:
    st.metric("👤 Your Score", st.session_state.human_score)

with col2:
    st.metric("🤖 Computer Score", st.session_state.comp_score)

st.markdown("---")

st.subheader("Choose Your Move")

col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("🪨 Rock", use_container_width=True):
        user_choice = 1

with col2:
    if st.button("📄 Paper", use_container_width=True):
        user_choice = 2

with col3:
    if st.button("✂️ Scissors", use_container_width=True):
        user_choice = 3

# Game Logic
if user_choice:

    comp_choice = random.randint(1, 3)

    st.write(f"### You chose: {emoji[user_choice]}")
    st.write(f"### Computer chose: {emoji[comp_choice]}")

    if (
        (user_choice == 1 and comp_choice == 3)
        or (user_choice == 2 and comp_choice == 1)
        or (user_choice == 3 and comp_choice == 2)
    ):
        st.session_state.human_score += 1

        st.success("🎉 You won this round!")
        st.balloons()

    elif user_choice == comp_choice:
        st.info("🤝 It's a Draw!")

    else:
        st.session_state.comp_score += 1
        st.error("😢 Computer won this round!")

# Check Winner
if st.session_state.human_score >= 5:
    st.markdown("## 🏆 CONGRATULATIONS!")
    st.success("You won the game!")

    # Celebration Effect
    st.balloons()
    st.snow()

elif st.session_state.comp_score >= 5:
    st.markdown("## 🤖 COMPUTER WINS!")
    st.error("Better luck next time!")

# Restart Button
st.markdown("---")

if st.button("🔄 Restart Game"):
    st.session_state.human_score = 0
    st.session_state.comp_score = 0
    st.rerun()