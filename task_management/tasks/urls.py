from django.urls import path
from .views import TaskCreateView, TaskAssignView, TaskListView, UserCreateView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/assign/<int:task_id>/', TaskAssignView.as_view(), name='task-assign'),
    path('tasks/user/<int:user_id>/', TaskListView.as_view(), name='task-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'), 
]