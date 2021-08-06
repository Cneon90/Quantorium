from django.db import models

# Create your models here.


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=220)
    email = models.CharField(max_length=220)
    birthday = models.CharField(max_length=220)
    password = models.CharField(max_length=220)
    status = models.CharField(max_length=220)
    status = models.CharField(max_length=220)