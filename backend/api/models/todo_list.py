from django.db import models
from . import BaseModel

class TodoList(BaseModel):
    """docstring for TodoList"""
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)

    class Meta:
        db_table = 'todo_list'
