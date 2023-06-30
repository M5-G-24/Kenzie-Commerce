from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.tokens import PasswordResetTokenGenerator


class User(AbstractUser):
    is_active = models.BooleanField(default=False)
    email = models.EmailField(blank=False)
    role = models.CharField(
        max_length=10,
        choices=[
            ("ADMIN", "Administrator"),
            ("SELLER", "Seller"),
            ("CUSTOMER", "Customer"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
