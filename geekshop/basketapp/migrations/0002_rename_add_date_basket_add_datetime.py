# Generated by Django 3.2.8 on 2021-10-14 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='add_date',
            new_name='add_datetime',
        ),
    ]
