import tkinter as tk
from tkinter import messagebox

# Function to update the input field
def button_click(value):
    current = input_text.get()
    input_text.set(current + str(value))

# Function to clear the input field
def clear_field():
    input_text.set("")

# Function to evaluate the expression
def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        input_text.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Input field
input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, font=("Arial", 20), bd=8, insertwidth=2, width=14, justify="right")
input_field.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 15), bg="lightgreen", 
                  command=calculate).grid(row=row, column=col, sticky="nsew")
    elif button == "C":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 15), bg="lightcoral", 
                  command=clear_field).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 15), bg="lightgray", 
                  command=lambda b=button: button_click(b)).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Adjust row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
