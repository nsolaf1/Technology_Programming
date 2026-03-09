# Class: BankAccount
# Attributes:
#     owner
#     balance

# Methods:
#     deposit()
#     withdraw()
#     check_balance()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Succesfully Deposited: {amount}")
        print(f"New Balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Succesfully Widthdrawn: {amount}")
        print(f"New Balance: {self.balance}")
        

    def check_balance(self):
        print(f"Your balance is {self.balance}")


p1 = BankAccount("Elnura", 999)

# p1.check_balance()
p1.deposit(500)
p1.withdraw(99)
p1.check_balance()