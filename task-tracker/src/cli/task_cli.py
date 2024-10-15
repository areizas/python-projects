from services.task_service import TaskService
from models.task import Task

class TaskCLI:
  def __init__(self, *args, **kwargs):
    self.service = kwargs.get('service')
    self.args = args[0]

  def run(self):

    match self.args[1]:
      case 'add':
        task_id = self.service.get_next_id()
        task = Task(id=task_id, description=self.args[2:][0])
        self.service.add_task(task)
      case 'update':
        task_id = int(self.args[2])
        self.service.update_task_description(task_id,self.args[3:][0])
      case 'delete':
        task_id = int(self.args[2])
        self.service.delete_task(task_id)
      case 'mark-in-progress':
        task_id = int(self.args[2])
        self.service.update_task_status(task_id,'IN-PROGRESS')
      case 'mark-done':
        task_id = int(self.args[2])
        self.service.update_task_status(task_id,'DONE')
      case 'list':
        if len(self.args) < 3:
          print("\n".join(self.service.list_tasks()))
        else:
          match self.args[2]:
            case 'done':
              print("\n".join(self.service.list_task_by_status('DONE')))
            case 'todo':
              print("\n".join(self.service.list_task_by_status('TODO')))
            case 'in-progress':
              print("\n".join(self.service.list_task_by_status('IN-PROGRESS')))
            case _:
              print("Status is not identified. Try: done, todo, in-progress")
      case _:
        print("Command is not allowed.")
