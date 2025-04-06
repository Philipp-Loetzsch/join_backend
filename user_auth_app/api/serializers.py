from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from join_app.models import UserContact
from .functions import create_contacts_for_user, create_tasks_for_user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields  = ['username', 'email', 'password', 'repeated_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = User(
            email=self.validated_data['email'], 
            username=self.validated_data['username'], 
            first_name=self.validated_data.get('first_name', ''), 
            last_name=self.validated_data.get('last_name', '')
        )
        account.set_password(self.validated_data['password'])
        account.save()
        
        full_name = f"{account.first_name} {account.last_name}".strip()
        shortcut = (account.first_name[:1] + account.last_name[:1]).upper()

        UserContact.objects.create(
            user=account,
            color='gold',
            phone='',
            email=account.email,
            name=f"{full_name} (Yourself)",
            shortcut=shortcut
        )
        
        contact_ids = create_contacts_for_user(account)
        create_tasks_for_user(account, contact_ids)
        
        return account
    
class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'Email does not exist'})
        user = authenticate(username=user.username, password=password)
        if user is None:
            raise serializers.ValidationError({'password': 'Wrong password'})
        
        data['user'] = user
        return data