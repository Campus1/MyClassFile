# Assignment # 5
# Developer: Usman Zia
# Date: 07/28/2019
# Create The ToDo file will contain two columns of data (Task, Priority) which you store in a Python dictionary. 
# Each Dictionary will represent one row of data and these rows of data are added to a Python List to create a table of data.

# defined the path to my text file
infile = '/Users/uziad/Documents/Python Class/Foundation of Programming Python/Assignment & Module 5/ToDo.txt'
# read in ToDo.txt here using readlines
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
   

# created empty dictionary to store data as we loop 
taskdict = {} 

   
for line in lines:
    #split the line and pull out task by index
    task = line.split(',')[0].strip()
    priority = line.split(',')[1].strip()
    #dded new key to a dictionary here using task ask key and priority as value
    taskdict[task] = priority
 

#creating the while loop to ask question to users 
  
while True:
    print ("""
    Menu of Options
    1 - Show current data
    2 - Add a new item.
    3 - Remove an existing item.
    4 - Save Data to File
    5 - Exit Program
    """)
    
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

    # Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print('This is the current items in the table')
        print(taskdict)
    
    
  # Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        task = input("What is the task name?: ")
        priority = input("What is the level of priorty this task?: ") 
          # add a new key, value pair to the dictionary
        taskdict[task] = priority 
    # add a new key, value pair to the dictionary


    # Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        # locate key and delete it using del function
        del taskdict[remove_key]# locate key and delete it using del function


        # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        # open a file handle
        with open('todo_file.txt', 'w') as file:
        # loop through key, value and write to file
            for task, priority in taskdict.items():
                # formating the task and priority
                output = "{}, {}\n".format(task,priority)
                # printing to the file
                file.write(output)
                print(output)
                
    # Chocie 5- end the program
    elif (strChoice == '5'):
        print('The program has been ended')
        break #and Exit the program
      

    # I would be nice to have an option to resubmit previous assignment if the results are not as expected and received low grades
    # Also, comments/suggests to improve the submitted code.
    # Can we get the answer key once the assignment is submitted without an option of resubmitting the assignment.
