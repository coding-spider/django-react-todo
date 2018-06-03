from django.db import models
from . import BaseModel, TodoList

class TodoListItem(BaseModel):
    """docstring for TodoListItem"""
    todoList = models.ForeignKey(TodoList, on_delete = models.PROTECT, db_column = 'fk_id_todo_list')
    description = models.CharField(max_length = 255)

    class Meta:
        db_table = 'todo_list_item'
