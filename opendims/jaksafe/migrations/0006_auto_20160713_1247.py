# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-13 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jaksafe', '0005_auto_20160531_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportautosummary',
            options={'get_latest_by': 'pk', 'ordering': ['pk'], 'verbose_name_plural': 'Report auto summarys'},
        ),
    ]