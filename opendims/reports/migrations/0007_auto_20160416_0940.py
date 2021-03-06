# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 02:40
from __future__ import unicode_literals

import common.validators
from decimal import Decimal
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20160415_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventimage',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='eventimpact',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reports/event_image/', validators=[common.validators.FileSizeValidator(1)], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='order',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='affected_death',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Affected death'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='affected_injury',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Affected injury'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='affected_total',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Affected total'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='evac_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Evacution point'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='evac_total',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Evacution total'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='loss_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Loss total'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='note',
            field=models.TextField(blank=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='rt_text',
            field=models.TextField(blank=True, verbose_name='RT text'),
        ),
    ]
