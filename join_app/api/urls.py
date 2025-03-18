from django.urls import path
from .views import (
    TaskDetailView, UserTaskListCreateView,
    UserContactListCreateView, UserContactDetailView,
    # AdminContactListView, AdminContactDetailView
)

urlpatterns = [
    # Tasks
    path('api/user/tasks/', UserTaskListCreateView.as_view(), name='user-tasks'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Custom Kontakte für User
    path('api/user/contacts/', UserContactListCreateView.as_view(), name='user-contacts'),
    path('api/user/contacts/<int:pk>/', UserContactDetailView.as_view(), name='user-contact-detail'),

    # Admin Kontakte
    # path('api/admin/contacts/', AdminContactListView.as_view(), name='admin-contacts'),
    # path('api/admin/contacts/<int:pk>/', AdminContactDetailView.as_view(), name='admin-contact-detail'),
]
