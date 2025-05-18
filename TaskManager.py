from Taskmaker import TaskMaker

class TaskManager:
  def __init__(self):
    #array for the the to-do list 
    self.to_do_list = []

  
   #Add item to list (in array)
    def add_list(self):
      # Asking user for input
      duty = input(f'What task are you adding? ')
      priorities = input(f'How important is this task? Low, Medium or High ')
      due_date = input(f'Whats the due date for this task? mm/yyyy ')

      new_task = TaskMaker(duty, priorities, due_date)
      self.to_do_list.append(new_task)

      print(f'Task added: {duty} with {priorities} priorities and due on {due_date}.')
      
   #delete item off list (in array)
    def delete_list(self):                                          
      #checks if anything in the list
      if not self.to_do_list:
        print(f'No Task currently')
        return

      print(f'Here are you Task that you currently have to do. ')
      for idx, TaskMaker in enumerate(self.to_do_list):
        print(f'{idx}. {TaskMaker}')

      try:
        task_index = int(input(f'Enter the index of the task you want to delete: '))

        if 0 <= task_index < len(self.to_do_list):
          delete_task = self.to_do_list.pop(task_index)
          print(f'Task delete: {delete_task}')
        else:
          print(f'Invalid index. Please try again. ')
      except ValueError:
        print(f'Invalid input. Please enter a valid index.')
        
