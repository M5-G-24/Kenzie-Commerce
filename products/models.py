from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    disponibility = models.CharField(
        max_length=120,
        choices=[
            ("AVAILABLE", "Available"),
            ("UNAVAILABLE", "Unavailable"),
        ],
    )
    user = models.ForeignKey("users.User", models.CASCADE, related_name="user_products")
