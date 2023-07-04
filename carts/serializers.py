from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        extra_kwargs = {"id": {"read_only": True}, "user": {"read_only": True}}
        fields = ["id", "user"]
