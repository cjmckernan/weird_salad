from django.db import models 
from django.contrib.auth.models import AbstractUser

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_address = models.TextField()


class Employee(AbstractUser):
    location = models.ForeignKey(Location, null=True, on_delete=models.DO_NOTHING)
    edit_stock = models.BooleanField(default=False)
    take_payments = models.BooleanField(default=False)


