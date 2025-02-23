from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=20, decimal_places=2)
    shortcut = models.CharField(max_length=2)
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return self.name
   
   
class Assign(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='assings')
    
class Subtask(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField()
 
class Task(models.Model):
    title = models.CharField(max_length=50)
    category= models.CharField(max_length=50)
    description=models.TextField()
    dueDate=models.DecimalField(max_digits=30, decimal_places=2)
    position=models.DecimalField(max_digits=5, decimal_places=2)
    prio=models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    assignTo = models.ForeignKey(Assign, on_delete=models.CASCADE, related_name='tasks')
    subtasks = models.ForeignKey(Subtask, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField( max_length=250)
    tasks = models.ManyToManyField( Task, related_name='users')
    contacts = models.ManyToManyField( Contact, related_name='users')
     
    def __str__(self):
        return self.name
