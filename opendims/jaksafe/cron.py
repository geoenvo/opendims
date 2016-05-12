import logging
import requests
from decimal import Decimal
import time

from django.conf import settings

from .models import ReportAutoSummary
from geolevels.models import Village


def jaksafe_scheduled_job():
    logger = logging.getLogger('django_crontab.crontab')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('/tmp/' + __name__ + '.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    r = requests.get('http://jaksafe.bpbd.jakarta.go.id/report/auto_report_json/' + time.strftime('%Y%m%d') + '/all')
    json = r.json()
    for report in json:
        rw = report['rw']
        created = report['tanggal']
        village = report['kelurahan_id']
        source = report['sumber']
        damage_infrastruktur = report['damage_infrastruktur']
        loss_infrastruktur = report['loss_infrastruktur']
        damage_lintas_sektor = report['damage_lintas_sektor']
        loss_lintas_sektor = report['loss_lintas_sektor']
        damage_produktif = report['damage_produktif']
        loss_produktif = report['loss_produktif']
        damage_sosial_perumahan = report['damage_sosial_perumahan']
        loss_sosial_perumahan = report['loss_sosial_perumahan']
        damage_total = report['damage_total']
        loss_total = report['loss_total']

        try:
            result = ReportAutoSummary.objects.get(created=report['tanggal'], village=report['kelurahan_id'])
        except ReportAutoSummary.DoesNotExist:
            report_auto_summary = ReportAutoSummary(
                rw=rw,
                created=created,
                village=Village.objects.get(id=village),
                source=source,
                damage_infrastruktur=damage_infrastruktur,
                loss_infrastruktur=loss_infrastruktur,
                damage_lintas_sektor=damage_lintas_sektor,
                loss_lintas_sektor=loss_lintas_sektor,
                damage_produktif=damage_produktif,
                loss_produktif=loss_produktif,
                damage_sosial_perumahan=damage_sosial_perumahan,
                loss_sosial_perumahan=loss_sosial_perumahan,
                damage_total=damage_total,
                loss_total=loss_total)
            report_auto_summary.save()
