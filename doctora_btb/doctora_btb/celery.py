import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctora_btb.settings')

celery_app = Celery('doctora_btb')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'send-mail-every-hour': {
        'task': 'main.tasks.send_unsent_mail',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}