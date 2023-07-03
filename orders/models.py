from django.db import models
from carts.models import Cart


class Order(models.Model):
    status = models.CharField(
        max_length=120,
        choices=[
            ("PLACED", "placed"),
            ("PROGRESS", "progress"),
            ("DELIVERED", "delivered"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    carts = models.ManyToManyField(Cart, related_name="orders")
