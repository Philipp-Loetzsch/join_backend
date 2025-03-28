from django.urls import path
from .views import  RegistrationView,LogInView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
