# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-13 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolevels', '0002_auto_20160530_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name_plural': 'Provinces'},
        ),
        migrations.AlterModelOptions(
            name='rt',
            options={'verbose_name_plural': 'RTs'},
        ),
        migrations.AlterModelOptions(
            name='rw',
            options={'verbose_name_plural': 'RWs'},
        ),
        migrations.AlterModelOptions(
            name='subdistrict',
            options={'verbose_name_plural': 'Subdistricts'},
        ),
        migrations.AlterModelOptions(
            name='village',
            options={'verbose_name_plural': 'Villages'},
        ),
    ]
