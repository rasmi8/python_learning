class bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def check_balance(self):
        print("balance is : ", self.balance)
        
c = bankaccount('rashmi', 10)

c.check_balance()
c.deposit(10)
c.withdraw(5)
c.check_balance()

# Modify mutiple objects
