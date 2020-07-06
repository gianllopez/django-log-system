from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class LogUpModel(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25) 
    surname = models.CharField(max_length=25) 
    phone = models.CharField(max_length=20, blank=True, null=True) 
    age = models.IntegerField(default=18, blank=True, null=True)
    def __str__(self):
        return '%s -> %s' % (self.user.username, self.user.password)
