# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-24 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterlevel', '0006_multiplewaterlevelreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplewaterlevelreport',
            name='water_level_report',
        ),
        migrations.AddField(
            model_name='waterlevelreport',
            name='multiple_water_level_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waterlevel.MultipleWaterLevelReport'),
        ),
    ]
