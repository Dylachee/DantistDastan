from django.urls import path
from .views import MedicalHistoryCreateView , DentalServicesCreateView , AppointmentCreateView

urlpatterns = [
    path('medical-history/', MedicalHistoryCreateView.as_view(), name='medical-history-create'),
    path('services/',DentalServicesCreateView.as_view(), name='dental-service-list'),
    path('appointments/',AppointmentCreateView.as_view(), name='appointments-create'),

]
