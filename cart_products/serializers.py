from rest_framework import serializers
from .models import CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id", "user", "product", "amount"]
        extra_kwargs = {"user": {"read_only": True}, "total": {"read_only": True}}

    def create(self, validated_data):
        return CartProduct.objects.create(**validated_data)


class CartProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id", "user", "product", "amount"]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
            "product": {"read_only": True},
        }
