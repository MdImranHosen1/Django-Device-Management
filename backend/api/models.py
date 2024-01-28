from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255,unique=True)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Checkout(models.Model):
    device_name = models.CharField(max_length=255)
    CONDITION_CHOICES = [
        ('RETURNED', 'Return Device'),
        ('NOT_RETURNED', 'Take Device'),
    ]

    taken_data = models.DateTimeField()
    return_data = models.DateTimeField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='NOT_RETURNED')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    