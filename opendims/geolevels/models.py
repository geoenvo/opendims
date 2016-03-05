from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.core import urlresolvers


class GeolevelsAbstractModel(models.Model):
    class Meta:
        abstract = True
    
    def get_admin_url(self):
        return urlresolvers.reverse(
            'admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=(self.id,)
        )


verbose_note = _('Note')
verbose_name = _('Name')
verbose_polygon = _('Polygon')


class Province(GeolevelsAbstractModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return self.name


verbose_province = _('Province')


class City(GeolevelsAbstractModel):
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Province, verbose_name=verbose_province)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    class Meta:
        verbose_name_plural = _('Cities')
    
    def __unicode__(self):
        return self.name


verbose_city = _('City')


class Subdistrict(GeolevelsAbstractModel):
    id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City, verbose_name=verbose_city)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return self.name


verbose_subdistrict = _('Subdistrict')


class Village(GeolevelsAbstractModel):
    id = models.BigIntegerField(primary_key=True)
    subdistrict = models.ForeignKey(Subdistrict, verbose_name=verbose_subdistrict)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return self.name


verbose_village = _('Village')
verbose_rw = _('RW')


class RW(GeolevelsAbstractModel):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, verbose_name=verbose_village)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    class Meta:
        verbose_name = verbose_rw
    
    def __unicode__(self):
        return self.name


verbose_rt = _('RT')


class RT(GeolevelsAbstractModel):
    id = models.BigIntegerField(primary_key=True)
    rw = models.ForeignKey(RW, verbose_name=verbose_rw)
    name = models.CharField(max_length=50, verbose_name=verbose_name)
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=verbose_polygon)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    class Meta:
        verbose_name = verbose_rt
    
    def __unicode__(self):
        return self.name
