from django.db import models

class UserProfile(models.Model):
    
    username = models.CharField(max_length=100)
    
    age = models.IntegerField()
    
    is_public = models.BooleanField(default=True)

    class Meta:
        db_table = 'profiles_userprofile'

    def __str__(self):
        return self.username
