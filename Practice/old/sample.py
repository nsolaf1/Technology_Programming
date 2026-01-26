import tkinter as tk

def convert_feet_to_meters():
    try:
        feet = float(feet_entry.get())
        meters = feet * 0.3048
        result_label.config(text=f"{feet} feet = {meters:.2f} meters")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def convert_fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator with Conversion")

# Entry field for calculator input
entry = tk.Entry(root, width=20, font=("Arial", 14), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Conversion section
feet_label = tk.Label(root, text="Feet:", font=("Arial", 12))
feet_label.grid(row=6, column=0)
feet_entry = tk.Entry(root, font=("Arial", 12))
feet_entry.grid(row=6, column=1)
feet_convert_button = tk.Button(root, text="Convert to M", font=("Arial", 12), command=convert_feet_to_meters)
feet_convert_button.grid(row=6, column=2)

fahrenheit_label = tk.Label(root, text="Fahrenheit:", font=("Arial", 12))
fahrenheit_label.grid(row=7, column=0)
fahrenheit_entry = tk.Entry(root, font=("Arial", 12))
fahrenheit_entry.grid(row=7, column=1)
fahrenheit_convert_button = tk.Button(root, text="Convert to C", font=("Arial", 12), command=convert_fahrenheit_to_celsius)
fahrenheit_convert_button.grid(row=7, column=2)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=8, column=0, columnspan=4)

root.mainloop()
