from rest_framework import serializers
from .models import Order
from cart_products.models import CartProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "product", "user", "created_at", "amount", "total", "status"]


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status"]
