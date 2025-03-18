from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    shortcut = models.CharField(max_length=2)
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return self.name

class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_contacts")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="user_contacts", blank=True, null=True)
    custom_name = models.CharField(max_length=255, blank=True, null=True) 
    custom_email = models.EmailField(blank=True, null=True)   
    custom_phone = models.CharField(max_length=20, blank=True, null=True) 
    custom_shortcut = models.CharField(max_length=2, blank=True, null=True)
    custom_color = models.CharField(max_length=7, blank=True, null=True) 

    def save(self, *args, **kwargs):
        if not self.custom_name:
            self.custom_name = self.contact.name
        if not self.custom_email:
            self.custom_email = self.contact.email
        if not self.custom_phone:
            self.custom_phone = self.contact.phone
        if not self.custom_shortcut:
            self.custom_shortcut = self.contact.shortcut
        if not self.custom_color:
            self.custom_color = self.contact.color
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.custom_name} ({self.custom_email})"


class Subtask(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks") 
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    dueDate = models.DateField()
    position = models.IntegerField()
    prio = models.CharField(max_length=20, choices=[("low", "Low"), ("medium", "Medium"), ("urgent", "Urgent")])
    status = models.CharField(max_length=50, choices=[("todo", "To Do"), ("inProgress", "In Progress"), ("awaitFeedback", "Await Feedback"), ("done", "Done")])
    assignTo = models.ManyToManyField(Contact, related_name="tasks", blank=True)  # Kontakte können Tasks haben
    subtasks = models.ManyToManyField(Subtask, related_name="tasks", blank=True)

    def __str__(self):
        return f"{self.user} - {self.title}"
