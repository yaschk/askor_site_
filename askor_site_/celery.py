from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from askor_site_.settings import dev




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askor_site_.settings')

app = Celery('askor_site_')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))