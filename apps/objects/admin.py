from django.contrib import admin
from .models import MedicalHistory , DentalService

admin.site.register([MedicalHistory , DentalService])
