from django.db import models
from . import BaseModel, TodoList

class TodoListItem(BaseModel):
    """docstring for TodoListItem"""

    STATUSES = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED')
    )

    todoList = models.ForeignKey(TodoList, on_delete = models.PROTECT, db_column = 'fk_id_todo_list')
    description = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255, default = 'PENDING', choices = STATUSES)

    class Meta:
        db_table = 'todo_list_item'
