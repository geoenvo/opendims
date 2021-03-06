# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 05:54
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('disasterrehabilitation', '0004_auto_20160428_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventassesment',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 4, 29, 5, 54, 8, 767856, tzinfo=utc), verbose_name='Updated'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='funding',
            field=models.CharField(choices=[('APBN', 'APBN'), ('APBD', 'APBD'), ('CSR', 'CSR'), ('PUBLIC', 'PUBLIC'), ('OTHER', 'OTHER')], default='APBD', max_length=50, verbose_name='Funding'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('PHYSICAL', 'PHYSICAL'), ('NON-PHYSICAL', 'NON-PHYSICAL')], default='PHYSICAL', max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)], verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='eventassesment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
