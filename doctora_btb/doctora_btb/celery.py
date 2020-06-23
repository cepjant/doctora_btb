import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctora_btb.settings')

celery_app = Celery('doctora_btb')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()