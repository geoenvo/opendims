from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse

from common.models import CommonAbstractModel
from common.validators import MimetypeValidator, FileSizeValidator


verbose_id = _('ID')
verbose_note = _('Note')
verbose_name = _('Name')
verbose_polygon = _('Polygon')
verbose_geojson = _('GeoJSON')


class Province(CommonAbstractModel):
    id = models.IntegerField(primary_key=True, verbose_name=verbose_id)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/province/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('Provinces')

    def get_absolute_url(self):
        return reverse('geolevels:province_detail', args=[self.pk])

    def __unicode__(self):
        return self.name


verbose_province = _('Province')


class City(CommonAbstractModel):
    id = models.IntegerField(primary_key=True, verbose_name=verbose_id)
    province = models.ForeignKey(Province, verbose_name=verbose_province)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/city/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('Cities')

    def get_absolute_url(self):
        return reverse('geolevels:city_detail', args=[self.pk])

    def __unicode__(self):
        return self.name


verbose_city = _('City')


class Subdistrict(CommonAbstractModel):
    id = models.IntegerField(primary_key=True, verbose_name=verbose_id)
    city = models.ForeignKey(City, verbose_name=verbose_city)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/subdistrict/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('Subdistricts')

    def get_absolute_url(self):
        return reverse('geolevels:subdistrict_detail', args=[self.pk])

    def __unicode__(self):
        return self.name


verbose_subdistrict = _('Subdistrict')


class Village(CommonAbstractModel):
    id = models.BigIntegerField(primary_key=True, verbose_name=verbose_id)
    subdistrict = models.ForeignKey(
        Subdistrict,
        verbose_name=verbose_subdistrict
    )
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/village/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('Villages')

    def get_absolute_url(self):
        return reverse('geolevels:village_detail', args=[self.pk])

    def __unicode__(self):
        return self.name


verbose_village = _('Village')
verbose_rw = _('RW')


class RW(CommonAbstractModel):
    id = models.BigIntegerField(primary_key=True, verbose_name=verbose_id)
    village = models.ForeignKey(Village, verbose_name=verbose_village)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/rw/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('RWs')

    def get_absolute_url(self):
        return reverse('geolevels:rw_detail', args=[self.pk])

    def __unicode__(self):
        return self.name


verbose_rt = _('RT')


class RT(CommonAbstractModel):
    id = models.BigIntegerField(primary_key=True, verbose_name=verbose_id)
    rw = models.ForeignKey(RW, verbose_name=verbose_rw)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(
        null=True,
        blank=True,
        verbose_name=verbose_polygon
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    geojson = models.FileField(
        null=True,
        blank=True,
        upload_to='geolevels/rt/',
        validators=[
            MimetypeValidator(('text/plain', 'application/json')),
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_geojson
    )

    class Meta:
        verbose_name_plural = _('RTs')

    def get_absolute_url(self):
        return reverse('geolevels:rt_detail', args=[self.pk])

    def __unicode__(self):
        return self.name
