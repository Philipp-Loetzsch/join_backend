from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from join_app.models import Task, UserContact, Subtask
from .serializer import TaskSerializer, UserContactSerializer, SubtaskSerializer
from join_app.permissions import IsOwner


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()  # Kein extra Filter nötig


class UserTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """Setzt den User automatisch beim Erstellen"""
        serializer.save(user=self.request.user)


class UserContactListCreateView(generics.ListCreateAPIView):
    serializer_class = UserContactSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserContactSerializer
    queryset = UserContact.objects.all()


class SubtaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        """Nur Subtasks von Tasks des aktuellen Users abrufen"""
        return Subtask.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        """Stellt sicher, dass der Subtask nur zu eigenen Tasks hinzugefügt wird"""
        task_id = self.kwargs["task_id"]
        task = get_object_or_404(Task, id=task_id, user=self.request.user)
        serializer.save(task=task)


class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubtaskSerializer
    queryset = Subtask.objects.all()
