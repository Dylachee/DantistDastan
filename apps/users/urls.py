from django.urls import path
from .views import DentistRegistrationView , PatientCreateView

urlpatterns = [
    # Другие URL-пути вашего приложения
    path('dentists/register/', DentistRegistrationView.as_view(), name='dentist-registration'),
    path('patients/create/', PatientCreateView.as_view(), name='patient-create'),
]
