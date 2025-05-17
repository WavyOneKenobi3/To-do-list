
class TaskMaker:
  def __init__(self, duty, priorities = "Low", due_date = None, completion_status = False)
    self.duty = duty 
    self.priorities = priorities 
    self.due_date = due_date
    self.completion_status = completion_status





  def status(self):
    self.completion_status = True
    return self.completion_status
    
    
