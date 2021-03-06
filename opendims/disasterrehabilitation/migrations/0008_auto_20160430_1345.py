# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disasterrehabilitation', '0007_auto_20160429_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'get_latest_by': 'updated', 'ordering': ['-updated', '-created'], 'verbose_name': 'activity', 'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ['name'], 'verbose_name': 'agency', 'verbose_name_plural': 'agencies'},
        ),
    ]
