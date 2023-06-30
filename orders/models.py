from django.db import models


class OrderModel(models.Model):
    status = models.CharField(
        max_length=120,
        choices=[
            ("PLACED", "placed"),
            ("PROGRESS", "progress"),
            ("DELIVERED", "delivered"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    carts = models.ManyToManyField("Carts.cart", related_name="orders")
