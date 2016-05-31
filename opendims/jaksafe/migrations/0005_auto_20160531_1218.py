# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaksafe', '0004_auto_20160411_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportautosummary',
            options={'get_latest_by': 'pk', 'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='damage_infrastruktur',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Infrastructure damage'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='damage_lintas_sektor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Cross-sector damage'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='damage_produktif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Productive damage'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='damage_sosial_perumahan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Social-Housing damage'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='damage_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Total damage'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='loss_infrastruktur',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Infrastructure loss'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='loss_lintas_sektor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Cross-sector loss'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='loss_produktif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Productive loss'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='loss_sosial_perumahan',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Social-Housing loss'),
        ),
        migrations.AlterField(
            model_name='reportautosummary',
            name='loss_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Total loss'),
        ),
    ]