from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.IntegerField()
    course=models.CharField(max_length=30)

class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.IntegerField(default=0)
    department=models.CharField(max_length=100)

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    quantity=models.IntegerField()
    description=models.CharField(max_length=30)

