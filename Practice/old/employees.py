class Employees:
    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
        self.email = name + "."+ last + "@company.com"
    
    def bonus(self):
        self.salary += 10000
    
    def __str__(self):
        return f'{self.name} {self.last} {self.salary}'
    
    

emp1 = Employees("Aman", "Esen", 40000)
emp2 = Employees("Lera", "Albina", 150000)

# emp1.first = "Aman"
# emp1.last = "Aman" 
# emp1.email = "aman.esen@companyt.com"

print(emp1.salary)
emp1.bonus()
print(emp1.salary)

print(emp2.salary)
emp2.bonus()
print(emp2.salary)

