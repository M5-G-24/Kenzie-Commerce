from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "id": {"read_only": True},
        }
        model = Product
        fields = ("id", "name", "category", "price", "stock", "availability")

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
