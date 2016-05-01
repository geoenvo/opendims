# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20160429_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('DISASTER_INFO', 'Disaster information'), ('WATERLEVEL_INFO', 'Water level information')], default='DISASTER_INFO', max_length=50, verbose_name='Subject'),
        ),
    ]