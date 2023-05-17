import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.root = tk.Tk()
        self.root.title("Guess the Number Game")

        self.label = tk.Label(self.root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.target_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.target_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

game = GuessNumberGame()
game.root.mainloop()
