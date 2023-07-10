from django.db import models


class StatusChoices(models.TextChoices):
    placed = "placed"
    progress = "progress"
    delivered = "delivered"


class Order(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_orders",
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="product_orders"
    )
    amount = models.IntegerField()
    total = models.FloatField()
    status = models.CharField(
        max_length=120,
        choices=StatusChoices.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
