from rest_framework import serializers
from api.models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    """docstring for TodoListSerializer"""
    class Meta:
        model = TodoList
        fields = '__all__'
