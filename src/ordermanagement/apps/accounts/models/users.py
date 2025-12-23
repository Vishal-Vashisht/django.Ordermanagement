from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel


class User(AbstractUser, BaseModel):
    """User Model."""
    email = models.EmailField(
        verbose_name="User Email",
        unique=True,
    )
    phone = models.CharField(
        max_length=20, blank=True
    )
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
