from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    user = models.ForeignKey("users.User", models.CASCADE, related_name="user_products")
