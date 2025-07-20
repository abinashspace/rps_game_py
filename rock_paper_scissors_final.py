import tkinter as tk
import random

# ==== THEME SETTINGS ====
WINDOW_BG = "#1a1b26"      # Dark elegant background
BOX_BG = "#2e2e3a"         # Choice box background
WIN_COLOR = "#00FF7F"      # Neon green
LOSE_COLOR = "#ff355e"     # Neon red
TIE_COLOR = "#00e5ff"      # Cool neon cyan
FONT_MAIN = ("Segoe UI", 20, "bold")
FONT_RESULT = ("Arial", 18, "italic")
FONT_EMOJI = ("Segoe UI Emoji", 50)
FONT_LABEL = ("Arial", 14)

# ==== GAME VARIABLES ====
user_score = 0
computer_score = 0
moves = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# ==== MAIN FUNCTION ====
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(moves)

    # Update emoji box
    emoji_label.config(
        text=f"{emojis[user_choice]}   VS   {emojis[computer_choice]}"
    )
    names_label.config(
        text=f"You{' '*12}Computer\n{user_choice.title():<12}{computer_choice.title():>10}"
    )

    # Decide winner
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg=TIE_COLOR)
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
        result_label.config(text="You Win! 🎉", fg=WIN_COLOR)
    else:
        computer_score += 1
        result_label.config(text="Computer Wins! 💻", fg=LOSE_COLOR)

    score_label.config(
        text=f"Score: You {user_score}  |  Computer {computer_score}"
    )

def quit_game():
    root.destroy()

# ==== GUI SETUP ====
root = tk.Tk()
root.title("Rock, Paper, Scissors - Neon UI")
root.config(bg=WINDOW_BG)
root.resizable(False, False)

# ==== SCORE DISPLAY ====
score_label = tk.Label(
    root,
    text="Score: You 0  |  Computer 0",
    font=FONT_MAIN,
    fg="#f1f1f1",
    bg=WINDOW_BG
)
score_label.pack(pady=(20, 5))

# ==== EMOJI VS BOX ====
emoji_label = tk.Label(
    root,
    text="",
    font=FONT_EMOJI,
    bg=BOX_BG,
    fg="#FFFFFF",
    width=20,
    height=2,
    relief="ridge",
    bd=8
)
emoji_label.pack(pady=10)

names_label = tk.Label(
    root,
    text="Make your move!",
    font=FONT_LABEL,
    bg=BOX_BG,
    fg="#aaaaaa"
)
names_label.pack()

# ==== RESULT TEXT ====
result_label = tk.Label(
    root,
    text="",
    font=FONT_RESULT,
    bg=WINDOW_BG,
    fg="#ffffff"
)
result_label.pack(pady=(10, 20))

# ==== BUTTONS ====
button_frame = tk.Frame(root, bg=WINDOW_BG)
button_frame.pack()

button_styles = {
    "rock": {"bg": "#00ff7f", "fg": "#000"},
    "paper": {"bg": "#00e5ff", "fg": "#000"},
    "scissors": {"bg": "#ff355e", "fg": "#000"}
}

for move in moves:
    tk.Button(
        button_frame,
        text=f"{emojis[move]}  {move.title()}",
        font=FONT_MAIN,
        width=12,
        bg=button_styles[move]["bg"],
        fg=button_styles[move]["fg"],
        activebackground="#ffffff",
        activeforeground="#000000",
        bd=0,
        relief="ridge",
        command=lambda m=move: play(m)
    ).pack(side="left", padx=10, pady=10)

# ==== QUIT BUTTON ====
quit_btn = tk.Button(
    root,
    text="Quit",
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="#ffffff",
    activebackground="#444444",
    activeforeground="#ff5555",
    width=10,
    command=quit_game
)
quit_btn.pack(pady=(0, 15))

# ==== START THE GAME ====
root.mainloop()
