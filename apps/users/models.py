from django.db import models

class Dentist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    experience = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
