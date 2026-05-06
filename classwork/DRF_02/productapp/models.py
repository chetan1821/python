from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()

    def __str__(self):
        return self.name
