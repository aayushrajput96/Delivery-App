# api/models.py
from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=255)  # Example field
    delivery_address = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
