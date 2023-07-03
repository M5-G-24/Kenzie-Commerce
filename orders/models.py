from django.db import models


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
    cart_product = models.ForeignKey(
        "cart_products.CartProduct",
        on_delete=models.CASCADE,
        related_name="cart_product_order",
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_orders"
    )
