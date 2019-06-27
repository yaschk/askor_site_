from __future__ import absolute_import, unicode_literals
from celery import task
from django.core.management import call_command

@task()
def update_rates():
<<<<<<< HEAD
    # os.system("python manage.py updatecurrencies oxr --base=USD")
    print('Hello')
=======
>>>>>>> f05c8e7c9cc68545759eeeb22004c507837b1592
    call_command('updatecurrencies')
