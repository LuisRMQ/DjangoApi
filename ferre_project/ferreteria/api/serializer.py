from rest_framework import serializers
from ferreteria.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 
from ferreteria.models import Role, Product, Category, Supplier,Sale, SaleDetail,Employee

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'role_id']  

    def create(self, validated_data):
        role_id = validated_data.pop('role_id', None)
        user = User.objects.create_user(
            username=validated_data['username'], 
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        if role_id:
            user.role_id = role_id
            user.save()
        return user

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'         

class SaleDetailSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = SaleDetail
        fields = ['detail_id', 'sale', 'product', 'quantity', 'unit_price']
        read_only_fields = ['detail_id', 'sale']  

class SaleSerializer(serializers.ModelSerializer):
    details = SaleDetailSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['sale_id', 'date', 'customer', 'total', 'employee', 'details']
        read_only_fields = ['sale_id', 'date'] 

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        sale = Sale.objects.create(**validated_data)

        for detail_data in details_data:
            SaleDetail.objects.create(sale=sale, **detail_data)

        return sale

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        instance.customer = validated_data.get('customer', instance.customer)
        instance.total = validated_data.get('total', instance.total)
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()

        instance.details.all().delete()
        for detail_data in details_data:
            SaleDetail.objects.create(sale=instance, **detail_data)

        return instance
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'