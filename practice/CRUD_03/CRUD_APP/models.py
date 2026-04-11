from django.db import models
# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to="image",null=True)
    