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
from ferreteria.api.views import RegisterView,EmployesAttendanceAPIView,CardRetrieveUpdateDestroy,CardListCreate,AttendanceRetrieveUpdateDestroy,AttendanceListCreate,SupplierTransactionsAPIView,CustomerListCreate,CustomerRetrieveUpdateDestroy, RoleView,PurchaseDetailAPIView, PurchaseListCreateAPIView,CustomTokenObtainPairView,EmployeeRetrieveUpdateDestroy,ProductList,CategorieList,SupplierList,UserListCreate,EmployeeListCreate, UserRetrieveUpdateDestroy,SaleListCreate,SaleRetrieveUpdateDestroy
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('api/asistencia/', AttendanceListCreate.as_view(), name='attendance-list'),
    path('api/asistencia/<int:pk>/', AttendanceRetrieveUpdateDestroy.as_view(), name='attendance-detail'),
    path('api/tarjetas/', CardListCreate.as_view(), name='card-list'),
    path('api/tarjetas/<int:pk>/', CardRetrieveUpdateDestroy.as_view(), name='card-detail'),
    path('api/productos/', ProductList.as_view(), name='product-list'),
    path('api/productos/<int:pk>/',ProductList.as_view(), name="product-detail"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('roles/', RoleView.as_view(), name='roles'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-retrieve-update-destroy'),
    path('api/categorias',CategorieList.as_view(), name="categories-list"),
    path('api/categorias/<int:pk>/',CategorieList.as_view(), name="categories-detail"),
    path('api/proveedores/', SupplierList.as_view(), name="proveedores-list"),
    path('api/proveedores/<int:pk>/', SupplierList.as_view(), name='proveedores-detail'),   
    path('ventas/', SaleListCreate.as_view(), name='ventas-list-create'),
    path('ventas/<int:pk>/', SaleRetrieveUpdateDestroy.as_view(), name='ventas-detail'),
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('purchases/', PurchaseListCreateAPIView.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/', PurchaseDetailAPIView.as_view(), name='purchase-detail'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('attendance/<int:employee_id>/transactions/', EmployesAttendanceAPIView.as_view(), name='attendance-transactions'),
    path('suppliers/<int:supplier_id>/transactions/', SupplierTransactionsAPIView.as_view(), name='supplier-transactions'),
]

