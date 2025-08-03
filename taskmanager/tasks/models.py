from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
