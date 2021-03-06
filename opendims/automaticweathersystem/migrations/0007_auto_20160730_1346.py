# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-30 06:46
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('automaticweathersystem', '0006_auto_20160713_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('temperature', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Temperature')),
                ('humidity', models.PositiveIntegerField(blank=True, null=True, verbose_name='Humidity')),
                ('pressure', models.PositiveIntegerField(blank=True, null=True, verbose_name='Pressure')),
                ('wind_speed', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Wind speed')),
                ('wind_direction', models.PositiveIntegerField(blank=True, null=True, verbose_name='Wind direction')),
                ('day_rain', models.PositiveIntegerField(blank=True, null=True, verbose_name='Day rain')),
                ('rain_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Rain rate')),
                ('uv_index', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='UV index')),
                ('solar_radiation', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Solar radiation')),
            ],
            options={
                'ordering': ['pk'],
                'get_latest_by': 'pk',
                'verbose_name_plural': 'Sensor reports',
            },
        ),
        migrations.RenameModel(
            old_name='AWSStation',
            new_name='SensorStation',
        ),
        migrations.RemoveField(
            model_name='awsreport',
            name='awsstation',
        ),
        migrations.AlterModelOptions(
            name='sensorstation',
            options={'verbose_name_plural': 'Sensor stations'},
        ),
        migrations.DeleteModel(
            name='AWSReport',
        ),
        migrations.AddField(
            model_name='sensorreport',
            name='sensorstation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automaticweathersystem.SensorStation', verbose_name='Sensor station'),
        ),
    ]
