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
###################################################################################
tasks = []

def addTask():
    task = input("PLease enter a task!: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list. )
          
def listTasks():
    if not tasks:
        print("There are no tasks there currently!")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}"))
            
        ## Task #1 take out the groceries!
        
def deleteTask():
    listTasks()
    try:
        taskToDelete - int(input("Enter the # to delete"))
        if taskToDelete < len(tasks):
            tasks.pop(taksToDelete)
            print(f"Task '{taskToDelete}' has been removed.)
            else
        
    except:
        print("Invalid statement")
        
if __name__ == "__main__":
    # Creating a loop to run the app
print(" Welcome to TaskiD0!- the to-do list app :) ")
while True:
    print(\n)
    print("Please select the following options: ")
    print("-------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List a task")
    print("4. Quit")
    
choice = input("Enter your choice: ")

if(choice == "1"):
 addTask()   
elif(choice == "2"):
 deleteTask()
elif(choice == "3"):
 listTask()
elif(choice == "4"):
    break
else:
    print("Invalid input. Please try again.")
    
    print("GoodBye! ✋✋🤟")
