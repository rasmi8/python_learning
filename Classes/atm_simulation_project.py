# ATM simulation mini project using OOPS Concept 

class bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient balance. Try a smaller amount ")
        else:
            self.balance = self.balance - amount
            return self.balance
    
    def check_balance(self):
        return self.balance

    def run_atm(self):
         
        while True:
            print("\n ATM Menu \n")
            print("1 : To check Account details")
            print("2: To deposit")
            print("3: To withdraw")
            print("4: To check balance")
            print("5: To Exit")
            
            choice = input("enter your choice: \n")
            
            
            if choice == '1':
                
                    for c in customer:
                        if c.name.lower() == name.lower():
                            print(f"{c.name} : You are an existing customer: your balance is {c.check_balance()}")
                            break
                    else:
                        print("Account not found")
                            
            elif choice == '2':
                
                amount = int(input("Enter an amount to deposit \n "))
                
                for c in customer:
                    if c.name.lower() == name.lower():
                        original_balance = c.balance
                        c.deposit(amount)
                        print(f"original balance : {original_balance} :Deposited {amount} : New balance : {c.balance}")
                        break
                
            elif choice == '3':
                
                amount = int(input("Enter an amount to withdraw \n "))
                
                for c in customer:
                    if c.name.lower() == name.lower():
                            if amount > c.balance:
                                print("Insufficient balance, Try a smaller amount : ")
                            if amount < c.balance:
                                original_balance = c.balance
                                c.withdraw(amount)
                                print(f"original balance  {original_balance} : Withdrawn {amount}: New balance: {c.balance}")
                                break
            elif choice == '4':
                
                for c in customer:
                    if c.name.lower() == name.lower():
                        print(f"Balance: {c.check_balance()}")
                        break
                
            elif choice =='5':
                print("Thank you for banking with us. good bye!!")
                break
            else:
                print("Invalid input. Select options from the menu")
       
customer = [
    bankaccount('rasmi', 100),
    bankaccount('ishan', 200),
    bankaccount('mama', 300),
    bankaccount('baba', 500),
    bankaccount('babu', 600),
    bankaccount('chandu', 700),
    
]

name = input("Enter your name: \n ").strip()

for c in customer:
    if c.name.lower() == name.lower():
        c.run_atm()
    


        

       
   
   
   
