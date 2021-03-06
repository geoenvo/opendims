# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20160427_1613'),
        ('disasterrehabilitation', '0005_auto_20160429_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
                ('file', models.FileField(blank=True, null=True, upload_to='disasterrehabilitation/eventassessment/', verbose_name='File')),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Event', verbose_name='Event')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.RemoveField(
            model_name='eventassesment',
            name='event',
        ),
        migrations.RemoveField(
            model_name='location',
            name='eventassesment',
        ),
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='funding',
            field=models.CharField(choices=[('APBN', 'APBN'), ('APBD', 'APBD'), ('CSR', 'CSR'), ('PUBLIC', 'Public'), ('OTHER', 'Other')], default='APBD', max_length=50, verbose_name='Funding'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start',
            field=models.DateTimeField(verbose_name='Start date'),
        ),
        migrations.DeleteModel(
            name='EventAssesment',
        ),
        migrations.AddField(
            model_name='location',
            name='eventassessment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disasterrehabilitation.EventAssessment', verbose_name='Event assessment'),
        ),
    ]
