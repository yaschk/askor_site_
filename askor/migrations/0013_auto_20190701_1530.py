# Generated by Django 2.2.1 on 2019-07-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askor', '0012_auto_20190630_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='name_ru',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_uk',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
