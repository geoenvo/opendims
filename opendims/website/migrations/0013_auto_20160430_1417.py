# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20160430_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='name',
        ),
        migrations.AddField(
            model_name='attachment',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Title'),
        ),
    ]
