from django.contrib import admin
from .models import MedicalHistory , DentalService , Appointment

admin.site.register([MedicalHistory , DentalService, Appointment])
