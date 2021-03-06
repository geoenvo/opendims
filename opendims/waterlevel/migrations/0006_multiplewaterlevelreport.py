# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-24 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterlevel', '0005_auto_20160713_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleWaterLevelReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_level_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='waterlevel.WaterLevelReport')),
            ],
            options={
                'ordering': ['-pk'],
                'get_latest_by': 'pk',
                'verbose_name_plural': 'Multiple Water Level Report',
            },
        ),
    ]
