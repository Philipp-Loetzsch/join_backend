from django.urls import path
from .views import (
    TaskDetailView, UserTaskListCreateView,
    UserContactListCreateView, UserContactDetailView,
    SubtaskListCreateView, SubtaskDetailView
    # AdminContactListView, AdminContactDetailView
)

urlpatterns = [

    path('api/user/tasks/', UserTaskListCreateView.as_view(), name='user-tasks'),
    path('api/user/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('api/user/contacts/', UserContactListCreateView.as_view(), name='user-contacts'),
    path('api/user/contacts/<int:pk>/', UserContactDetailView.as_view(), name='user-contact-detail'),
    
    path('api/user/tasks/<int:task_id>/subtasks/', SubtaskListCreateView.as_view(), name='subtask-list'),
    path('api/user/tasks/<int:task_id>/subtasks/<int:pk>/', SubtaskDetailView.as_view(), name='subtask-detail'),
]
