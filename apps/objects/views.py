from django.shortcuts import render
from .serializers import MedicalHistorySerializer , DentalServiceSerializer
from .models import MedicalHistory , DentalService
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