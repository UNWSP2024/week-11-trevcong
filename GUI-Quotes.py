#AUTHOR: Trevor Conger
#DATE: 11/15/2024
#TITLE: GUI Quotes


import tkinter as tk
import random


quotes = [
    "Artificial Intelligence, deep learning, machine learning — whatever you’re doing if you don’t understand it — learn it. Because otherwise, you’re going to be a dinosaur within 3 years.” – Mark Cuban",
    "The ability to learn is the most important quality a machine can possess. - Elon Musk",
    "We’re going to see more change in the next five years than we’ve seen in the last 50.” – Jack Ma",
    "AI-driven automation will continue to eliminate traditional jobs, but also create new opportunities and industries we can’t even imagine yet.” – Jensen Huang"
]


def update_quote():
    new_quote = random.choice(quotes)
    label.config(text=new_quote)

root = tk.Tk()
root.title("Favorite Saying")

label = tk.Label(root, text=quotes[0])
label.pack(pady=20)

button = tk.Button(root, text="New Quote", command=update_quote)
button.pack(pady=10)


root.mainloop()