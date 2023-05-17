from django.urls import path
from .views import MedicalHistoryCreateView

urlpatterns = [
    path('medical-history/create/', MedicalHistoryCreateView.as_view(), name='medical-history-create'),
]
