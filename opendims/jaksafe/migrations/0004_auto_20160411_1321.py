# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jaksafe', '0003_auto_20160408_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportautosummary',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geolevels.Village', verbose_name='Village'),
        ),
    ]