
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    imageurl = models.CharField(max_length=1000, null=True, blank=True, default="this is default")
    price = models.FloatField()
    is_closed = models.BooleanField(default=False, blank=True, null=True)