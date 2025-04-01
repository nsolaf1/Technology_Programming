import tkinter as tk

class QuadraticCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quadratic Equation Solver")
        self.geometry("400x300")
        self.configure(bg='#34495E')

        # Equation display field
        self.equation = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.equation, font=('Arial', 18), bg='white', fg='black', justify='center')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Input fields for a, b, and c
        self.a_entry = tk.Entry(self, font=('Arial', 14))
        self.a_entry.grid(row=1, column=0, padx=5, pady=5)
        self.a_entry.insert(0, "a")

        self.b_entry = tk.Entry(self, font=('Arial', 14))
        self.b_entry.grid(row=1, column=1, padx=5, pady=5)
        self.b_entry.insert(0, "b")

        self.c_entry = tk.Entry(self, font=('Arial', 14))
        self.c_entry.grid(row=1, column=2, padx=5, pady=5)
        self.c_entry.insert(0, "c")

    # Solve button
    quad_button = tk.Button(self, text="Solve Quadratic", font=('Arial', 14), bg='#FFA500', fg="white", command=self.solve_quadratic)
    quad_button.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

    def my_sqrt(self, x):
    # """Manual square root calculation using Newton's method."""
    
        if x < 0:
            return None # No real solutions
        guess = x / 2.0
        for _ in range(10): # More iterations improve accuracy
            guess = (guess + x / guess) / 2.0
            return guess

    def solve_quadratic(self):
        # """Solves the quadratic equation ax² + bx + c = 0"""
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())

        if a == 0:
            self.equation.set("Not a quadratic equation")
            return

        D = b**2 - 4*a*c # Discriminant

        if D < 0:
            self.equation.set("No Real Solutions")
            return

        sqrt_D = self.my_sqrt(D)
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)

        if D == 0:
            self.equation.set(f"x = {x1:.3f}")
        else:
             self.equation.set(f"x = {x1:.3f}")
                

 

if __name__ == "__main__":
    app = QuadraticCalculator()
    app.mainloop()