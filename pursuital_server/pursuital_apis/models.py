from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("user", "User"),
        ("manager", "Manager"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
