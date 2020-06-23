from django.db import models


class Message(models.Model):
    SENT = 'SENT'
    NOT_SENT = 'NOT_SENT'

    STATUS_CHOICES = (
        (SENT, 'Отправлено'),
        (NOT_SENT, 'Не отправлено')
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=NOT_SENT
    )
    email = models.EmailField(
        verbose_name='Адрес отправителя'
    )
    body = models.TextField(
        verbose_name='Содержание'
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )