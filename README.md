# 🗺️ U.S. States Guessing Game

An interactive Python game that challenges the player to guess all **50 U.S. states** using a blank map of the United States.

The game displays a map and continuously prompts the user to enter state names.  
Correct guesses are written directly onto the map at their geographic location.

---

## 📌 How the Game Works

- A blank map of the United States is displayed.
- The player types the name of a U.S. state.
- If the guess is correct:
  - The state name appears on the map in the correct position.
- The game continues until:
  - All 50 states are guessed **or**
  - The player types **`Exit`**

When the player exits the game, a CSV file is generated containing the names of all states that were **not guessed**.

---

## 📂 Files Included

- `main.py` – Main game logic
- `50_states.csv` – State names with x/y coordinates for map placement
- `blank_states_img.gif` – Blank U.S. map used by the game
- `states_to_learn.csv` – Generated file with missing states (created on exit)

---

## 🛠️ Technologies Used

- Python
- turtle module
- pandas

---

## ▶️ How to Run the Game

1. Make sure you have **Python 3** installed.
2. Install required dependencies:
   ```bash
   pip install pandas
   ```
3. Run the game:
   ```bash
   python main.py
   ```
4. Start guessing U.S. states by typing their names.
5. Type `Exit` at any time to end the game and generate the missing states file.

---

## 🎯 Purpose of the Project

This project was built to:
- Practice working with CSV files in Python
- Use the turtle graphics library
- Apply basic game logic and user input handling
- Reinforce knowledge of U.S. geography in a fun way

---

## 🚀 Possible Improvements

- Add case-insensitive and partial name matching
- Track score and number of attempts
- Add a timer or difficulty levels
- Improve UI with hints or state outlines

---

## 👤 Author

Savvas Resiniotis  
Python Learner & Data Enthusiast
