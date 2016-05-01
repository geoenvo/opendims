# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-30 06:45
from __future__ import unicode_literals

import common.validators
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_post_slideshow_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='website/attachment_image/', validators=[common.validators.FileSizeValidator(1)], verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='image_preview',
            field=image_cropping.fields.ImageRatioField('image', '260x180', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Image preview (260x180 px)'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='image_thumb',
            field=image_cropping.fields.ImageRatioField('image', '70x70', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Image thumb (70x70 px)'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='siteheader',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='website/attachment_file/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='website.Post', verbose_name='Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='siteheader',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='website/siteheader/', validators=[common.validators.FileSizeValidator(1)], verbose_name='Image'),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('id', 'slug')]),
        ),
    ]