from django.db import models
from django.contrib.auth.models import User
class soeuser(models.Model):
    mainuser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    phno = models.CharField(max_length=10)
    def __str__(self):
        return self.name





