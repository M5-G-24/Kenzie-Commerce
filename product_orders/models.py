from django.db import models


class ProductOrder(models.Model):
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="order_product_order"
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="product_product_order",
    )
    amount = models.IntegerField()
