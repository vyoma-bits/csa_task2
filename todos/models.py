from django.db import models
from django.contrib.auth.models import User 

class Todo(models.Model):
    title = models.CharField(max_length=255) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)  
    completed = models.BooleanField(default=False) 
    # I have not used these fields, I have plan to use these fields to show how much time did it take for the user to complete the task, will do it
    # created_at = models.DateTimeField(auto_now_add=True) 
    # updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title  


