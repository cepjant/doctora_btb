from celery import shared_task
from django.core.mail import send_mail


@shared_task
def async_send_mail(name, message, host, to):
    send_mail(f'feedback from {name}', message, host, to)
