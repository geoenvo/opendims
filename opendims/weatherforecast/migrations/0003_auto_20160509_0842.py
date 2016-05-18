# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-09 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherforecast', '0002_auto_20160503_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherforecastreport',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='forecast',
            field=models.CharField(blank=True, choices=[('CERAH', 'Clear'), ('CERAH BERAWAN', 'Partly cloudy'), ('BERAWAN', 'Cloudy'), ('HUJAN RINGAN', 'Light rain'), ('HUJAN SEDANG', 'Moderate rain'), ('HUJAN DERAS', 'Heavy rain')], max_length=50, verbose_name='Forecast'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='forecast_morning',
            field=models.CharField(blank=True, choices=[('CERAH', 'Clear'), ('CERAH BERAWAN', 'Partly cloudy'), ('BERAWAN', 'Cloudy'), ('HUJAN RINGAN', 'Light rain'), ('HUJAN SEDANG', 'Moderate rain'), ('HUJAN DERAS', 'Heavy rain')], max_length=50, verbose_name='Morning forecast'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='forecast_night',
            field=models.CharField(blank=True, choices=[('CERAH', 'Clear'), ('CERAH BERAWAN', 'Partly cloudy'), ('BERAWAN', 'Cloudy'), ('HUJAN RINGAN', 'Light rain'), ('HUJAN SEDANG', 'Moderate rain'), ('HUJAN DERAS', 'Heavy rain')], max_length=50, verbose_name='Night forecast'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='forecast_noon',
            field=models.CharField(blank=True, choices=[('CERAH', 'Clear'), ('CERAH BERAWAN', 'Partly cloudy'), ('BERAWAN', 'Cloudy'), ('HUJAN RINGAN', 'Light rain'), ('HUJAN SEDANG', 'Moderate rain'), ('HUJAN DERAS', 'Heavy rain')], max_length=50, verbose_name='Noon forecast'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='humidity_max',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Humidity max'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='humidity_min',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Humidity min'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='temperature_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Temperature max'),
        ),
        migrations.AlterField(
            model_name='weatherforecastreport',
            name='temperature_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Temperature min'),
        ),
    ]