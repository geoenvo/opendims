# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20160518_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
    ]