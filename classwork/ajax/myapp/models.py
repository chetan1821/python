from django.db import models

# Create your models here.
class Product (models.Model):
    name=models.CharField(max_length=50)

class Country(models.Model):
    name=models.CharField(max_length=50)

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)



