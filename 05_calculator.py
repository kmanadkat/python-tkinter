import tkinter as tk

root = tk.Tk()
root.title("Mini Calculator")

# Input Field
inputField = tk.Entry(root, width=31, borderwidth=4)
inputField.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

previousNumber = 0
operation = ""

def buttonClick(number):
    currentNumber = inputField.get()
    inputField.delete(0, tk.END)
    inputField.insert(0, str(currentNumber) + str(number))
    return

def buttonAdd():
    global previousNumber
    global operation
    operation = "+"
    previousNumber = int(inputField.get())
    inputField.delete(0, tk.END)
    return

def buttonSubtract():
    global previousNumber
    global operation
    operation = "-"
    previousNumber = int(inputField.get())
    inputField.delete(0, tk.END)
    return

def buttonMultiply():
    global previousNumber
    global operation
    operation = "*"
    previousNumber = int(inputField.get())
    inputField.delete(0, tk.END)
    return

def buttonDivide():
    global previousNumber
    global operation
    operation = "/"
    previousNumber = int(inputField.get())
    inputField.delete(0, tk.END)
    return

def buttonEqual():
    global previousNumber
    global operation
    currentNumber = int(inputField.get())
    inputField.delete(0, tk.END)
    result = 0
    if operation == "+":
        result = previousNumber + currentNumber
    elif operation == "-":
        result = previousNumber - currentNumber
    elif operation == "*":
        result = previousNumber * currentNumber
    elif operation == "/":
        result = previousNumber / currentNumber
    
    inputField.insert(0, str(result))
    return

def buttonClear():
    inputField.delete(0, tk.END)
    return

# Buttons
button1 = tk.Button(root, text=1, padx=40, pady=20, command=lambda: buttonClick(1))
button2 = tk.Button(root, text=2, padx=40, pady=20, command=lambda: buttonClick(2))
button3 = tk.Button(root, text=3, padx=40, pady=20, command=lambda: buttonClick(3))
button4 = tk.Button(root, text=4, padx=40, pady=20, command=lambda: buttonClick(4))
button5 = tk.Button(root, text=5, padx=40, pady=20, command=lambda: buttonClick(5))
button6 = tk.Button(root, text=6, padx=40, pady=20, command=lambda: buttonClick(6))
button7 = tk.Button(root, text=7, padx=40, pady=20, command=lambda: buttonClick(7))
button8 = tk.Button(root, text=8, padx=40, pady=20, command=lambda: buttonClick(8))
button9 = tk.Button(root, text=9, padx=40, pady=20, command=lambda: buttonClick(9))
button0 = tk.Button(root, text=0, padx=40, pady=20, command=lambda: buttonClick(0))
buttonAdd = tk.Button(root, text='+', padx=39, pady=20, command=buttonAdd)
buttonEqual = tk.Button(root, text='=', padx=92, pady=20, command=buttonEqual)
buttonClear = tk.Button(root, text='Clear', padx=81, pady=20, command=buttonClear)

buttonSubtract = tk.Button(root, text='-', padx=39, pady=20, command=buttonSubtract)
buttonMultiply = tk.Button(root, text='*', padx=41, pady=20, command=buttonMultiply)
buttonDivide = tk.Button(root, text='/', padx=41, pady=20, command=buttonDivide)


# Render Buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)

buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0) 
buttonMultiply.grid(row=6, column=1) 
buttonDivide.grid(row=6, column=2) 

# Event Loop
root.mainloop()