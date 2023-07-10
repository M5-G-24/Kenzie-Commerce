from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "street", "number", "zip_code", "user"]
        extra_kwargs = {"user": {"read_only": True}}
