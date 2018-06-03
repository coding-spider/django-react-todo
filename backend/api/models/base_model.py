from django.db import models

class BaseModel(models.Model):
    """docstring for BaseModel"""
    isActive = models.BooleanField(default = True, db_column = 'is_active', db_index = True)
    createdDate = models.DateTimeField(auto_now_add = True, db_column = 'created_date', db_index = True)
    lastModifiedDate = models.DateTimeField(auto_now = True, db_column = 'last_modified_date', db_index = True)

    class Meta:
        abstract = True
