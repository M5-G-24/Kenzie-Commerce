from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelField):
    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "carts"]
