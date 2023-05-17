from rest_framework import serializers
from .models import Dentist , Patient

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'