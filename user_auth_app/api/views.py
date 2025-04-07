from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LogInSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status


class RegistrationView(APIView):
    """
    API view for handling new user registrations.

    Accepts POST requests with user registration data (e.g., username, email,
    password, first_name, last_name). If validation is successful, creates
    a new user, generates an authentication token, and returns user details
    along with the token. Allows access from any user.
    """
    permission_classes = [AllowAny]

    def post( self, request):
        """
        Handles POST request to register a new user.

        Args:
            request (Request): The incoming HTTP request containing user
                               registration data in the request body.

        Returns:
            Response: An HTTP Response.
                      - 200 OK: If registration is successful, returns a JSON
                        object containing the auth token and user details
                        ('token', 'username', 'email', 'first_name', 'last_name').
                      - 400 Bad Request: If the provided data is invalid,
                        returns a JSON object with validation errors.
        """
        serializer = RegistrationSerializer(data=request.data)


        data={}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data={
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
                'first_name': saved_account.first_name,
                'last_name': saved_account.last_name
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInView(APIView):
    """
    API view for handling user login requests.

    Accepts POST requests with user credentials (e.g., email/username, password).
    If authentication is successful via the LogInSerializer, it logs the user in
    (using Django's session framework), generates/retrieves an authentication
    token, and returns user details along with the token. Allows access from
    any user without prior authentication.
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles POST request to authenticate and log in a user.

        Args:
            request (Request): The incoming HTTP request containing user
                               credentials in the request body.

        Returns:
            Response: An HTTP Response.
                      - 200 OK: If login is successful, returns a JSON object
                        containing the auth token and user details
                        ('token', 'username', 'first_name', 'last_name').
                      - 400 Bad Request: If authentication fails or data is
                        invalid, returns a JSON object with errors.
        """
        serializer = LogInSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            data={
                'token': token.key,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)