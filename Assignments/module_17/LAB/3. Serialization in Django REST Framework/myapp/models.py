from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=20)
