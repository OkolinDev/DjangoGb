# Generated by Django 3.2.8 on 2021-10-21 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20211021_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 13, 26, 32, 294408, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
