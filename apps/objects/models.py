from django.db import models
from apps.users.models import Patient

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    diagnosis = models.CharField(max_length=100)
    medications = models.TextField()
    allergies = models.TextField()
    symptoms = models.TextField()
    doctor_notes = models.TextField()
    follow_up_date = models.DateField()

class DentalService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title