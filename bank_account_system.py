class BankAccount:
    def __init__(self, username, balance = 0.0):
        self.username = username
        self.balance = balance
     
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. Current balance : {self.balance}")
        else:
            print("deposit amount must be positive. ")
        
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
               self.balance -= amount
            print(f"{amount} has been withdrawn. Current balance: {self.balance}")
        else:
            print("no sufficient balance")
    
    def check_balance(self):
                print(f"current balance : {self.balance}")

username = input('Enter a name : ')         
account = BankAccount(username)

while True:
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Quit')
    choice = input("Enter your choice : ")
    if choice == '1':
        amount = float(input("Enter an amount to deposit : "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter an amount to withdraw : "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        break

