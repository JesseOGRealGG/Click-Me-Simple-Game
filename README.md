<img width="502" height="398" alt="Screenshot 2026-06-08 175257" src="https://github.com/user-attachments/assets/779c43d6-56e6-4b30-a653-341432a9c739" />
<img width="1550" height="1168" alt="Screenshot 2026-06-08 175250" src="https://github.com/user-attachments/assets/36e0c913-fe5d-4e7e-8912-e8168a0ea588" />
<img width="1556" height="1196" alt="Screenshot 2026-06-08 175232" src="https://github.com/user-attachments/assets/6d2edc07-aa37-447a-9996-114650b7beb5" />
<img width="1576" height="810" alt="Screenshot 2026-06-08 175439" src="https://github.com/user-attachments/assets/d5abdba1-2ddb-4a88-8670-fd113531d599" />
<img width="1560" height="292" alt="Screenshot 2026-06-08 175351" src="https://github.com/user-attachments/assets/f992c511-bdeb-4ce9-acb7-c47b1746a7e9" />
<img width="1026" height="958" alt="Screenshot 2026-06-08 175343" src="https://github.com/user-attachments/assets/138447ea-0ae2-4797-ad9a-412ba2b0c916" />
<img width="1572" height="1174" alt="Screenshot 2026-06-08 175337" src="https://github.com/user-attachments/assets/686d67e5-fdff-42ea-a5f7-43a86469e188" />
<img width="1566" height="1156" alt="Screenshot 2026-06-08 175324" src="https://github.com/user-attachments/assets/fcef65f9-b498-476b-a751-4567d94f7821" />
<img width="1332" height="1066" alt="Screenshot 2026-06-08 175308" src="https://github.com/user-attachments/assets/ad0f4b94-e150-4bef-a52c-b3679705d72e" />
<img width="342" height="338" alt="Screenshot 2026-06-08 175301" src="https://github.com/user-attachments/assets/5304cc01-4214-4e3e-87b2-8d084785a1ce" />
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
