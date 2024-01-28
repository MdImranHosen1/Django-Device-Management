from rest_framework import serializers
from .models import Company, Employee, Checkout

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'
        

class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'contact_information', 'company']
        extra_kwargs = {'company': {'write_only': True, 'required': False}}




class CheckoutSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    employees = EmployeeSerializer(read_only=True)

    class Meta:
        model = Checkout
        fields = ['id', 'device_name', 'taken_data', 'return_data', 'condition', 'company', 'employees']
        extra_kwargs = {
            'company': {'write_only': True, 'required': False},
            'employees': {'write_only': True, 'required': False}
        }


class CheckoutReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['condition']