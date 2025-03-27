from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User

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
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        email = self.validated_data['email']

        if pw != repeated_pw:
            raise serializers.ValidationError({'error': 'Passwords do not match'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email is already in use'})
        
        account = User(
            email=email, 
            username=self.validated_data['username'], 
            first_name=self.validated_data.get('first_name', ''),  # Falls nicht angegeben, Standardwert ''
            last_name=self.validated_data.get('last_name', '')  # Falls nicht angegeben, Standardwert ''
        )
        account.set_password(pw)
        account.save()
        return account