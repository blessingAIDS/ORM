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


