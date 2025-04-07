from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from join_app.models import UserContact
from .functions import create_contacts_for_user, create_tasks_for_user

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.

    Handles serialization and deserialization of UserProfile instances.
    Currently includes all fields from the UserProfile model.
    """
    class Meta:
        model = UserProfile
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Handles validation of registration data, creation of a new User instance
    with a properly hashed password, creation of an associated 'self' UserContact,
    and triggering the creation of default contacts and tasks for the new user.
    Includes password confirmation field.
    """

    repeated_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields  = ['username', 'email', 'password', 'repeated_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

    def save(self):
        """
        Creates the User account, hashes the password, and performs post-registration setup.

        Post-registration setup includes creating a UserContact for the user themselves
        and calling functions to create default contacts and tasks. Assumes password
        confirmation validation happens elsewhere (e.g., in a `validate` method or
        `validate_repeated_password`).

        Returns:
            User: The newly created and saved User instance.
        """
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data.get('first_name', ''),
            last_name=self.validated_data.get('last_name', '')
        )
        account.set_password(self.validated_data['password'])
        account.save()
        full_name = f"{account.first_name} {account.last_name}".strip()
        shortcut = (account.first_name[:1] + account.last_name[:1]).upper() if account.first_name and account.last_name else (account.username[:2].upper() if account.username else '??')

        UserContact.objects.create(
            user=account,
            color='gold', # Example default color
            phone='',
            email=account.email,
            name=f"{full_name} (Yourself)" if full_name else f"{account.username} (Yourself)",
            shortcut=shortcut if shortcut else '??'
        )
        contact_ids = create_contacts_for_user(account)
        create_tasks_for_user(account, contact_ids)

        return account

class LogInSerializer(serializers.Serializer):
    """
    Serializer for user login validation.

    Accepts email and password, validates them against existing User accounts,
    and performs authentication. Does not directly map to a model for saving.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validates user credentials (email and password).

        Checks if a user with the given email exists and if the provided
        password is correct for that user using Django's authentication system.

        Args:
            data (dict): Dictionary containing 'email' and 'password' keys.

        Returns:
            dict: The validated data dictionary, with the authenticated 'user'
                  object added under the 'user' key if validation succeeds.

        Raises:
            serializers.ValidationError: If the email does not exist or the
                                         password is incorrect.
        """
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
             raise serializers.ValidationError("Email and password are required.", code='authorization')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Invalid credentials'})

        user = authenticate(username=user_obj.username, password=password)

        if user is None:
            raise serializers.ValidationError({'detail': 'Invalid credentials'})
      
        if not user.is_active:
            raise serializers.ValidationError({'detail': 'User account is disabled.'})

        data['user'] = user 
        return data