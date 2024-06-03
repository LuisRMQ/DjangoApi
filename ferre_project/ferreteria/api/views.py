from rest_framework import viewsets
from ferreteria.models import User
from ferreteria.api.serializer import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer