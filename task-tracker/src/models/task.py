from datetime import datetime

class Task:
  
  def __init__(self, *args, **kwargs ):
    self.id = kwargs.get('id')
    self.description = kwargs.get('description')
    self.status = kwargs.get('status','TODO')
    self.createdAt = kwargs.get('createdAt',datetime.today().isoformat())
    self.updatedAt = kwargs.get('updatedAt',datetime.today().isoformat())

  def update_description(self, description):
    self.description = description

  def update_status(self, status):
    match status:
        case 'TODO':
          self.status = 'TODO'
        case 'IN-PROGRESS':
          self.status = 'IN-PROGRESS'
        case 'DONE':
          self.status = 'DONE'
        case _:
          print('Not allowed status. Please select one of: TODO, IN-PROGRESS, DONE')

if __name__ == '__main__':
  task = Task(1,"description")
  print(f"task.id: {task.id}")
  print(f"task.description: {task.description}")
  print(f"task.status: {task.status}")
  print(f"task.createdAt: {task.createdAt}")
  print(f"task.updatedAt: {task.updatedAt}")