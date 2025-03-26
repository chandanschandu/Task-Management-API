from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False  # Make this field optional
    )

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'created_at', 'completed_at',
            'status', 'task_type', 'assigned_to'
        ]