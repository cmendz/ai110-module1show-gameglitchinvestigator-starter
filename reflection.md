# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
# I submitted 50 and told me to go higher
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
# The Attempts number didn't change first time I ran and another at one point.
# It kept saying higher but in the end, the number was even way lower than my first guess.
# When had 2 attempts left, it said 1 attempt left and gave me score.
# New game changes the target number in the debug info, but guesses dont work and attempts dont go down.
# When finished playing one mode, going to another difficulty doesn't change the other bugs.
# History not recording correctly
# Took 2 presses each guess for attemps to go down and be recorded into history.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|       Input      | Expected Behavior |  Actual Behavior   | Console Output / Error |
|------------------|-------------------|--------------------|------------------------|
|  50 (secret=60)  | "Too High" hint   | "Too Low" hint     |          N/A           |
|  60 (secret=40)  | "Too Low" hint    | "Too High" hint    |          N/A           |
|  Clicked Guess   | Attemps Left - 1  | Attempts Left same |          N/A           |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
# The various AI tools I used on this project were strictly Copilot and the AI Coding Assistant within VSCode.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
# An example of an AI suggestion that was correct was when it came to a bug within the logic of the code. For example, previously, when gussing a number higher than the secret, it would indicate to "GO Higher", which should have not been the case.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
# For the most part, the AI suggestions were never incorrect or misleading, since for every clear prompt, there was a clear change, and I made sure to go through each change, feeling confident that it was changing for the better along the way.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# After accepting and making changes to bugs and code, I would always close and rerun the application again through Streamlit, while making sure that each detail has been changed and is working accordingly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
#  One pytest that was used was at first when testing a function called "test_guess_too_high_with_string_secret()", which ensured the outcome was ("Too High", "📉 Go LOWER!"). However, since then, this function was removed and kept basic at "test_guess_too_high", as there was a bug where sometimes the secret number would be kept as a string in the data.
- Did AI help you design or understand any tests? How?
# AI helped me understand the test mentioned in the question above, where a specific test case of a guess being higher than the secret, should return "Too High", "📉 Go LOWER!", in which it did, as well as the other scenarios where the guess is equal to the secret, and also when the guess is lower than the secret.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
# For Streamlit reruns, I would explain it as the application being rerun again whenever a button is pressed, which allows the screen to be updated. For Streamlit session states, I would describe it as a way to share variables and information between each run, so that future runs of the application can remember what was done previously.

# Example: Without Session State, if beginning with 5 attempts to guess, if number is guessed, Streamlit forgets everything and application resets attempts back at 5 everytime.

# Example: With Session State, when guessing a number, Streamlit checks the session state and subtracts 1 from attempts, remembering now that you have 1 less than before and also keeping the same secret number for you to guess.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
# I look forward to first analyzing code myself for bugs, and then using the assistance of the Coding Assistant to help scan and recommend proper changes.
- What is one thing you would do differently next time you work with AI on a coding task?
# I would make sure to immediately comment next to the changes that were made, that way it reduces the hassle of having to go through each fix at the end and wondering what exactly was changed again.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# Overall, this project helped me realize that the Coding Assistant isn't there to create the whole project and write the code all for you. Instead, it is there to guide and suggests changes that may help your goals.
