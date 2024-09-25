class TaskManagementSystem:
    def __init__(self):
        self.projects = {}

    def create_project(self):
        project_name = input("Enter project name: ")
        self.projects[project_name] = []
        
    def add_task_to_project(self):
        project_name = input("Enter project name: ")
        if project_name in self.projects:
            task_title = input("Enter task title: ")
            description = input("Enter description: ")
            self.projects[project_name].append({"task_title": task_title, "description": description})
        else:
            print("Sorry, no project found.")

    def view_tasks_in_project(self):
        project_name = input("Enter project name: ")
        if project_name in self.projects:
            for task in self.projects[project_name]:
                print("Task Title: ", task["task_title"])
                print("Description: ", task["description"])
        else:
            print("Sorry, no project found.")

task_manager = TaskManagementSystem()
while True:
    choice = input("1. Create project\n2. Add task to project\n3. View task in project\n4. Quit\nEnter your choice: ")
    if choice == '1':
        task_manager.create_project()
    elif choice == '2':
        task_manager.add_task_to_project()
    elif choice == '3':
        task_manager.view_tasks_in_project()
    elif choice == '4':
        break

# class BankAccount:
#     def _init_(self, username):
#         self.username = username
#         self.balance = 0

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} has been deposited.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if self.balance >= amount:
#                 self.balance -= amount
#                 print(f"{amount} has been withdrawn.")
#             else:
#                 print("No sufficient balance!")
#         else:
#             print("Withdrawal amount must be positive.")

#     def check_balance(self):
#         print(f"Current balance: {self.balance}")

#     def quit(self):
#         print(f"Thank you {self.username} for banking with us. Goodbye!")
        
# # Menu-driven code to execute the BankAccount operations

# def main():
#     user_name = input("Enter your name: ")
#     account = BankAccount(user_name)
    
#     while True:
#         print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Quit")
#         choice = int(input("Enter your choice: "))
        
#         if choice == 1:
#             amount = float(input("Enter an amount to deposit: "))
#             account.deposit(amount)
        
#         elif choice == 2:
#             amount = float(input("Enter an amount to withdraw: "))
#             account.withdraw(amount)
        
#         elif choice == 3:
#             account.check_balance()
        
#         elif choice == 4:
#             account.quit()
#             break
        
#         else:
#             print("Invalid option. Please choose a valid action.")

# if__name__ == "_main_":
#     main()