from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    fees = models.IntegerField()
    rating = models.FloatField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="slots")
    day = models.CharField(max_length=10)   # Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day}"
