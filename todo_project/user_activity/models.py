# user_activity/models.py
from django.db import models
from django.contrib.auth.models import User
from todo_app.models import Task

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"
