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