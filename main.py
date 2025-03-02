import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x300")  # Set initial window size
        self.root.resizable(True, True)  # Allow window resizing

        # Generate a random number between 1 and 100
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # UI Elements
        self.label = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Arial", 12))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number in {self.attempts} attempts!")
                self.root.destroy()  # Close the game after winning
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()