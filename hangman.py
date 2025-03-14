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

def guess(letter):
    global chances
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
    
    update_display()

    if '_' not in guessed:
        status_label.config(text="Congratulations! You guessed the word!")
        disable_buttons()
    elif chances <= 0:
        status_label.config(text=f"You lost! The word was '{word}'.")
        disable_buttons()

def update_guessed(letter):
    for index, char in enumerate(word):
        if char == letter:
            guessed[index] = letter

def update_display():
    word_label.config(text=' '.join(guessed))

def disable_buttons():
    for btn in buttons:
        btn.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Hangman Game")

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

# Run the application
root.mainloop()
