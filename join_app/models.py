from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=20)  
    shortcut = models.CharField(max_length=2)
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return self.name
class Subtask(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    dueDate = models.DateTimeField()  
    position = models.IntegerField()  
    prio = models.CharField(max_length=20, choices=[("low", "Low"), ("medium", "Medium"), ("urgent", "Urgent")])  
    status = models.CharField(max_length=50, choices=[("todo", "To Do"), ("inProgress", "In Progress"), ("awaitFeedback", "Await Feedback"), ("done", "Done")])
    assignTo = models.ManyToManyField(Contact, related_name="tasks")  
    subtasks = models.ManyToManyField(Subtask, related_name="tasks", blank=True) 

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=250)
    tasks = models.ManyToManyField(Task, related_name="users", blank=True)
    contacts = models.ManyToManyField(Contact, related_name="users", blank=True)

    def __str__(self):
        return self.name
