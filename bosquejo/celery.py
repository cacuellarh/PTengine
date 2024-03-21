import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bosquejo.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('bosquejo')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


