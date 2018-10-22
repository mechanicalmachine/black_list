from rest_framework import serializers
from operation.models import PhonesList


class PhoneInBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesList
        fields = ('phone', )

    def to_representation(self, phone):
        super(PhoneInBlacklistSerializer, self).to_representation(phone)
        return {
            "in_blacklist": phone.status,
            "in_blacklist_since": phone.added_date
        }


class PhonesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonesList
        fields = ('phone', 'added_date')

    def to_representation(self, phone):
        super(PhonesListSerializer, self).to_representation(phone)
        return {
            "phone_number": phone.phone,
            "in_blacklist_since": phone.added_date
        }
