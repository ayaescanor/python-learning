tasks=[]
menue=int(input(" choose :1 FOR ADDING TASKS , 2 Edit Task, 3 Delete Task, 4 EXIT  "))
while True:
    if menue==1:
        user_new_task_toadd=input("enter the new task")
        tasks.append(user_new_task_toadd)
        print(" Task added successfully")
    elif menue==2:
        new_task=input("enter the new task: ")
        task_index=int(input("enter the index of the task you want to edit "))
        tasks[task_index]=new_task
        print("Task edited successfully")
    elif menue==3:
        task_index_todelete=int(input("enter the task index that you want to delet"))
        tasks.pop(task_index_todelete)
        print("Task deleted successfully")
    elif menue==4:
        break
    else:
        print("invalid option")
    





