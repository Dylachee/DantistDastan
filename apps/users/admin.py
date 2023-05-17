from django.contrib import admin
from .models import Dentist , Patient

admin.site.register([Dentist, Patient])