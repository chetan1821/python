from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    stock=models.IntegerField()
    image = models.ImageField(upload_to="images",null=True)

    def total_value(self):
        return self.price * self.stock

