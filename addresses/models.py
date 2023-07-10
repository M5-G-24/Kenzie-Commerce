from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=120)
    number = models.IntegerField()
    zip_code = models.CharField(max_length=120)
    user = models.OneToOneField(
        "users.User", models.CASCADE, related_name="user_address"
    )
