# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 10:12
from __future__ import unicode_literals

import common.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20160415_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='eventimages', to='reports.Event', verbose_name='Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventimpact',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='eventimpacts', to='reports.Event', verbose_name='Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reports/event_image', validators=[common.validators.MimetypeValidator('application/png'), common.validators.FileSizeValidator(1)]),
        ),
        migrations.AlterField(
            model_name='eventimpact',
            name='rt_text',
            field=models.TextField(blank=True, verbose_name='RT Text'),
        ),
    ]