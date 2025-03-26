from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Task
from .serializers import TaskSerializer, UserSerializer

class TaskCreateView(APIView):
    """API to create a new task."""
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskAssignView(APIView):
    """API to assign a task to one or multiple users."""
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        user_ids = request.data.get('assigned_to', [])
        users = User.objects.filter(id__in=user_ids)
        if len(user_ids) != users.count():
            return Response({"error": "One or more users not found"}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_to.add(*users)
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)


class TaskListView(APIView):
    """API to get all tasks assigned to a specific user."""
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserCreateView(APIView):
    """API to create a new user."""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)