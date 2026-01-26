import tkinter as tk


class Calculator():
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("270x200")
        self.root.configure(background="light blue")

        # Entry field for displaying input/output
        self.expression = ""
        self.equation = tk.StringVar()

        entry_field = tk.Entry(root, textvariable=self.equation, font=("Arial", 14), justify="right")
        entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=5, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, font=("Arial", 12), bg="white", 
                      command=lambda t=text: self.on_button_click(t), height=2, width=7).grid(row=row, column=col, pady=2)

    def on_button_click(self, button_text):
        if button_text == "=":
            self.calculate()
        elif button_text == "C":
            self.clear()
        else:
            self.expression += button_text
            self.equation.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))  # Safer than eval()
            self.equation.set(result)
            self.expression = result  # Store the result for further calculations
        except Exception:
            self.equation.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
