from django.urls import path
from .views import DentistRegistrationView , PatientCreateView

urlpatterns = [
    # Другие URL-пути вашего приложения
    path('dentists/', DentistRegistrationView.as_view(), name='dentist-registration'),
    path('patients/', PatientCreateView.as_view(), name='patient-create'),
]
