from django.urls import path
from .views import user_name, user_tasks , user_contacts, task_detail, contact_detail, UserListView
urlpatterns = [
    path('api/user/<int:pk>/', user_name, name='user-name'),
    path('api/user/<int:user_id>/tasks/' , user_tasks, name='user-tasks'),
    path('api/tasks/<int:pk>/', task_detail, name='task-detail'),
    path('api/user/<int:user_id>/contacts/', user_contacts, name='user-contacts'),
    path('api/contacts/<int:pk>/', contact_detail, name='contact-detail'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]
