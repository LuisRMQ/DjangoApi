from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ferreteria.models import User, Role
from ferreteria.api.serializer import UserSerializer , RegisterSerializer , RoleSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        refresh = response.data['refresh']
        username = request.data['username']  # Cambiado 'email' a 'username'
        user = User.objects.get(username=username)
        return Response({
            'refresh': refresh,
            'access': token,
            'user': UserSerializer(user).data
        })