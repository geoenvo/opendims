# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolevels', '0001_initial'),
        ('reports', '0009_event_height_min'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(verbose_name='End Date')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('type', models.CharField(choices=[('Physical', 'Physical'), ('Non-Physical', 'Non-Physical')], default='Physical', max_length=50, verbose_name='Type')),
                ('funding', models.CharField(choices=[('APBN', 'APBN'), ('APBD', 'APBD'), ('Society Funds', 'Society Funds'), ('CSR', 'CSR')], default='Physical', max_length=50, verbose_name='Funding')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterrehabilitation.Activity', verbose_name='Activity')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.City', verbose_name='City')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='PostAssesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('file', models.FileField(blank=True, null=True, upload_to='disasterrehabilitation/postassesment/', verbose_name='File')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Event')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('file', models.FileField(blank=True, null=True, upload_to='disasterrehabilitation/reference/', verbose_name='File')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterrehabilitation.Activity', verbose_name='Activity')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'get_latest_by': 'updated',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='postassesment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterrehabilitation.PostAssesment', verbose_name='Post Assesment'),
        ),
        migrations.AddField(
            model_name='location',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Province', verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='location',
            name='rt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.RT', verbose_name='RT'),
        ),
        migrations.AddField(
            model_name='location',
            name='rw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.RW', verbose_name='RW'),
        ),
        migrations.AddField(
            model_name='location',
            name='subdistrict',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Subdistrict', verbose_name='Subdistrict'),
        ),
        migrations.AddField(
            model_name='location',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolevels.Village', verbose_name='Village'),
        ),
        migrations.AddField(
            model_name='activity',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterrehabilitation.Agency', verbose_name='Agency'),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Event'),
        ),
    ]