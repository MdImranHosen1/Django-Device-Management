from django.urls import path
from .views import (
    CompanyListView, 
    CompanyDetailView,
    EmployeeListView, 
    EmployeeDetailView, 
    EmployeeTakeDeviceView,
    CompanyCheckoutsListView, 
    CompanyCheckoutsDetailView
)

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:company_id>/employees/', EmployeeListView.as_view(), name='company-employees-list'),
    path('companies/<int:company_id>/employees/<int:pk>/', EmployeeDetailView.as_view(), name='company-employee-detail'),
    path('companies/<int:company_id>/employees/<int:pk>/take-device/', EmployeeTakeDeviceView.as_view(), name='employee-take-device'),
    path('companies/<int:company_id>/checkouts/', CompanyCheckoutsListView.as_view(), name='company-checkouts-list'),
    path('companies/<int:company_id>/checkouts/<int:pk>/', CompanyCheckoutsDetailView.as_view(), name='company-checkouts-detail'),
]
