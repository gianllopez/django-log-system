from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class LoginLog(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    username = models.CharField(max_length=25)
    logindate = models.DateField(auto_now_add=True)
    logintime = models.TimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % self.username