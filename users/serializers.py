from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "is_active",
            "email",
            "role",
            "password",
            "username",
            "is_staff"
        ]
        extra_kwargs = {
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
        }

    def create(self, validated_data: dict) -> User:     
        if validated_data.get('role') == "Administrator":
            return User.objects.create_superuser(**validated_data)  
        else:
            return User.objects.create_user(**validated_data)
       
        
      