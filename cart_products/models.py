from django.db import models

class CartProduct(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.FloatField()