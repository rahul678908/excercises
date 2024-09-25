class Bank_Account:
    def _init_(self, username):
        self.username = username
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} has been withdrawn. Current balance: {self.balance}")
            else:
                print("No sufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def quit(self):
        print(f"Thank you {self.username} for banking with us. Goodbye!")

        
# Menu-driven code to execute the BankAccount operations

def main():
    user_name = input("Enter your name: ")
    
    if user_name.lower() != "ajay":
        print("Invalid username, only 'Ajay' is allowed.")
        return

    account = Bank_Account(user_name)
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Quit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter an amount to deposit: "))
            account.deposit(amount)
        
        elif choice == 2:
            amount = float(input("Enter an amount to withdraw: "))
            account.withdraw(amount)
        
        elif choice == 3:
            account.check_balance()
        
        elif choice == 4:
            account.quit()
            break
        
        else:
            print("Invalid option. Please choose a valid action.")

