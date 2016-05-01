# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 08:14
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160426_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slideshow_image_crop',
            field=image_cropping.fields.ImageRatioField('slideshow_image', '770x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='slideshow image crop'),
        ),
    ]