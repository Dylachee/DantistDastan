from django.shortcuts import render
from .serializers import MedicalHistorySerializer
from .models import MedicalHistory
from rest_framework import generics

class MedicalHistoryCreateView(generics.CreateAPIView):
    serializer_class = MedicalHistorySerializer