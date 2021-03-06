# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 04:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20160416_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimpact',
            name='evac_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Evacuation point'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='evac_total',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Evacuated total'),
        ),
    ]
