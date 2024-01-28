# Documentation



I used django-rest-framwork generic view. Documantation is below:

https://www.django-rest-framework.org/api-guide/generic-views/

- Admin setup:
  - username:```admin```
  - password:```admin```

## Describe the urls.
```http://127.0.0.1:8000/api/```

This is the base urls.


1. ```/companies/```
    
    POST request: Add a companies

    GET request: View list of all companies

2. ```companies/<int:pk>/```
   
    PUT request: Edit the information of companies

    GET request: View companies which id=pk

3. ```companies/<int:company_id>/employees/```

    POST request: Add a employees companie which id=company_id

    GET request: View list of all employees which company_id=company_id
4. ```companies/<int:company_id>/employees/<int:pk>/```

    PUT request: Edit a employees information of companie where id=company_id

    GET request: View list of an employees which pk=empolyees_id

5. ```companies/<int:company_id>/employees/<int:pk>/take-device/```
   
    POST request: An employee can take a device. Before take a device several input from fill up.
    - a: device name
    - b: taken data
    - c: return data
    - d: companies id ->Automatic take input from urls.
    - e: employees id ->Automatic take input from urls.
6. ```companies/<int:company_id>/checkouts/```
   
   GET: All the device history will shown. Also show the condition the device is return or not. Also which employees take the device.

7. ```companies/<int:company_id>/checkouts/<int:pk>/``` 

    PATCH: Edit a specefic checkout. Also can modify that the device is return or not.

## Describe the models

**Company model:**

If we need than we can add more information about an company. For simplicity add only name..
```py
class Company(models.Model):
    name = models.CharField(max_length=255,unique=True)
```
**Employee model:**

Employee model has 3 varible.Name,Contact_information,company. Company is foreignKey which indicate the Company model.
```py
class Employee(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
```


**Checkout model:**

In this model i take the history of every taken devices.
```py
class Checkout(models.Model):
    device_name = models.CharField(max_length=255)
    CONDITION_CHOICES = [
        ('RETURNED', 'Return Device'),
        ('NOT_RETURNED', 'Not Return Device'),
    ]

    taken_data = models.DateTimeField()
    return_data = models.DateTimeField()
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='NOT_RETURNED')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
```

## Describe the serializers

**CompanySerializer:**

Company serializer used for Serialize the company model.
```py
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'
```

**EmployeeSerializer**

EmployeeSerializer serializer used for Serialize the employee model.
```py
class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'contact_information', 'company']
        extra_kwargs = {'company': {'write_only': True, 'required': False}}

```
**CheckoutSerializer**

CheckoutSerializer serializer used for Serialize the Checkout model.
```py
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
```

**CheckoutReturnSerializer**

CheckoutReturnSerializer  Serialize the checkout model condition field.
```py
class CheckoutReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['condition']
```