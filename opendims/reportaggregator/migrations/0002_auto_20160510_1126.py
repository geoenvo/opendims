# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reportaggregator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='reportaggregator.Source', verbose_name='Source'),
        ),
    ]