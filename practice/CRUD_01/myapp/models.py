from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    dept=models.CharField(max_length=50)
    image = models.ImageField(upload_to="images",null=True)
    image2=models.ImageField(upload_to="images2",null=True)
    



