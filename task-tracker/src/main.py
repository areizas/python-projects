from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from cli.task_cli import TaskCLI
import sys


if __name__ == '__main__':
  repository = TaskRepository('data/tasks.json')
  service = TaskService(repository)
  cli = TaskCLI(sys.argv,service=service)
  cli.run()