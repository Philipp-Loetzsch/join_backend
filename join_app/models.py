from django.db import models
from django.contrib.auth.models import User

class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contacts")
    custom_name = models.CharField(max_length=255, blank=True, null=True) 
    custom_email = models.EmailField(blank=True, null=True)   
    custom_phone = models.CharField(max_length=20, blank=True, null=True) 
    custom_shortcut = models.CharField(max_length=2, blank=True, null=True)
    custom_color = models.CharField(max_length=7, blank=True, null=True) 
    
    def __str__(self):
        return f"{self.user.username} - {self.custom_name} ({self.custom_email})"


class Subtask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name="subtask")
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task} - {self.title}"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task") 
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    dueDate = models.DateField()
    position = models.IntegerField()
    prio = models.CharField(max_length=20, choices=[("low", "Low"), ("medium", "Medium"), ("urgent", "Urgent")])
    status = models.CharField(max_length=50, choices=[("todo", "To Do"), ("inProgress", "In Progress"), ("awaitFeedback", "Await Feedback"), ("done", "Done")])
    assignTo = models.ManyToManyField(UserContact, related_name="tasks_list", blank=True)
    subtasks = models.ManyToManyField(Subtask, related_name="tasks_list", blank=True)

    def __str__(self):
        return f"{self.user} - {self.title}"
