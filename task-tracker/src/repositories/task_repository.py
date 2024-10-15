import json
import os
from models.task import Task

class TaskRepository:

  def __init__(self, filename):
    self.filename = filename
    if not os.path.exists(filename):
      with open(self.filename,'w') as file:
        file.write('[]')

  def load(self):
    try:
      with open(self.filename,'r') as file:
        data = json.load(file)
        return [Task(**item) for item in data ]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

  def save(self, tasks):
    with open(self.filename,'w') as file:
      json.dump([task.__dict__ for task in tasks],file)
