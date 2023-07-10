from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "id": {"read_only": True},
            "seller": {"source": "user", "read_only": True},
        }
        model = Product
        fields = ("id", "name", "category", "price", "stock", "seller")

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["seller"] = instance.user.username
        return representation
