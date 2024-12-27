from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_delivery_person = models.BooleanField(default=False)
    pass

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Custom related_name to avoid conflicts
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Custom related_name to avoid conflicts
        blank=True,
    )
