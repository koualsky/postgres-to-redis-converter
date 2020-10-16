import os
from celery import Celery
from time import sleep
from django.conf import settings


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
settings.configure()

app = Celery('celerys', backend='rpc://', broker='amqp://guest:guest@rabbitmq:5672')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
