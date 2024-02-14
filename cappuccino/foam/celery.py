import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foam.settings")
app = Celery("cappuccino")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
