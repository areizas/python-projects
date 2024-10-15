from repositories.task_repository import TaskRepository
from models.task import Task

class TaskService:
  def __init__(self, repository: TaskRepository):
    self.repository = repository
    self.tasks = self.repository.load()

  def add_task(self,task):
    self.tasks.append(task)
    self.repository.save(self.tasks)

  def delete_task(self, task_id):
    self.tasks = [ task for task in self.tasks if task.id != task_id ]
    self.repository.save(self.tasks)

  def get_task(self, task_id):
    for task in self.tasks:
      if task.id == task_id:
        return task
    return None

  def get_next_id(self):
    return max([task.id for task in self.tasks]) + 1 if len(self.tasks) > 0 else 1

  def list_tasks(self):
    return [str(task.__dict__) for task in self.tasks]

  def list_task_by_status(self,status):
    return [str(task.__dict__) for task in self.tasks if task.status == status]

  def update_task_description(self, task_id, description):
    for i in range(len(self.tasks)):
      if self.tasks[i].id == task_id:
        self.tasks[i].update_description(description)
        self.repository.save(self.tasks)

  def update_task_status(self, task_id, status):
    for i in range(len(self.tasks)):
      if self.tasks[i].id == task_id:
        self.tasks[i].update_status(status)
        self.repository.save(self.tasks)
      
        