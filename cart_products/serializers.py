from rest_framework import serializers
from .models import CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = CartProduct
        fields = ["id", "cart", "product", "amount", "total"]
        extra_kwargs = {"id": {"read_only": True}, "cart": {"read_only": True}}

    def get_total(self, obj):
        return obj.total


class CartProductUpdateSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = CartProduct
        fields = ["id", "cart", "product", "amount", "total"]
        extra_kwargs = {
            "id": {"read_only": True},
            "cart": {"read_only": True},
            "product": {"read_only": True},
        }

    def get_total(self, obj):
        return obj.total
