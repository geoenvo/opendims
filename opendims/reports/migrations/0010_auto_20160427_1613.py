# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_event_height_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='closed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Closed'),
        ),
    ]
