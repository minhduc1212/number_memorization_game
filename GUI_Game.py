import random
import tkinter as tk
from time import sleep

class NumberMemorizationGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Memorization Game")
        self.a = 3
        self.list_of_numbers = []
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to the Number Memorization Game!")
        self.label.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        self.entries = []
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_numbers)
        self.submit_button.pack()

    def start_game(self):
        self.label.config(text="You will be shown a number and you have to memorize it.\nYou will be asked to enter the number after a few seconds.")
        self.root.update()
        sleep(1)
        self.label.config(text="1")
        self.root.update()
        sleep(1)
        self.label.config(text="2")
        self.root.update()
        sleep(1)
        self.label.config(text="3")
        self.root.update()
        sleep(1)
        self.label.config(text="Let's start!")
        self.root.update()
        self.list_of_numbers = self.random_number(self.a)
        sleep(2)
        self.label.config(text="Enter the numbers you saw:")
        self.root.update()
        self.create_entry_fields()

    def random_number(self, a):
        list_of_numbers = []
        for i in range(a):
            g_n = random.randint(1, 9)
            list_of_numbers.append(g_n)
            self.label.config(text=f'number_{i} is: {g_n}')
            self.root.update()
            sleep(1)
        return list_of_numbers

    def create_entry_fields(self):
        for entry in self.entries:
            entry.destroy()
        self.entries = []
        for i in range(self.a):
            entry = tk.Entry(self.input_frame)
            entry.pack(side=tk.LEFT)
            self.entries.append(entry)

    def check_numbers(self):
        correct = True
        for i in range(self.a):
            f_input = int(self.entries[i].get())
            if f_input != self.list_of_numbers[i]:
                correct = False
                break
        if correct:
            self.label.config(text="Congratulations! You got all the numbers right!")
            self.a += 1
            self.start_game()
        else:
            self.label.config(text=f"Sorry! You got some numbers wrong. Try again!\nThe correct numbers were: {self.list_of_numbers}\nYour points are: {self.a - 3}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberMemorizationGame(root)
    root.mainloop()