from rest_framework import generics
from django.shortcuts import get_object_or_404
from join_app.models import Task, UserContact, Subtask
from .serializer import TaskSerializer, UserContactSerializer, SubtaskSerializer



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single Task instance.

    Handles GET, PUT, PATCH, and DELETE requests for a specific task,
    identified by its primary key in the URL.

    Attributes:
        serializer_class (TaskSerializer): The serializer used for task data.
        queryset (QuerySet): Base queryset. Note: Permissions must be configured
                             to ensure users can only access/modify their own tasks.
        permission_classes (list): Recommended: [IsAuthenticated] and custom permission
                                    to check object ownership.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all() 

class UserTaskListCreateView(generics.ListCreateAPIView):
    """
    API view for listing tasks owned by the current user or creating a new task.

    Handles GET requests to list tasks and POST requests to create a new task
    for the currently authenticated user.

    Attributes:
        serializer_class (TaskSerializer): The serializer used for task data.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserContactListCreateView(generics.ListCreateAPIView):
    """
    API view for listing contacts owned by the current user or creating a new contact.

    Handles GET requests to list contacts and POST requests to create a new contact
    for the currently authenticated user.

    Attributes:
        serializer_class (UserContactSerializer): The serializer used for contact data.
    """
    serializer_class = UserContactSerializer

    def get_queryset(self):
        """
        Overrides the default queryset to return only contacts owned by the
        currently authenticated user.
        """
        return UserContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Overrides the default creation behavior to automatically set the task's
        'user' field to the currently authenticated user upon saving.
        """
        serializer.save(user=self.request.user)

class UserContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single UserContact instance.

    Handles GET, PUT, PATCH, and DELETE requests for a specific contact,
    identified by its primary key in the URL.

    Attributes:
        serializer_class (UserContactSerializer): The serializer used for contact data.
        queryset (QuerySet): Base queryset. Note: Permissions must be configured
                             to ensure users can only access/modify their own contacts.
        permission_classes (list): Recommended: [IsAuthenticated] and custom permission
                                    to check object ownership.
    """
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()

class SubtaskListCreateView(generics.ListCreateAPIView):
    """
    API view for listing contacts owned by the current user or creating a new contact.

    Handles GET requests to list contacts and POST requests to create a new contact
    for the currently authenticated user.

    Attributes:
        serializer_class (UserContactSerializer): The serializer used for contact data.
    """
    serializer_class = SubtaskSerializer
    
    def get_queryset(self):
        """
        Overrides the default queryset to return only subtasks belonging to the
        specified parent task (via URL's 'task_id'), ensuring the parent task
        belongs to the currently authenticated user.
        """
        task_id = self.kwargs["task_id"]
        return Subtask.objects.filter(task__user=self.request.user, task__id=task_id)

    def perform_create(self, serializer):
        """
        Overrides the default creation behavior to associate the new subtask
        with the correct parent task identified by 'task_id' in the URL.

        Ensures the parent task belongs to the current user before saving.
        """
        task_id = self.kwargs["task_id"]
        task = get_object_or_404(Task, id=task_id, user=self.request.user)
        subtask = serializer.save(task=task)  
        task.subtasks.add(subtask)  


class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a single Subtask instance.

    Handles GET, PUT, PATCH, and DELETE requests for a specific subtask,
    identified by its primary key in the URL.

    Attributes:
        serializer_class (SubtaskSerializer): The serializer used for subtask data.
        queryset (QuerySet): Base queryset. Note: Permissions must be configured
                             to ensure users can only access/modify subtasks belonging
                             to tasks they own.
        permission_classes (list): Recommended: [IsAuthenticated] and custom permission
                                    to check ownership via the parent task.
    """
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()
