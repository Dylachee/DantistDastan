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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стоматолог'
        verbose_name_plural = 'Стоматологи'

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'