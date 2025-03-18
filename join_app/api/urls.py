from django.urls import path
from .views import (
    TaskDetailView, UserTaskListCreateView,
    UserContactListCreateView, UserContactDetailView,
    SubtaskListCreateView, SubtaskDetailView
    # AdminContactListView, AdminContactDetailView
)

urlpatterns = [
    # Tasks
    path('', UserTaskListCreateView.as_view(), name='user-tasks'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Custom Kontakte für User
    path('api/user/contacts/', UserContactListCreateView.as_view(), name='user-contacts'),
    path('api/user/contacts/<int:pk>/', UserContactDetailView.as_view(), name='user-contact-detail'),
    
    path('<int:task_id>/subtasks/', SubtaskListCreateView.as_view(), name='subtask-list'),
    path('<int:task_id>/subtasks/<int:pk>/', SubtaskDetailView.as_view(), name='subtask-detail'),

    # Admin Kontakte
    # path('api/admin/contacts/', AdminContactListView.as_view(), name='admin-contacts'),
    # path('api/admin/contacts/<int:pk>/', AdminContactDetailView.as_view(), name='admin-contact-detail'),
]
