from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from join_app.models import Task, UserContact, Subtask
from .serializer import TaskSerializer, UserContactSerializer, SubtaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class UserTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserContactListCreateView(generics.ListCreateAPIView):
    serializer_class = UserContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserContact.objects.filter(user=self.request.user)
    
    
class SubtaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs["task_id"]
        return Subtask.objects.filter(tasks__id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs["task_id"]
        task = generics.get_object_or_404(Task, id=task_id, user=self.request.user)
        subtask = serializer.save()
        task.subtasks.add(subtask) 

class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubtaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs["task_id"]
        return Subtask.objects.filter(tasks__id=task_id)

# class AdminContactListView(generics.ListAPIView):
#     serializer_class = ContactSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         if not self.request.user.is_staff:
#             return Contact.objects.none() 
#         return Contact.objects.all()

# class AdminContactDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ContactSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         if not self.request.user.is_staff:
#             return Contact.objects.none()
#         return Contact.objects.all()


