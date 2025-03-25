# Ex02 Django ORM Web Application
# Date: 25/03/25
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
models.py:

from django.db import models
from django.contrib import admin
class bankloan(models.Model):
    Name=models.CharField(max_length=100)
    Accountno=models.IntegerField(primary_key="Accountno")
    Startdate=models.DateField()
    Email=models.EmailField()
    Mobilenumber=models.IntegerField()
    Amount=models.IntegerField()

class bankloanAdmin(admin.ModelAdmin):
    list_display=('Name','Accountno','Startdate','Email','Mobilenumber','Amount')


admin.py:

from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)
# OUTPUT

![alt text](<ex02/Screenshot 2025-03-25 213853.png>)

# Name:Blessing S
# Reg no: 24002843
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
