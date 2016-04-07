# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 13:12
from __future__ import unicode_literals

from decimal import Decimal
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolevels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Code')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Point')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=50, verbose_name='Status')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Height')),
                ('magnitude', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Magnitude')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.City', verbose_name='City')),
                ('disaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Disaster', verbose_name='Disaster')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Province', verbose_name='Province')),
                ('rt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.RT', verbose_name='RT')),
                ('rw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.RW', verbose_name='RW')),
                ('subdistrict', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Subdistrict', verbose_name='Subdistrict')),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Village', verbose_name='Village')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('status', models.CharField(choices=[('VERIFIED', 'Verified'), ('UNVERIFIED', 'Unverified'), ('PENDING', 'Pending')], default='PENDING', max_length=50, verbose_name='Status')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='reports.Event', verbose_name='Event')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Code')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='report',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Source', verbose_name='Source'),
        ),
    ]
