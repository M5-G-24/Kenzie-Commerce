from rest_framework import serializers
from .models import Order
from cart_products.models import CartProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "product", "user" "created_at", "amount", "total", "status"]

    def create(self, validated_data, cart_product_id) -> Order:
        cart_product = CartProduct.objects.get(cart_product_id)

        for cart_product["product_id"] in cart_product:
            Order.objects.create()
