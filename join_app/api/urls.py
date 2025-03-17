from django.urls import path
from .views import UserView, TaskDetailView, ContactDetailView, UserTaskListCreateView, UserContactListCreateView
urlpatterns = [
    path('api/user/<int:pk>/', UserView.as_view(), name='user-name'),
    path('api/user/<int:user_id>/tasks/' , UserTaskListCreateView.as_view(), name='user-tasks'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/user/<int:user_id>/contacts/', UserContactListCreateView.as_view(), name='user-contacts'),
    path('api/contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
