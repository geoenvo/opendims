# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 06:55
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20160427_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='image_preview',
            field=image_cropping.fields.ImageRatioField('image', '260x180', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Image preview (260x180 px)'),
        ),
        migrations.AddField(
            model_name='eventimage',
            name='image_thumb',
            field=image_cropping.fields.ImageRatioField('image', '70x70', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Image thumb (70x70 px)'),
        ),
    ]