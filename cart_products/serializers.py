from rest_framework import serializers
from .models import CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id", "cart", "product", "amount"]
