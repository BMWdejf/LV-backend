import os
from core.celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('products')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()