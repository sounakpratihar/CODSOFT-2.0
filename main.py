import os

# Initialize the to-do list
todo_list = []

# Display menu
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Remove a Task")
    print("5. Exit")

# View the to-do list
def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Add a task to the list
def add_task():
    task = input("\nEnter the task to add: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Invalid input. Task cannot be empty.")

# Update a task in the list
def update_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(todo_list):
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    old_task = todo_list[task_number - 1]
                    todo_list[task_number - 1] = new_task
                    print(f"Task '{old_task}' updated to '{new_task}'.")
                else:
                    print("Invalid input. Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Remove a task from the list
def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()