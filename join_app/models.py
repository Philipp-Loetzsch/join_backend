from django.db import models
from django.contrib.auth.models import User

class UserContact(models.Model):
    """
    Represents a contact associated with a specific registered User.

    Stores personal details for a contact linked to a user account.

    Attributes:
        user (ForeignKey to User): The user who owns this contact. Deletes contact
            if the user is deleted. Can be accessed via `user.contacts`.
        name (CharField): The name of the contact. Optional.
        email (EmailField): The email address of the contact. Optional.
        phone (CharField): The phone number of the contact. Optional.
        shortcut (CharField): A short identifier or initials for the contact (max 2 chars). Optional.
        color (CharField): A color code (e.g., hex like #RRGGBB) associated with the contact. Optional.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    shortcut = models.CharField(max_length=2, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        """Returns a string representation of the contact."""
        return f"{self.user.username} - {self.name} ({self.email})"

class Task(models.Model):
    """
    Represents a task created by a registered User.

    Contains details about the task, its status, priority, assignments,
    and relationship to the owning user.

    Attributes:
        user (ForeignKey to User): The user who created and owns this task. Deletes task
            if the user is deleted. Can be accessed via `user.tasks`.
        title (CharField): The title of the task (max 50 chars). Required.
        category (CharField): The category of the task (max 50 chars). Required.
        description (TextField): A detailed description of the task. Required.
        dueDate (IntegerField): The due date for the task.
        position (IntegerField): A field potentially used for ordering or positioning tasks. Required.
        prio (CharField): The priority level of the task. Limited to choices:
            "Low", "Medium", "Urgent". Required.
        status (CharField): The current status of the task. Limited to choices:
            "todo", "inProgress", "awaitFeedback", "done". Required.
        assignTo (ManyToManyField to UserContact): Contacts assigned to this task.
            A task can be assigned to multiple contacts, and contacts can have multiple
            tasks. Required (blank=False). Can be accessed via `contact.tasks_list`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    dueDate = models.IntegerField() # Consider changing to DateField or DateTimeField
    position = models.IntegerField()
    prio = models.CharField(max_length=20, choices=[("Low", "Low"), ("Medium", "Medium"), ("Urgent", "Urgent")])
    status = models.CharField(max_length=50, choices=[("todo", "To Do"), ("inProgress", "In Progress"), ("awaitFeedback", "Await Feedback"), ("done", "Done")])
    assignTo = models.ManyToManyField(UserContact, related_name="tasks_list", blank=False)

    def __str__(self):
        """Returns a string representation of the task, including ID, user, and title."""
        return f"TASK_ID: [{self.id}] USER:{self.user} TITLE: {self.title}"


class Subtask(models.Model):
    """
    Represents a subtask associated with a parent Task.

    Attributes:
        task (ForeignKey to Task): The parent task this subtask belongs to. Deletes subtask
            if the parent task is deleted. Can be accessed via `task.subtasks`.
        title (CharField): The title or description of the subtask (max 50 chars). Required.
        complete (BooleanField): Indicates whether the subtask is completed. Defaults to False.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self):
        """Returns a string representation of the subtask, including ID and parent task info."""
        return f"SUBTASK_ID: [{self.id}]{self.task}"