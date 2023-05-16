from django.urls import path
from .views import DentistRegistrationView

urlpatterns = [
    # Другие URL-пути вашего приложения
    path('dentists/register/', DentistRegistrationView.as_view(), name='dentist-registration'),
]
