import tkinter as tk

root = tk.Tk()

# Labels
heading = tk.Label(root, text="Registeration Form", font="-weight bold", height=4)
firstNameLabel = tk.Label(root, text="First Name", fg="#737373")
secondNameLabel = tk.Label(root, text="Second Name", fg="#737373")
emailLabel = tk.Label(root, text="Email Id", fg="#737373")
passwordLabel = tk.Label(root, text="Password", fg="#737373")


# Input field
firstNameField = tk.Entry(width=18, bg="#f4f4f5")
secondNameField = tk.Entry(width=18, bg="#f4f4f5")
emailField = tk.Entry(width=38, bg="#f4f4f5")

password = tk.StringVar()
passwordField = tk.Entry(textvariable=password, show="*", width=38, bg="#f4f4f5")

def disableUI() :
    firstNameField.configure(state=tk.DISABLED)
    secondNameField.configure(state=tk.DISABLED)
    emailField.configure(state=tk.DISABLED)
    passwordField.configure(state=tk.DISABLED)
    myButton.configure(state=tk.DISABLED)

# Button Action
def clickHandler():
    firstName = firstNameField.get()
    emailId = emailField.get()
    message = tk.Label(root, text="Registeration successful!", fg="#15803d").grid(row=12, column=1, columnspan=2)
    greeting = tk.Label(root, text=f"Confirmation mail sent to {emailId}").grid(row=13, column=1, columnspan=2, pady=(0,24))
    myButton.configure(text="Completed")

    print(password.get())

    # Disable UI
    disableUI()


# Create Button Widget
myButton = tk.Button(root, text="Submit", padx=24, pady=8, command=clickHandler)


# Render Widgets
heading.grid(row=1, column=1, columnspan=2)

firstNameLabel.grid(row=2, column=1, padx=(24, 0), sticky= tk.W)
firstNameField.grid(row=3, column=1, padx=(24, 0), pady=(0, 12))

secondNameLabel.grid(row=2, column=2, padx=(0,24), sticky= tk.W)
secondNameField.grid(row=3, column=2, padx=(0,24), pady=(0, 12))

emailLabel.grid(row=5, column=1, columnspan=2, padx=24, sticky= tk.W)
emailField.grid(row=6, column=1, columnspan=2, padx=24, pady=(0, 12))

passwordLabel.grid(row=8, column=1, columnspan=2, padx=24, sticky= tk.W)
passwordField.grid(row=9, column=1, columnspan=2, padx=24)

myButton.grid(row=11, column=1, columnspan=2, pady=20)

# Event Loop
root.mainloop()