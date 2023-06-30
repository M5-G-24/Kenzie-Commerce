from rest_framework import serializers
from .models import OrderModel


class OrderSerializer(serializers.ModelField):
    class Meta:
        model = OrderModel
        fields = ["id", "status", "created_at", "carts"]
