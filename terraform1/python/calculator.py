import tkinter as tk

# Function to update the entry field
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=calculate
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda t=text: click(t)
        )

    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    width=23,
    height=2,
    bg="red",
    fg="white",
    command=clear
)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()