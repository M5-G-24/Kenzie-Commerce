from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)
