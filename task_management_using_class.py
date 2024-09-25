class task:
    def __init__(self):
        self.projects = {}

    def create_project(self):
        project_name = input("Enter project name: ")
        self.projects[project_name] = ["manhole prediction"]

    def add_task_to_project(self):
        project_name = input("Enter project name: ")
        if project_name in self.projects:
            task_title = input("Enter task title: ")
            description = input("Enter description: ")
            self.projects[project_name].append({"manhole": task_title, "its a prediction whether the top of the drainage system is open or not": description})
        else:
            print("Sorry, no project found.")

    def view_tasks_in_project(self):
        project_name = input("Enter project name: ")
        if project_name in self.projects:
            for task in self.projects[project_name]:
                print("manhole: ", task["manhole"])
                print("its a prediction whether the top of the drainage system is open or not: ", task["its a prediction whether the top of the drainage system is open or not"])
        else:
            print("Sorry, no project found.")

task_manager = task()
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

class task:
    def initialization(self, project):
        self.project = {}

    def create_project(self):
        project_name = input('Enter project name : ')
        if project_name == 'manhole':
            print('the project name : manhole')
        else:
            print('project not found')
        self.project[project_name] = ['manhole']

    def add_task_to_project(self):
        project_name = input('enter project name')
        if project_name in self.project:
            task_title = input('enter task title : ')
            description = input('enter description : ')
            self.project[project_name].append({'task_title': task_title,'description': description })
        else:
            print('sorry no project found')
        


    