# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_trips_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='start',
            field=models.DateField(),
        ),
    ]