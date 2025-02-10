tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "[✔]" if task["completed"] else "[ ]"
            print(f"{index}. {status} {task['task']}")

def add_task():
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully!")

def complete_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
