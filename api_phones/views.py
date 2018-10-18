from rest_framework import generics
from .serializers import PhonesListSerializer
from operation.models import PhonesList


class ApiPhonesRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhonesListSerializer
    lookup_field = 'phone'

    def get_queryset(self):
        return PhonesList.objects.all()

