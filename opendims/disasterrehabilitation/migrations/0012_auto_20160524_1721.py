# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasterrehabilitation', '0011_activity_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='created',
        ),
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.DateField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start',
            field=models.DateField(verbose_name='Start date'),
        ),
    ]
