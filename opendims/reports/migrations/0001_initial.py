# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 09:51
from __future__ import unicode_literals

from decimal import Decimal
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('created', models.DateTimeField()),
                ('height', models.PositiveIntegerField(default=0)),
                ('magnitude', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=50)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Disaster')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kejadian', models.DateTimeField(auto_now=True, verbose_name='Tanggal Kejadian')),
                ('status', models.CharField(choices=[('Un', 'Unverivied'), ('V', 'Verified'), ('Tbd', 'To be Determined')], max_length=50)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('note', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Source'),
        ),
    ]
