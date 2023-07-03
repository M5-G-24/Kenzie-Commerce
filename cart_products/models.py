from django.db import models


class CartProduct(models.Model):
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.IntegerField()
