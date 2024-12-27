from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_notification(email, order_id):
    send_mail(
        'Order Update',
        f'Your order {order_id} has been updated.',
        'from@example.com',
        [email],
    )
    
@shared_task
def add(x, y):
    return x + y