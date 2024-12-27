# # from django.db import models
# # from django.conf import settings

# # class Order(models.Model):
# #     customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
# #     pickup_address = models.CharField(max_length=255)
# #     dropoff_address = models.CharField(max_length=255)
# #     package_details = models.TextField()
# #     delivery_person = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='deliveries')
# #     status = models.CharField(choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], max_length=20)
# #     created_at = models.DateTimeField(auto_now_add=True)
# from django.db import models
# from django.contrib.auth.models import User

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     delivery_address = models.CharField(max_length=255)
#     delivery_time = models.DateTimeField(null=True, blank=True)

# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Pending')  # e.g., Pending, In Progress, Delivered
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField(null=True, blank=True)