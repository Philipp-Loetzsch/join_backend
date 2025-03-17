from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from join_app.models import Task, Contact, User
from .serializer import TaskSerializer, ContactSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


class UserView( generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        return user.tasks.all()

class UserContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        return user.contacts.all()


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
