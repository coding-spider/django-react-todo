from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import TodoList
from api.serializers import TodoListSerializer

class TodoListView(APIView):
    """docstring for TodoListView"""

    def get(self, request, format=None):
        todoLists = TodoList.objects.all()
        serializer = TodoListSerializer(todoLists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

