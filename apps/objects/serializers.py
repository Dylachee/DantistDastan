from rest_framework import serializers
from .models import MedicalHistory , DentalService

class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

class DentalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalService
        fields = '__all__'  