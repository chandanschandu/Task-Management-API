from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    TASK_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default='personal')
    assigned_to = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name