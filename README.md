# Ex02 Django ORM Web Application
# Date: 22/04/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
admin.py:

from django.contrib import admin
from .models import Loan,LoanAdmin

admin.site.register(Loan,LoanAdmin)

models.py:

from django.db import models
from django.contrib import admin

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_term = models.IntegerField()
    disbursement_date = models.DateField()

class LoanAdmin(admin.ModelAdmin):
list_display=('loan_id','customer_name','loan_amount','interest_rate','loan_term','disbursement_date')

![image](https://github.com/user-attachments/assets/d1fb6a22-7676-4521-849c-665c95e225dc)

# OUTPUT

![image](https://github.com/user-attachments/assets/4e8a5ac3-3591-432c-b0bd-ee6ccc134469)
![image](https://github.com/user-attachments/assets/712207e5-3f2b-452f-b356-a6a72fa027bc)


# Name:Blessing S
# Reg no: 212224230039
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
