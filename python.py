tasks = []

# Function to display menu
def display_menu():
 print("1. Add Task")
 print("2. View Tasks")
 print("3. Delete Task")
 print("4. Quit")

# Function to add a task
def add_task():
 task = input("Enter a task: ")
 tasks.append(task)
 print("Task added!")

# Function to view tasks
def view_tasks():
 print("Tasks:")
 for i, task in enumerate(tasks, 1):
  print(f"{i}. {task}")

# Function to delete a task
def delete_task():
 task_number = int(input("Enter the task number to delete: "))
 if task_number > 0 and task_number <= len(tasks):
  tasks.pop(task_number - 1)
  print("Task deleted!")
 else:
  print("Invalid task number!")

# Main loop
while True:
 display_menu()
 choice = input("Choose an option: ")
 if choice == "1":
  add_task()
 elif choice == "2":
  view_tasks()
 elif choice == "3":
  delete_task()
 elif choice == "4":
  break
 else:
  print("Invalid choice!")