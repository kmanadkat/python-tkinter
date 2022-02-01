import tkinter as tk

root = tk.Tk()

# Create Label Widget
myLabel = tk.Label(root, text="Hello World")

# Render On Screen
myLabel.pack()

# Event Loop
root.mainloop()