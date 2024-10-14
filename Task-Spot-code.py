####################################
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
