import random
from tkinter import *

# ==========================
# VARIABLES
# ==========================
score = 0
high_score = 0
time_left = 30
game_running = False
theme = "light"
difficulty = "Normal"

# ==========================
# THEMES
# ==========================
themes = {
    "light": {
        "bg": "#f4f6f8",
        "panel": "#ffffff",
        "fg": "#222222",
        "secondary_fg": "#666666",
        "button_bg": "#e7e7e7",
        "accent": "#4A90E2",
        "score_bg": "#222222",
        "score_fg": "white"
    },

    "dark": {
        "bg": "#141414",
        "panel": "#222222",
        "fg": "#ffffff",
        "secondary_fg": "#aaaaaa",
        "button_bg": "#333333",
        "accent": "#5B8DEF",
        "score_bg": "#2a2a2a",
        "score_fg": "white"
    }
}

# ==========================
# WINDOW
# ==========================
window = Tk()
window.title("Click Me")
window.geometry("800x600")
window.resizable(False, False)


# ==========================
# THEME
# ==========================
def get_theme():
    return themes[theme]


def apply_window_theme():
    current = get_theme()
    window.configure(bg=current["bg"])


# ==========================
# UTIL
# ==========================
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def toggle_theme():
    global theme

    theme = "dark" if theme == "light" else "light"
    main_menu()


# ==========================
# BUTTON SIZE BY DIFFICULTY
# ==========================
def get_button_size():
    if difficulty == "Easy":
        return (18, 3)

    elif difficulty == "Normal":
        return (12, 2)

    else:
        return (8, 1)


# ==========================
# GAME FUNCTIONS
# ==========================
def move_button():
    click_btn.place(
        x=random.randint(50, 650),
        y=random.randint(80, 500)
    )


def change_x_y():
    global score

    if not game_running:
        return

    score += 1
    lbl_score.config(text=f"Score: {score}")
    move_button()


def update_timer():
    global time_left
    global game_running

    if time_left > 0 and game_running:
        lbl_timer.config(text=f"Time: {time_left}")
        time_left -= 1
        window.after(1000, update_timer)

    else:
        game_running = False
        game_over()


def start_game():
    global score
    global time_left
    global game_running
    global lbl_score
    global lbl_timer
    global click_btn

    clear_window()
    apply_window_theme()

    current = get_theme()

    score = 0
    game_running = True

    selected_time = time_var.get()

    if selected_time == "Custom":
        custom_timer_menu()
        return

    time_left = int(selected_time)

    # Score
    lbl_score = Label(
        window,
        text=f"Score: {score}",
        font=("Segoe UI", 14, "bold"),
        bg=current["score_bg"],
        fg=current["score_fg"],
        padx=10,
        pady=5
    )
    lbl_score.place(x=10, y=10)

    # Timer
    lbl_timer = Label(
        window,
        text=f"Time: {time_left}",
        font=("Segoe UI", 14, "bold"),
        bg=current["score_bg"],
        fg=current["score_fg"],
        padx=10,
        pady=5
    )
    lbl_timer.place(x=670, y=10)

    # Difficulty label
    Label(
        window,
        text=f"Difficulty: {difficulty}",
        font=("Segoe UI", 12),
        bg=current["bg"],
        fg=current["fg"]
    ).place(x=340, y=10)

    # Click button
    width, height = get_button_size()

    click_btn = Button(
        window,
        text="CLICK ME",
        command=change_x_y,
        width=width,
        height=height,
        font=("Segoe UI", 12, "bold"),
        bg=current["accent"],
        fg="white",
        relief="flat",
        cursor="hand2"
    )

    move_button()
    update_timer()


