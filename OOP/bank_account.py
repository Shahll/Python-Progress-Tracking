class BankAccount:
    def __init__(self):
        self.account = 0
        
    def deposit(self, amount):
        self.account += amount
        return f"You deposit {amount}"
    
    def withdraw(self, amount):
        self.account -= amount
        return f"You withdraw {amount}"
    
    def get_balance(self):
        return f"Your balance is {self.account}"
    

bank = BankAccount()
print(bank.deposit(123))
print(bank.get_balance())
print(bank.withdraw(100))
print(bank.get_balance())
