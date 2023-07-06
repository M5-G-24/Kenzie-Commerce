from django.db import models
from products.models import Product
from math import ceil


class CartProduct(models.Model):
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.FloatField()

    def save(self, *args, **kwargs):
        self.total = ceil(self.product.price * self.amount * 100) / 100
        super().save(*args, **kwargs)