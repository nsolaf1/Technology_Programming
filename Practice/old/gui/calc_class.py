import tkinter as tk
import math


class BaseCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.expression = ""
        self.equation = tk.StringVar()
        self.create_widgets()
        self.create_base_buttons()

    def create_widgets(self):
        entry = tk.Entry(self,
                         textvariable=self.equation,
                         font=('Arial', 20),
                         bg='white',
                         fg='black',
                         borderwidth=2,
                         relief='sunken',
                         justify='right')
        entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'Clear':
            self.clear()
        else:
            self.expression += str(char)
            self.equation.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def create_base_buttons(self):
        base_buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('Clear', 5, 3)
        ]

        for (text, row, col) in base_buttons:
            bg_color = '#FF6B6B' if text in '+-*/=.' else '#4ECDC4'
            fg_color = 'white' if text in '+-*/=.' else 'black'

            action = lambda x=text: self.on_button_click(x)
            button = tk.Button(self,
                               text=text,
                               font=('Arial', 14),
                               fg=fg_color,
                               bg=bg_color,
                               command=action,
                               borderwidth=1,
                               relief='raised')
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

        # Configure grid weights for responsive resizing
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)


class StandardCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.title("Standard Calculator")
        self.geometry("300x400")
        self.configure(bg='#2D2D2D')
        self.minsize(250, 350)


class ScientificCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.configure(bg='#34495E')
        self.create_scientific_buttons()
        self.minsize(350, 450)

    def calculate(self):
        try:
            expr = self.expression
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('√', 'math.sqrt')
            result = str(eval(expr))
            self.equation.set(result)
            self.expression = result
        except:
            self.equation.set(" error ")
            self.expression = ""

    def create_scientific_buttons(self):
        scientific_buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('√', 1, 2), ('(', 1, 3), (')', 1, 4)
        ]

        for (text, row, col) in scientific_buttons:
            action = lambda x=text: self.on_button_click(x)
            button = tk.Button(self,
                               text=text,
                               font=('Arial', 14),
                               fg='white',
                               bg='#45B7D1',
                               command=action,
                               borderwidth=1,
                               relief='raised')
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')


if __name__ == "__main__":
    # app = StandardCalculator()  
    app = ScientificCalculator()  
    app.mainloop()