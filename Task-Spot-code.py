def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'rb') as file:
            return pickle.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASK_FILE, 'wb') as file:
        pickle.dump(tasks, file)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    """Remove a task by its number."""
    display_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
