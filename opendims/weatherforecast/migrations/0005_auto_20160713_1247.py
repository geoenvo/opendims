# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-13 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherforecast', '0004_auto_20160516_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherforecastreport',
            options={'get_latest_by': 'pk', 'ordering': ['pk'], 'verbose_name_plural': 'Weather forecast reports'},
        ),
    ]