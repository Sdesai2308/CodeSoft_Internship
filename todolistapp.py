#To-do list app
tasks=[]
TaskId = 1
def addTask():
    global TaskId
    taskTitle = str(input("Enter task title: "))
    CompletionTime =  float(input("Enter time for completion in hours"))
    tasks.append({"Id" : TaskId , "Title" : taskTitle , "Duration" : CompletionTime , "Status": "Pending"})
    print("Task added successfully")
    TaskId += 1
    
def updateTask():
    Id = int(input("Enter Task id :"))
    field = input("Enter field to update (Id / Title / Duration / Status) : ")
    value = input("Enter fields value: ")
    for task in tasks:
        if(task["Id"] == Id):
            task[field] = value             
    print("task updated")
    
def showTasks():
    for task in tasks:
        print( "Task Id: " ,task["Id"],"\tTitle: " ,task["Title"] ,"\tDuration: ",task["Duration"] , "\tStatus: " , task["Status"])
        
print("Choose 1 to add a task")
print("Choose 2 to update the task")
print("Choose 3 to see all assigned tasks")
print("Choose 4 to exit.")
status=True
while(status):
    choice = int(input("enter Your Choice: "))
    if(choice == 1):
        addTask()
    elif(choice == 2):
        updateTask()
    elif(choice == 3):
        showTasks()
    elif(choice == 4):
        status = False
    else:
        print("Wrong Choice")
