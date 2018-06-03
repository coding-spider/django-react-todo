from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """docstring for BaseModel"""
    isActive = models.BooleanField(default = True, db_column = 'is_active', db_index = True)
    createdDate = models.DateTimeField(auto_now_add = True, db_column = 'created_date', db_index = True)
    lastModifiedDate = models.DateTimeField(auto_now = True, db_column = 'last_modified_date', db_index = True)

    class Meta:
        abstract = True

class TodoList(BaseModel):
    """docstring for TodoList"""
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)

    class Meta:
        db_table = 'todo_list'


class TodoListItem(BaseModel):
    """docstring for TodoListItem"""
    todoList = models.ForeignKey(TodoList, on_delete = models.CASCADE, db_column = 'fk_id_todo_list')
    description = models.CharField(max_length = 255)

    class Meta:
        db_table = 'todo_list_item'


