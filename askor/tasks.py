from __future__ import absolute_import, unicode_literals
from celery import task
from django.core.management import call_command

@task()
def update_rates():
    call_command('updatecurrencies')
