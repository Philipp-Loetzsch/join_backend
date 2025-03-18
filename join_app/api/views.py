from rest_framework import generics
from django.shortcuts import get_object_or_404
from join_app.models import Task, UserContact, Subtask
from .serializer import TaskSerializer, UserContactSerializer, SubtaskSerializer



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()  # Kein extra Filter nötig

class UserTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserContactListCreateView(generics.ListCreateAPIView):
    serializer_class = UserContactSerializer

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()

class SubtaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializer
    
    def get_queryset(self):
        return Subtask.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        task_id = self.kwargs["task_id"]
        task = get_object_or_404(Task, id=task_id, user=self.request.user)
        
        # Subtask speichern und der Task zuweisen
        subtask = serializer.save(task=task)  # Task explizit zuweisen
        task.subtasks.add(subtask)  # Subtask zu den Subtasks der Task hinzufügen


class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()
