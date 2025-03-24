from django.db import models
from django.contrib.auth.models import User

class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contacts")
    name = models.CharField(max_length=255, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)   
    phone = models.CharField(max_length=20, blank=True, null=True) 
    shortcut = models.CharField(max_length=2, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True) 
    
    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.email})"
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks") 
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    dueDate = models.IntegerField()
    position = models.IntegerField()
    prio = models.CharField(max_length=20, choices=[("Low", "Low"), ("Medium", "Medium"), ("Urgent", "Urgent")])
    status = models.CharField(max_length=50, choices=[("todo", "To Do"), ("inProgress", "In Progress"), ("awaitFeedback", "Await Feedback"), ("done", "Done")])
    assignTo = models.ManyToManyField(UserContact, related_name="tasks_list", blank=False)
    
    def __str__(self):
        return f"TASK_ID: [{self.id}] USER:{self.user} TITLE: {self.title}"


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"SUBTASK_ID: [{self.id}]{self.task}"
