# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disasterrehabilitation', '0012_auto_20160524_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'get_latest_by': 'pk', 'ordering': ['pk'], 'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'get_latest_by': 'pk', 'ordering': ['pk'], 'verbose_name_plural': 'agencies'},
        ),
        migrations.AlterModelOptions(
            name='eventassessment',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='reference',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
    ]
