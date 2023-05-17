from django.urls import path
from .views import MedicalHistoryCreateView , DentalServicesCreateView

urlpatterns = [
    path('medical-history/', MedicalHistoryCreateView.as_view(), name='medical-history-create'),
    path('services/',DentalServicesCreateView.as_view(), name='dental-service-list'),

]
