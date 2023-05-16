from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DentistSerializer
from .models import Dentist
from rest_framework.permissions import IsAuthenticated

class DentistRegistrationView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    permission_classes = [IsAuthenticated]