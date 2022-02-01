import tkinter as tk
from tkmacosx import Button

root = tk.Tk()

# Button Action
def clickHandler():
    myLabel = tk.Label(root, text="You clicked a button!!")
    myLabel.pack() 

# Create Button Widget
myButton = Button(
    root, text="Click me",
    padx=24, pady=12, command=clickHandler,
    bg="#2563eb", fg="#ffffff",
)

# Render Button
myButton.pack()

# Event Loop
root.mainloop()