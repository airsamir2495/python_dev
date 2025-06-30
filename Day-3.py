# Instructions
# Create a list called tasks and populate it with initial tasks: "Planning", "Design", "Coding", "Testing".
# Create another list called time_spent to store the time spent on each task. Initialize it with zeros.
# Create a function called log_time that takes a task name and an amount of time. It will find the task in the tasks list and update the corresponding time in time_spent.
# Use a while loop to repeatedly ask the user for a task and time spent on that task until they choose to exit.
# Use a for loop to go through the tasks and time_spent lists, printing out a summary of time spent on each task.


tasks = ["Planning", "Design", "Coding", "Testing"]
time_spent = [0,0,0,0]



def log_time(data,time):
    print('Data::',data,'Time::',time)
    for t in range(len(tasks)): 
        if (data in tasks[t]):
            time_spent[t]+=time

print("Tasks Categories::",tasks,"\nTo close the application type close")
while True:
    data = str(input('Enter Task:'))
    if (data =='close'): 
        print ("\n***********\n")
        break  
    else:
        if data in tasks:
            time = float(input("How many hours did you work?"))
            log_time(data,time)
        else:
            print("Wrong Task!!!")

   

for i in range(len(tasks)):
    print(f"Task:",tasks[i],"Hour Spend:",time_spent[i])

