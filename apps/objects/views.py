from django.shortcuts import render
from .serializers import MedicalHistorySerializer , DentalServiceSerializer , Appointment
from .models import MedicalHistory , DentalService , Appointment
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
class MedicalHistoryCreateView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsAuthenticated]

class DentalServicesCreateView(RetrieveUpdateDestroyAPIView , ListCreateAPIView):
    queryset = DentalService.objects.all()
    serializer_class = DentalServiceSerializer
    permission_classes = [IsAuthenticated]

class AppointmentCreateView(RetrieveUpdateDestroyAPIView , ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    