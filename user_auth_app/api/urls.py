from django.urls import path
from .views import  RegistrationView,LogInView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', UserProfileList.as_view(), name='userprofile-list'),
    # path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    # path('login/', obtain_auth_token, name='login')
    path('login/', LogInView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
