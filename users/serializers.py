from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from carts.serializers import CartSerializer
from carts.models import Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_active", "email", "password", "username", "is_staff", "user_cart"]
        extra_kwargs = {
            "is_staff": {"read_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "password": {"write_only": True},
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
            "user_cart": {'read_only': True}
        }
        user_cart = CartSerializer()

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        cart = Cart.objects.create(user=user)
        return user