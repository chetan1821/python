from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    age=models.IntegerField()

class Product(models.Model):
    pname=models.CharField(max_length=20)
    price=models.FloatField(max_length=20)

    
