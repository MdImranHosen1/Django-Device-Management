from rest_framework import generics
from .models import Company, Employee, Checkout
from .serializers import CompanySerializer, EmployeeSerializer, CheckoutSerializer,CheckoutReturnSerializer
from rest_framework.response import Response

# /companies/
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# companies/<int:pk>/
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# companies/<int:company_id>/employees/
class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(company_id=company_id)

    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        company = Company.objects.get(id=company_id)
        serializer.save(company=company)

# companies/<int:company_id>/employees/<int:pk>/
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# companies/<int:company_id>/employees/<int:pk>/take-device/
class EmployeeTakeDeviceView(generics.CreateAPIView):
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs['company_id']
        employee_id = self.kwargs['pk']
        
        company = Company.objects.get(id=company_id)
        employee = Employee.objects.get(id=employee_id)
        
        print("asdfsadf ", company_id, employee_id)
        serializer.save(company=company, employee=employee)

# companies/<int:company_id>/checkouts/
class CompanyCheckoutsListView(generics.ListAPIView):
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        return Checkout.objects.filter(company_id=company_id)

# companies/<int:company_id>/checkouts/<int:pk>/
class CompanyCheckoutsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutReturnSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        checkout_id = self.kwargs.get('pk')
        return Checkout.objects.filter(company_id=company_id, id=checkout_id)


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(condition=request.data.get('condition', instance.condition))
        return Response(serializer.data)