from django.db import models
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField(max_length=10)
    course=models.CharField(max_length=30)
    password=models.CharField(max_length=8)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
