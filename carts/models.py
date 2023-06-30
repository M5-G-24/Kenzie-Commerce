from django.db import models
from users.models import User
from products.models import Product


class Cart(models.Model):
    class Meta:
        ordering = ["id"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    products = models.ManyToManyField(Product)
