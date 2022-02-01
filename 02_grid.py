import tkinter as tk

root = tk.Tk()

# Create Label Widget
myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="My Name Is Krupesh")

# Render On Screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Event Loop
root.mainloop()