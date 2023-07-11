from rest_framework import serializers
from .models import Order
from users.models import User


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "product", "user", "created_at", "amount", "total", "status"]


class OrderStatusSerializer(serializers.ModelSerializer):
    user = UserEmailSerializer()
    class Meta:
        model = Order
        fields = ["id", "product", "user", "created_at", "amount", "total", "status"]
        extra_kwargs = {
            "id": {"read_only": True},
            "product": {"read_only": True},
            "user": {"read_only": True},
            "created_at": {"read_only": True},
            "amount": {"read_only": True},
            "total": {"read_only": True},
        }
        depth = 1
