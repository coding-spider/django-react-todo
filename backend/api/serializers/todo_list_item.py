from rest_framework import serializers
from api.models import TodoListItem

class TodoListItemSerializer(serializers.ModelSerializer):
    """docstring for TodoListItemSerializer"""
    class Meta:
        model = TodoListItem
        fields = '__all__'


