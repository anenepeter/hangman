import tkinter as tk
import random

# List of words to guess
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

# Choose a random word
word = random.choice(someWords)
guessed = ['_' for _ in word]  # List to keep track of guessed letters
chances = len(word) + 2  # Number of chances
used_letters = set()  # Track guessed letters
timer_duration = 20
timer_seconds = timer_duration
timer_active = False
timer_id = None

def start_timer():
    global timer_seconds, timer_id, timer_active, chances
    timer_seconds = timer_duration
    timer_active = True
    update_timer_label()
    timer_id = root.after(1000, update_timer)

def update_timer():
    global timer_seconds, timer_id, timer_active, chances
    if timer_active:
        timer_seconds -= 1
        update_timer_label()
        if timer_seconds <= 0:
            timer_active = False
            status_label.config(text=f"Time's up! You lost a chance.")
            chances -= 1
            update_display()
            if chances <= 0:
                status_label.config(text=f"You lost! The word was '{word}'.")
                disable_buttons()
            else:
                start_timer() # Start timer again for the next guess
        else:
            timer_id = root.after(1000, update_timer)

def stop_timer():
    global timer_active, timer_id
    timer_active = False
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

def update_timer_label():
    timer_label.config(text=f"Time: {timer_seconds}")

def guess(letter):
    global chances, timer_active
    if not timer_active:
        start_timer()
    if letter in used_letters:
        status_label.config(text=f"You already guessed '{letter.upper()}'.")
        return

    used_letters.add(letter)
    if letter in word:
        update_guessed(letter)
        status_label.config(text=f"Good guess! '{letter.upper()}' is in the word.")
    else:
        chances -= 1
        status_label.config(text=f"Wrong guess! '{letter.upper()}' is not in the word. {chances} chances left.")
    
    stop_timer() # Stop timer after guess
    update_display()
    start_timer() # Start timer for next guess, moved here

    if '_' not in guessed:
        status_label.config(text="Congratulations! You guessed the word!")
        disable_buttons()
        stop_timer()
    elif chances <= 0:
        status_label.config(text=f"You lost! The word was '{word}'.")
        disable_buttons()
        stop_timer()

def update_guessed(letter):
    for index, char in enumerate(word):
        if char == letter:
            guessed[index] = letter

def update_display():
    word_label.config(text=' '.join(guessed))
    chances_label.config(text=f"Chances left: {chances}") # Update chances label

def disable_buttons():
    for btn in buttons:
        btn.config(state='disabled')

def reset_game():
    global word, guessed, chances, used_letters, timer_active
    word = random.choice(someWords)
    guessed = ['_' for _ in word]
    chances = len(word) + 2
    used_letters = set()
    word_label.config(text=' '.join(guessed))
    status_label.config(text=f"You have {chances} chances. Start guessing!")
    chances_label.config(text=f"Chances left: {chances}") # Update chances label
    for btn in buttons:
        btn.config(state='normal') # Enable buttons
    stop_timer() # Stop any existing timer
    timer_active = False # Reset timer active flag
    start_timer() # Start timer for new game

def exit_game():
    root.destroy()

def handle_keypress(event):
    if not timer_active:
        start_timer()
    letter = event.char.lower()
    if 'a' <= letter <= 'z':
        guess(letter)

# Create the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a label to show the timer
timer_label = tk.Label(root, text="Time: 20", font=('Helvetica', 14))
timer_label.pack(pady=5)

# Create a label to show chances
chances_label = tk.Label(root, text=f"Chances left: {chances}", font=('Helvetica', 14))
chances_label.pack(pady=5)

# Create a label to show the word to guess
word_label = tk.Label(root, text=' '.join(guessed), font=('Helvetica', 24))
word_label.pack(pady=20)

# Create a label to show the game status
status_label = tk.Label(root, text=f"You have {chances} chances. Start guessing!", font=('Helvetica', 14))
status_label.pack(pady=10)

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack()

# Create buttons for each letter
buttons = []
for ascii_code in range(97, 123):  # ASCII codes for a-z
    letter = chr(ascii_code)
    btn = tk.Button(frame, text=letter.upper(), command=lambda l=letter: guess(l), width=4, height=2)
    btn.pack(side='left', padx=2, pady=2)
    buttons.append(btn)

# Create reset and exit buttons
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(side='left', padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(side='right', padx=10, pady=10)

# Bind keyboard input
root.bind("<KeyPress>", handle_keypress)

# Start the game and timer
reset_game()

# Run the application
root.mainloop()
