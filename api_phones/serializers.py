from rest_framework import serializers

from operation.models import PhonesList


class PhonesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesList
        fields = [
            'phone',
            'added_date'
        ]
