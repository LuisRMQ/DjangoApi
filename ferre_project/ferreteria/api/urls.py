from rest_framework.routers import DefaultRouter
from ferreteria.api.views import UserViewSet
from django.urls import path, include


urlpatterns = [
    path('api/', include('ferreteria.api.urls'))
]