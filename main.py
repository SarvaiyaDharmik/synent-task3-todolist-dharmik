import json
import os

FILE_NAME = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved tasks.")
            return []
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        json.dump(tasks,file,indent=4)

#Add a new task
def add_task(tasks):
    task = input("Enter your new task:").strip()

    if not task:
        print("Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task addes successfully!")

#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n==== YOUR TASKS =====")

    for index, task in enumerate(tasks,start=1):
        print(f"{index}. {task}") 

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Deleted successfully: {deleted_task}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n========== To-Do LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nEnter Your choice (1-4):").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks) 

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

if __name__ == "__main__":
    main()
