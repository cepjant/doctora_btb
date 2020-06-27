from celery import shared_task
from django.core.mail import send_mail
from .models import Message


@shared_task
def async_send_mail(name, message_text, host, recipient, body, email):
    message = Message(body=body, name=name, email=email)
    try:
        send_mail(f'feedback from {name}', message_text, host, recipient)
        message.status = 'SENT'
        message.save()
    except:
        message.status = 'NOT_SENT'
        message.save()