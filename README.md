# Click-Me-Simple-Game


A simple but customizable clicking speed game built with Python and Tkinter. The goal is to click the moving button as many times as possible before the timer runs out.

The game includes multiple difficulty levels, custom timers, theme switching, and high-score tracking.

---

## Features

* Click-based reflex game
* Multiple difficulty levels (Easy, Normal, Hard)
* Adjustable time limits
* Custom timer option
* Light and dark themes
* High score tracking
* Dynamic moving button system
* Simple and modern UI using Tkinter

---

## How It Works

The player starts the game from the main menu by selecting:

* A **time limit**
* A **difficulty level**

When the game starts, a button appears at random positions on the screen. Every successful click:

* Increases the score
* Moves the button to a new random position

The game runs until the timer reaches zero, after which a **Game Over** screen appears displaying:

* Final score
* High score
* Option to return to the main menu

---

## File Structure

```txt
project-folder/
│── main.py
│── requirements.txt
│── README.md
```

### Main Components

* **`main_menu()`** – Displays the main menu and settings
* **`start_game()`** – Starts a standard timed game
* **`custom_timer_menu()`** – Allows users to set a custom game duration
* **`change_x_y()`** – Handles button clicks and score updates
* **`update_timer()`** – Controls the game countdown
* **`game_over()`** – Displays final results and high score

---

## Technologies Used

* Python
* Tkinter
* Random module

---

## Installation

Install dependencies:

```bash
pip install tk
```

---

## How to Run

Run the game:

```bash
python main.py
```

### Gameplay

1. Select a timer duration or choose a custom time.
2. Choose a difficulty level:

   * **Easy** → Larger button
   * **Normal** → Medium button
   * **Hard** → Smaller button
3. Press **Start Game**.
4. Click the moving button as fast as possible before time runs out.

---

## Requirements

* Python 3.8+

---

## Future Improvements

* Sound effects
* Leaderboard system
* Click statistics (CPS tracking)
* Animations and visual effects
* Multiplayer mode

---

## License

This project is open-source and available under the **MIT License**.
