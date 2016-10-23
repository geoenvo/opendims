# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-21 08:10
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20161021_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'get_latest_by': 'created', 'ordering': ['created'], 'verbose_name_plural': 'Videos'},
        ),
        migrations.AddField(
            model_name='siteheader',
            name='background_color',
            field=colorfield.fields.ColorField(default='#003a6a', max_length=10),
        ),
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created'),
        ),
    ]
