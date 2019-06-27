from __future__ import absolute_import, unicode_literals
from django.utils.module_loading import import_string
from celery import task
from askor_site_.settings import dev
import logging
from datetime import datetime
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from currencies.models import Currency
from django.core.management import call_command

@task()
def update_rates():
    # os.system("python manage.py updatecurrencies oxr --base=USD")
    print('Hello')
    call_command('updatecurrencies oxr --base=USD')
