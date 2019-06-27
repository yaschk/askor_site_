from __future__ import absolute_import, unicode_literals
from django.utils.module_loading import import_string
from celery import task
from djmoney import settings
from askor_site_.settings import dev

if not dev:
    @task()
    def update_rates(backend=settings.EXCHANGE_BACKEND, **kwargs):
        backend = import_string(backend)()
        backend.updatecurrencies(**kwargs)
