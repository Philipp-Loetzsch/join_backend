# from rest_framework import generics
# from user_auth_app.models import UserProfile
# from .serializers import UserProfileSerializer

# class UserProfileList(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer



from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LogInSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post( self, request):
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
        else:
            data=serializer.errors
        return Response(data)            

class LogInView(APIView):
    authentication_classes = []  # Deaktiviert die Authentifizierungspflicht für diese View
    permission_classes = [AllowAny]
    
    def post(self, request):
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
            # Token für den Benutzer abrufen oder erstellen
         
            
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def login_view(request):
    #     email = request.data.get("email")
    #     password = request.data.get("password")

    #     if not email or not password:
    #         return Response({"error": "E-Mail und Passwort sind erforderlich"}, status=400)

    #     # Benutzer anhand der E-Mail finden
    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return Response({"error": "Benutzer nicht gefunden"}, status=404)

    #     # Passwort prüfen
    #     user = authenticate(username=user.username, password=password)
    #     if user:
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({"token": token.key, "username": user.username})

    #     return Response({"error": "Ungültige Anmeldeinformationen"}, status=400)
