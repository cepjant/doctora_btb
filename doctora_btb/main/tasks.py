import datetime
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Message



@shared_task
def async_send_mail(name, message_text, host, recipient, mes_id):

    obj = Message.objects.get(id=mes_id)
    try:
        send_mail(f'feedback from {name}', message_text, host, recipient)
        obj.status = 'SENT'
        obj.save()
    except Exception as e:
        obj.status = 'UNSENT'
        obj.error = e.args
        obj.save()


@shared_task
def send_unsent_mail():
    for mes in Message.objects.filter(status='UNSENT'):
        date = datetime.datetime.now().date()
        if str(mes.date).split(' ')[0] == str(date):
            message_text = f'Отправитель:\n' \
                           f'Имя: {mes.name}\n' \
                           f'email: {mes.email}\n\nТекст сообщения:\n{mes.body}'
            async_send_mail(mes.name, message_text, settings.EMAIL_HOST_USER, ['fokewet226@qlevjh.com'], mes.id)
