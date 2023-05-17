from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DentistSerializer , PatientSerializer
from .models import Dentist , Patient
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class DentistRegistrationView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    permission_classes = [IsAuthenticated]

class PatientCreateView(generics.CreateAPIView):
    serializer_class = PatientSerializer