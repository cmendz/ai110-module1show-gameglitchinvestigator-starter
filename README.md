# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of the game is to provide an experience where the user tries to guess a secret number randomized by the application.
- Game logic function were in app.py instead of logic_utils.py, incorrect descriptions given to user when guessing secret number, number of attemps left not changing accordingly with guess, etc.
- Moved game logic functions to logic_utils.py, refined descriptions given to users based on guesses, altered test cases in test_game_logic.py, etc.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters guess of 55 # Secret number is 40.
2. Game returns "Too High" and reduces "Attempts Left" by 1.
3. Score updates.
4. User enters a guess of 35.
5. Game returns "Too Low" and reduces "Attempts Left" by 1.
6. Score updates.
7. User enters correct guess of 40.
8. Game ends after correct guess, with score and message being returned.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

========================================== test session starts ==========================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\chris\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.8.0
collected 4 items                                                                                        

tests\test_game_logic.py ....                                                                      [100%]

=========================================== 4 passed in 0.01s ===========================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
