from django.db import models


class Message(models.Model):
    SENT = 'SENT'
    UNSENT = 'UNSENT'

    STATUS_CHOICES = (
        (SENT, 'Отправлено'),
        (UNSENT, 'Не отправлено')
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=UNSENT
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
    error = models.TextField(
        verbose_name='Ошибка отправки',
        default='NULL',
    )
    date = models.DateTimeField(
        auto_now_add=True
    )