# ==========================
# CUSTOM TIMER MENU
# ==========================
def custom_timer_menu():
    clear_window()
    apply_window_theme()

    current = get_theme()

    frame = Frame(
        window,
        bg=current["panel"],
        padx=40,
        pady=40
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(
        frame,
        text="Custom Timer",
        font=("Segoe UI", 26, "bold"),
        bg=current["panel"],
        fg=current["fg"]
    ).pack(pady=(0, 20))

    Label(
        frame,
        text="Enter time in seconds",
        font=("Segoe UI", 12),
        bg=current["panel"],
        fg=current["secondary_fg"]
    ).pack()

    timer_entry = Entry(
        frame,
        font=("Segoe UI", 14),
        justify="center",
        width=10
    )
    timer_entry.pack(pady=15)

    def start_custom():
        global time_left

        try:
            custom_time = int(timer_entry.get())

            if custom_time <= 0:
                return

            time_left = custom_time
            start_custom_game()

        except:
            pass

    Button(
        frame,
        text="Start Game",
        command=start_custom,
        font=("Segoe UI", 12, "bold"),
        bg=current["accent"],
        fg="white",
        relief="flat",
        padx=20,
        pady=8
    ).pack(pady=5)

    Button(
        frame,
        text="Back",
        command=main_menu,
        font=("Segoe UI", 11),
        bg=current["button_bg"],
        fg=current["fg"],
        relief="flat"
    ).pack(pady=5)


def start_custom_game():
    global score
    global game_running
    global lbl_score
    global lbl_timer
    global click_btn

    clear_window()
    apply_window_theme()

    current = get_theme()

    score = 0
    game_running = True

    lbl_score = Label(
        window,
        text=f"Score: {score}",
        font=("Segoe UI", 14, "bold"),
        bg=current["score_bg"],
        fg=current["score_fg"]
    )
    lbl_score.place(x=10, y=10)

    lbl_timer = Label(
        window,
        text=f"Time: {time_left}",
        font=("Segoe UI", 14, "bold"),
        bg=current["score_bg"],
        fg=current["score_fg"]
    )
    lbl_timer.place(x=670, y=10)

    width, height = get_button_size()

    click_btn = Button(
        window,
        text="CLICK ME",
        command=change_x_y,
        width=width,
        height=height,
        font=("Segoe UI", 12, "bold"),
        bg=current["accent"],
        fg="white",
        relief="flat"
    )

    move_button()
    update_timer()


# ==========================
# GAME OVER
# ==========================
def game_over():
    global high_score

    if score > high_score:
        high_score = score

    clear_window()
    apply_window_theme()

    current = get_theme()

    frame = Frame(
        window,
        bg=current["panel"],
        padx=50,
        pady=40
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(
        frame,
        text="GAME OVER",
        font=("Segoe UI", 28, "bold"),
        bg=current["panel"],
        fg=current["fg"]
    ).pack()

    Label(
        frame,
        text=f"Your Score: {score}",
        font=("Segoe UI", 16),
        bg=current["panel"],
        fg=current["fg"]
    ).pack(pady=10)

    Label(
        frame,
        text=f"High Score: {high_score}",
        font=("Segoe UI", 18, "bold"),
        bg=current["panel"],
        fg=current["accent"]
    ).pack()

    Button(
        frame,
        text="Back To Menu",
        command=main_menu,
        font=("Segoe UI", 12, "bold"),
        bg=current["accent"],
        fg="white",
        relief="flat",
        padx=20,
        pady=8
    ).pack(pady=20)


# ==========================
# MAIN MENU
# ==========================
def main_menu():
    clear_window()
    apply_window_theme()

    current = get_theme()

    frame = Frame(window, bg=current["bg"])
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(
        frame,
        text="CLICK ME",
        font=("Segoe UI", 36, "bold"),
        bg=current["bg"],
        fg=current["fg"]
    ).pack()

    Label(
        frame,
        text="How fast can you click?",
        font=("Segoe UI", 12),
        bg=current["bg"],
        fg=current["secondary_fg"]
    ).pack(pady=(0, 25))

    card = Frame(
        frame,
        bg=current["panel"],
        padx=40,
        pady=35
    )
    card.pack()

    Label(
        card,
        text="HIGH SCORE",
        font=("Segoe UI", 10, "bold"),
        bg=current["panel"],
        fg=current["secondary_fg"]
    ).pack()

    Label(
        card,
        text=str(high_score),
        font=("Segoe UI", 28, "bold"),
        bg=current["panel"],
        fg=current["accent"]
    ).pack(pady=(0, 20))

    # Time select
    Label(
        card,
        text="Time Limit",
        font=("Segoe UI", 14),
        bg=current["panel"],
        fg=current["fg"]
    ).pack()

    global time_var
    time_var = StringVar(value="30")

    OptionMenu(
        card,
        time_var,
        "10",
        "20",
        "30",
        "60",
        "120",
        "Custom"
    ).pack(pady=10)

    # Difficulty select
    Label(
        card,
        text="Difficulty",
        font=("Segoe UI", 14),
        bg=current["panel"],
        fg=current["fg"]
    ).pack()

    global difficulty_var
    difficulty_var = StringVar(value="Normal")

    def set_difficulty(*args):
        global difficulty
        difficulty = difficulty_var.get()

    difficulty_var.trace("w", set_difficulty)

    OptionMenu(
        card,
        difficulty_var,
        "Easy",
        "Normal",
        "Hard"
    ).pack(pady=10)

    Button(
        card,
        text="▶ Start Game",
        command=start_game,
        font=("Segoe UI", 14, "bold"),
        bg=current["accent"],
        fg="white",
        relief="flat",
        padx=25,
        pady=10
    ).pack(pady=10)

    Button(
        card,
        text=f"Theme: {theme.capitalize()}",
        command=toggle_theme,
        font=("Segoe UI", 11),
        bg=current["button_bg"],
        fg=current["fg"],
        relief="flat"
    ).pack()


# ==========================
# START
# ==========================
main_menu()
window.mainloop()