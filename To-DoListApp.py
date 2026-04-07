"""
Goal:
    -Add tasks
    -View tasks
    -Delete tasks
    -Save tasks for future use
Basic Structure:
    -List - store tasks
    -Functions - separate features
    -Loop - keep program running
    File handling - save and load data
"""

# To-Do List App
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        print("\nYour Tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i + 1}.  {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print("Removed:", removed)
        else:
            print("Invalid index")
    except:
        print("Enter valid number")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
      try:
          with open("tasks.txt", "r") as file:
              for line in file:
                  tasks.append(line.strip( ))
      except:
          pass

load_tasks()
while True:
    print("\n1. view Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_tasks()
        print("Task saved.  Exiting....")
        break
    else:
        print("Invalid choice")
        
