from django.db import models

# Create your models here.
class UserReg(models.Model):
    Username=models.CharField(max_length=15,unique=True)
    Email=models.CharField(max_length=15,unique=True)
    Number=models.IntegerField(max_length=15,unique=True)
    Gender=models.CharField(max_length=15)
    Address=models.CharField(max_length=30)
    Password=models.CharField(max_length=15)
    ConfirmPassword=models.CharField(max_length=15)



