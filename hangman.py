import tkinter as tk
import random
import string

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.someWords = '''apple banana mango strawberry 
        orange grape pineapple apricot lemon coconut watermelon 
        cherry papaya berry peach lychee muskmelon'''.split()
        
        self.word = random.choice(self.someWords)
        self.guessed = ['_' for _ in self.word]
        self.chances = len(self.word) + 2
        self.used_letters = set()
        self.timer_duration = 20
        self.timer_seconds = self.timer_duration
        self.timer_active = False
        self.timer_id = None
        
        self.timer_label = tk.Label(root, text=f"Time: {self.timer_seconds}", font=('Helvetica', 14))
        self.timer_label.pack(pady=5)
        
        self.chances_label = tk.Label(root, text=f"Chances left: {self.chances}", font=('Helvetica', 14))
        self.chances_label.pack(pady=5)
        
        self.word_label = tk.Label(root, text=' '.join(self.guessed), font=('Helvetica', 24))
        self.word_label.pack(pady=20)
        
        self.status_label = tk.Label(root, text=f"You have {self.chances} chances. Start guessing!", font=('Helvetica', 14))
        self.status_label.pack(pady=10)
        
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        self.buttons = []
        for letter in string.ascii_lowercase:
            btn = tk.Button(self.frame, text=letter.upper(), command=lambda l=letter: self.guess(l), width=4, height=2)
            btn.pack(side='left', padx=2, pady=2)
            self.buttons.append(btn)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(side='left', padx=10, pady=10)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(side='right', padx=10, pady=10)
        
        self.root.bind("<KeyPress>", self.handle_keypress)
        
        self.reset_game()
    
    def start_timer(self):
        self.timer_seconds = self.timer_duration
        self.timer_active = True
        self.update_timer_label()
        self.timer_id = self.root.after(1000, self.update_timer)
    
    def update_timer(self):
        if self.timer_active:
            self.timer_seconds -= 1
            self.update_timer_label()
            if self.timer_seconds <= 0:
                self.timer_active = False
                self.status_label.config(text=f"Time's up! You lost a chance.")
                self.chances -= 1
                self.update_display()
                if self.chances <= 0:
                    self.status_label.config(text=f"You lost! The word was '{self.word}'.")
                    self.disable_buttons()
                else:
                    self.start_timer() # Start timer again for the next guess
            else:
                self.timer_id = self.root.after(1000, self.update_timer)
    
    def stop_timer(self):
        self.timer_active = False
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
    
    def update_timer_label(self):
        self.timer_label.config(text=f"Time: {self.timer_seconds}")
    
    def guess(self, letter):
        if not self.timer_active:
            self.start_timer()
        if letter in self.used_letters:
            self.status_label.config(text=f"You already guessed '{letter.upper()}'.")
            return
        
        self.used_letters.add(letter)
        if letter in self.word:
            self.update_guessed(letter)
            self.status_label.config(text=f"Good guess! '{letter.upper()}' is in the word.")
        else:
            self.chances -= 1
            self.status_label.config(text=f"Wrong guess! '{letter.upper()}' is not in the word. {self.chances} chances left.")
        
        self.stop_timer() # Stop timer after guess
        self.update_display()
        self.start_timer() # Start timer for next guess, moved here
        
        if '_' not in self.guessed:
            self.status_label.config(text="Congratulations! You guessed the word!")
            self.disable_buttons()
            self.stop_timer()
        elif self.chances <= 0:
            self.status_label.config(text=f"You lost! The word was '{self.word}'.")
            self.disable_buttons()
            self.stop_timer()
    
    def update_guessed(self, letter):
        for index, char in enumerate(self.word):
            if char == letter:
                self.guessed[index] = letter
    
    def update_display(self):
        self.word_label.config(text=' '.join(self.guessed))
        self.chances_label.config(text=f"Chances left: {self.chances}") # Update chances label
    
    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state='disabled')
    
    def reset_game(self):
        self.word = random.choice(self.someWords)
        self.guessed = ['_' for _ in self.word]
        self.chances = len(self.word) + 2
        self.used_letters = set()
        self.word_label.config(text=' '.join(self.guessed))
        self.status_label.config(text=f"You have {self.chances} chances. Start guessing!")
        self.chances_label.config(text=f"Chances left: {self.chances}") # Update chances label
        for btn in self.buttons:
            btn.config(state='normal') # Enable buttons
        self.stop_timer() # Stop any existing timer
        self.timer_active = False # Reset timer active flag
        self.start_timer() # Start timer for new game
    
    def handle_keypress(self, event):
        if not self.timer_active:
            self.start_timer()
        letter = event.char.lower()
        if 'a' <= letter <= 'z':
            self.guess(letter)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
