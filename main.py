# title of project (To-Do list)



print("To-Do List\n")
print("Welcome to Your To-Do list app. ")

 
 #Add item to list (in array)
def add_list():
    task = input("Add Task\n ").lower()
    Date_Task = input("Add Date\n ")
    To_Do_List.update({task: Date_Task})    
    
 #delete item off list (in array)
def delete_list():                                          
    task = input("Delete Task: ").lower()
    if task in To_Do_List:                               
        del To_Do_List[task]
        print("Task removed.")
    else:
        print("Task not found in the list.")


def main():
 
    while True:
        #display a menu for user
        print("To-Do List")
        print("1. Add Task ")
        print("2. Delete Task")
        print("3. Show List")
        print("4. Quit")
        choices = input("Choose an option 1-4")
     
        if choices == "1":
            add_list()
        elif choices == "2":
            delete_list()
        elif choices == "3":
            print(To_Do_List)
        elif choices == "4":
            print("Ending Program")
            break
        else:
            print("Invalid option. Please try again.")
            









if __name__=="__main__":
  main()


  
