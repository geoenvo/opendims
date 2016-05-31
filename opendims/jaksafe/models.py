from __future__ import unicode_literals

from decimal import Decimal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

from common.models import CommonAbstractModel
from geolevels.models import Village

verbose_created = _('Created')
verbose_infradamage = _('Infrastructure damage')
verbose_infraloss = _('Infrastructure loss')
verbose_sectordamage = _('Cross-sector damage')
verbose_sectorloss = _('Cross-sector loss')
verbose_productdamage = _('Productive damage')
verbose_productloss = _('Productive loss')
verbose_socialdamage = _('Social-Housing damage')
verbose_socialloss = _('Social-Housing loss')
verbose_totaldamage = _('Total damage')
verbose_totalloss = _('Total loss')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_source = _('Source')
verbose_note = _('Note')


class ReportAutoSummary(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    village = models.ForeignKey(
        Village,
        verbose_name=verbose_village
    )
    rw = models.TextField(blank=True, verbose_name=verbose_rw)
    source = models.URLField(
        blank=True,
        default='',
        verbose_name=verbose_source)
    note = models.TextField(blank=True, default='', verbose_name=verbose_note)
    damage_infrastruktur = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_infradamage
    )
    loss_infrastruktur = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_infraloss
    )
    damage_lintas_sektor = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_sectordamage
    )
    loss_lintas_sektor = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_sectorloss
    )
    damage_produktif = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_productdamage
    )
    loss_produktif = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_productloss
    )
    damage_sosial_perumahan = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_socialdamage
    )
    loss_sosial_perumahan = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_socialloss
    )
    damage_total = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_totaldamage
    )
    loss_total = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        verbose_name=verbose_totalloss
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'

    def get_absolute_url(self):
        return reverse('jaksafe:reportautosummary_detail', args=[self.pk])

    def __unicode__(self):
        return '[%s] - %s' % (self.village, timezone.localtime(self.created))
