
#
# from celery import Celery

#
#
# app = Celery('askor_site_', broker='pyamqp://guest@localhost//')
#
#
# @app.task
# def update_rates(backend=settings.EXCHANGE_BACKEND, **kwargs):
#     backend = import_string(backend)()
#     backend.update_rates(**kwargs)

from __future__ import absolute_import, unicode_literals
from django.utils.module_loading import import_string
from celery import task
from djmoney import settings


@task()
def update_rates(backend=settings.EXCHANGE_BACKEND, **kwargs):
    backend = import_string(backend)()
    backend.update_rates(**kwargs)
    print('YO YO YO')