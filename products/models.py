from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    disponibility = models.CharField(
        max_length=11,
        choices=[
            ("AVALIABLE", "Avaliable"),
            ("UNAVALIABLE", "Unavaliable"),
        ],
    )
