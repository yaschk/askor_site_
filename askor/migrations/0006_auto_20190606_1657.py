# Generated by Django 2.2.1 on 2019-06-06 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askor', '0005_auto_20190606_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock_uk',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name_uk',
        ),
    ]
