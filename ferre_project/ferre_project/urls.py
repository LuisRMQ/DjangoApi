"""
URL configuration for ferre_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from ferreteria.api.views import RegisterView, RoleView, CustomTokenObtainPairView,ProductList,CategorieList,SupplierList
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('api/productos/', ProductList.as_view(), name='product-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('roles/', RoleView.as_view(), name='roles'),

    path('api/categorias',CategorieList.as_view(), name="categories-list"),
    path('api/categorias/<int:pk>/',CategorieList.as_view(), name="categories-detail"),

    path('api/proveedores/', SupplierList.as_view(), name="proveedores-list"),
    path('api/proveedores/<int:pk>/', SupplierList.as_view(), name='proveedores-detail'),   
]

