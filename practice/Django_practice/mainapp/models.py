from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    dept = models.CharField(max_length=20)
    join_date=models.DateField()

class product(models.Model):
    pid =models.IntegerField(primary_key=True,auto_created=True)
    pname=models.CharField(max_length=20)
    pdesc=models.CharField(max_length=100)
    pdate=models.DateField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name