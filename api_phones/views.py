from rest_framework import generics
from .serializers import PhoneInBlacklistSerializer, PhonesListSerializer
from operation.models import PhonesList


class ApiCheckPhoneView(generics.RetrieveAPIView):
    serializer_class = PhoneInBlacklistSerializer
    lookup_field = 'phone'

    def get_queryset(self):
        return PhonesList.objects.all()


class ApiGetPhonesView(generics.ListAPIView):
    queryset = PhonesList.objects.filter(status=True)
    serializer_class = PhonesListSerializer
