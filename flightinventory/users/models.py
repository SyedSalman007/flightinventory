from django.contrib.auth.models import AbstractUser
from django.db import models


class ContactDetail(models.Model):
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class User(AbstractUser):
    contact_detail = models.OneToOneField(ContactDetail, on_delete=models.CASCADE, null=True)
