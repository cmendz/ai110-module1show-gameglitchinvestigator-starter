import random
import streamlit as st
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score
#FIX: Moved get_range_for_difficulty function and parse_guess into logic_utils.py file.

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

st.session_state.setdefault("attempts", 0) #FIX: Changed "attempts" default value to 0 instead of None for better type consistency.
st.session_state.setdefault("score", 0)
st.session_state.setdefault("status", "playing")
st.session_state.setdefault("history", [])
st.session_state.setdefault("new_game_requested", False)

st.subheader("Make a guess")

attempts_info = st.empty() #FIX: Placeholder so "Attempts left" can be updated after form submission.

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

guess_key = f"guess_input_{difficulty}"

# Clear input if new game was requested (must happen BEFORE form is rendered)
if st.session_state.new_game_requested:
    st.session_state.pop(guess_key, None)
    st.session_state.new_game_requested = False

with st.form(key="guess_form"):
    raw_guess = st.text_input("Enter your guess:", key=guess_key)
    show_hint = st.checkbox("Show hint", value=True)
    submit = st.form_submit_button("Submit Guess 🚀")

col1, col2 = st.columns([2, 1])
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    pass

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.new_game_requested = True
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        secret = st.session_state.secret
        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            if st.session_state.attempts == 1: #FIX: Added special message for winning on the first attempt.
                st.success(
                    "🎉 Amazing! You guessed it on the first try! "
                    f"The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            else:
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

attempts_info.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
