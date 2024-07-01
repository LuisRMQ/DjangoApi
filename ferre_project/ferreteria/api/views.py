from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from ferreteria.models import User, Role,Product, Category,Supplier,Sale,Employee,Purchase,Customer, SaleDetail, PurchaseDetail
from ferreteria.api.serializer import UserSerializer ,CustomerSerializer,PurchaseSerializer, RegisterSerializer , RoleSerializer,ProductSerializer, CategorySerializer, SupplierSerializer,SaleSerializer,EmployeeSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        refresh = response.data['refresh']
        username = request.data['username']  
        user = User.objects.get(username=username)
        return Response({
            'refresh': refresh,
            'access': token,
            'user': UserSerializer(user).data
        })

class ProductList(APIView):
    def get(self, request, pk=None, *args, **kwargs):
     if pk is None:
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)
     else:
         try:
             product = Product.objects.get(pk=pk)
         except Product.DoesNotExist:
             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

         serializer = ProductSerializer(product)
         return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategorieList(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        else:
         try:
             category = Category.objects.get(pk=pk)
         except Category.DoesNotExist:
             return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

         serializer = CategorySerializer(category)
         return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class SupplierTransactionsAPIView(APIView):
     def get(self, request, supplier_id):
        try:
            supplier = get_object_or_404(Supplier, id_supplier=supplier_id)
            products = Product.objects.filter(supplier=supplier).select_related('category')
            product_data = [
                {
                    'id': product.id_product,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'available_quantity': product.available_quantity,
                    'category': product.category.name if product.category else 'Sin categoría'
                }
                for product in products
            ]

            return Response({
                'products': product_data
            })

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=500)

class SupplierList(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            supplier = Supplier.objects.all()
            serializer = SupplierSerializer(supplier, many=True)
            return Response(serializer.data)
        else:
         try:
             supplier = Supplier.objects.get(pk=pk)
         except Supplier.DoesNotExist:
             return Response({'error': 'Supplier not found'}, status=status.HTTP_404_NOT_FOUND)

         serializer = SupplierSerializer(supplier)
         return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
    def put(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer    

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer    

class PurchaseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailAPIView(generics.RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer    