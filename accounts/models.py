from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_pharmacist = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Pharmacist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='pharmacist')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)

    pharmacy_name = models.CharField(max_length=100)
    business_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)

    created_at = models.DateTimeField(default=timezone.now)

