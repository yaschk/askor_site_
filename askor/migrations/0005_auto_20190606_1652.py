# Generated by Django 2.2.1 on 2019-06-06 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askor', '0004_auto_20190606_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='add_info_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='add_info_uk',
        ),
    ]
