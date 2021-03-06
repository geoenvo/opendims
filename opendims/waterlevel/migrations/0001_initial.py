# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 13:13
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterGate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Point')),
                ('siaga_1_min', models.PositiveIntegerField(default=0, verbose_name='Siaga 1 min')),
                ('siaga_1_max', models.PositiveIntegerField(default=0, verbose_name='Siaga 1 max')),
                ('siaga_2_min', models.PositiveIntegerField(default=0, verbose_name='Siaga 2 min')),
                ('siaga_2_max', models.PositiveIntegerField(default=0, verbose_name='Siaga 2 max')),
                ('siaga_3_min', models.PositiveIntegerField(default=0, verbose_name='Siaga 3 min')),
                ('siaga_3_max', models.PositiveIntegerField(default=0, verbose_name='Siaga 3 max')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WaterLevelReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Height')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('weather', models.CharField(choices=[('T', 'Terang/Cerah'), ('MT', 'Mendung Tipis'), ('M', 'Mendung'), ('G', 'Gerimis'), ('H', 'Hujan')], default='T', max_length=50, verbose_name='Weather')),
                ('watergate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waterlevelreports', to='waterlevel.WaterGate', verbose_name='Water gate')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'get_latest_by': 'updated',
            },
        ),
    ]
