# title of project (To-Do list)



print("To-Do List\n")
print("Welcome to Your To-Do list app. ")


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


  
