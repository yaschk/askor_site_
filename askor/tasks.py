from __future__ import absolute_import, unicode_literals
from django.utils.module_loading import import_string
from celery import task
from askor_site_.settings import dev
import os


@task()
def update_rates():
    # os.system("python manage.py updatecurrencies oxr --base=USD")
    print('Hello')


