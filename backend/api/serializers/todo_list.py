from rest_framework import serializers
from api.models import TodoList
from api.serializers import TodoListItemSerializer

class TodoListSerializer(serializers.ModelSerializer):
    """docstring for TodoListSerializer"""
    todoListItems = TodoListItemSerializer(many = True, read_only = True)

    class Meta:
        model = TodoList
        fields = '__all__'
