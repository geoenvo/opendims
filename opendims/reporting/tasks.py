import datetime

from django.utils import timezone
from django.template.loader import get_template
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.db.models import Sum


from xhtml2pdf import pisa
from PyPDF2 import PdfFileReader, PdfFileMerger
from django_rq import job

from reports.models import Event
from weatherforecast.models import WeatherForecastReport
from waterlevel.models import WaterLevelReport
from reporting.models import Attachment, Report


@job
def generate_pdf_report(reporting_id):
    obj = Report.objects.get(pk=reporting_id)
    pdf_files = []
    pdf_files.append(obj.file)

    try:
        template = get_template('reporting/waterlevel.html')
        waterlevels = WaterLevelReport.objects.all()
        if obj.start and not obj.end:
            start = datetime.date(
                obj.start.year,
                obj.start.month,
                obj.start.day
            )
            waterlevels = waterlevels.filter(created__date=start)

        if obj.start and obj.end:
            waterlevels = waterlevels.filter(
                created__range=(obj.start, obj.end)
            )
        html = template.render({'waterlevels': waterlevels})

        pdf_waterlevels_temp = NamedTemporaryFile()

        pisa.CreatePDF(
            html.encode('utf-8'),
            dest=pdf_waterlevels_temp,
            encoding='utf-8'
        )
        attachment_created = timezone.localtime(timezone.now())
        pdf_waterlevels_filename = "{}__{}{}".format(
            attachment_created.strftime('%Y%m%d-%H%M'),
            'waterlevel',
            '.pdf'
        )
        attachment = Attachment()
        attachment.report = obj
        attachment.created = attachment_created
        attachment.file.save(
            pdf_waterlevels_filename,
            File(pdf_waterlevels_temp),
            save=False
        )
        attachment.save()
        pdf_files.append(attachment.file)
    except:
        pass

    try:
        template = get_template('reporting/weather_forecast.html')
        weatherforecasts = WeatherForecastReport.objects.all()
        if obj.start and not obj.end:
            start = datetime.date(
                obj.start.year,
                obj.start.month,
                obj.start.day
            )
            weatherforecasts = weatherforecasts.filter(created__date=start)

        if obj.start and obj.end:
            weatherforecasts = weatherforecasts.filter(
                created__range=(obj.start, obj.end)
            )

        html = template.render({'weatherforecasts': weatherforecasts})
        pdf_weather_temp = NamedTemporaryFile()
        pisa.CreatePDF(
            html.encode('utf-8'),
            dest=pdf_weather_temp,
            encoding='utf-8'
        )
        attachment_created = timezone.localtime(timezone.now())
        pdf_weather_filename = "{}__{}{}".format(
            attachment_created.strftime('%Y%m%d-%H%M'),
            'weatherforecasts',
            '.pdf'
        )
        attachment = Attachment()
        attachment.report = obj
        attachment.created = attachment_created
        attachment.file.save(
            pdf_weather_filename,
            File(pdf_weather_temp),
            save=False
        )
        attachment.save()
        pdf_files.append(attachment.file)
    except:
        pass

    try:
        template = get_template('reporting/statistics.html')
        statistics = Event.objects.filter(
            eventimpacts__isnull=False,
        ).distinct()

        statistics = statistics.annotate(
            evac_total=Sum('eventimpacts__evac_total'),
            affected_total=Sum('eventimpacts__affected_total'),
            affected_injury=Sum('eventimpacts__affected_injury'),
            affected_death=Sum('eventimpacts__affected_death'),
            loss_total=Sum('eventimpacts__loss_total')
        )

        if obj.start and not obj.end:
            start = datetime.date(
                obj.start.year,
                obj.start.month,
                obj.start.day
            )
            statistics = statistics.filter(created__date=start)

        if obj.start and obj.end:
            statistics = statistics.filter(
                created__range=(obj.start, obj.end)
            )
        html = template.render({'statistics': statistics})

        pdf_statistics_temp = NamedTemporaryFile()

        pisa.CreatePDF(
            html.encode('utf-8'),
            dest=pdf_statistics_temp,
            encoding='utf-8'
        )
        attachment_created = timezone.localtime(timezone.now())
        pdf_statistics_filename = "{}__{}{}".format(
            attachment_created.strftime('%Y%m%d-%H%M'),
            'statistics',
            '.pdf'
        )
        attachment = Attachment()
        attachment.report = obj
        attachment.created = attachment_created
        attachment.file.save(
            pdf_statistics_filename,
            File(pdf_statistics_temp),
            save=False
        )
        attachment.save()
        pdf_files.append(attachment.file)
    except:
        pass

    for disaster in obj.template.disaster_attached.all():
        try:
            template = get_template('reporting/report_' + disaster.code + '.html')
            events = Event.objects.filter(disaster__code=disaster.code)
            if obj.start and not obj.end:
                start = datetime.date(
                    obj.start.year,
                    obj.start.month,
                    obj.start.day
                )
                events = events.filter(created__date=start)

            if obj.start and obj.end:
                events = events.filter(
                    created__range=(obj.start, obj.end)
                )
            html = template.render({'events': events})
            pdf_disaster_temp = NamedTemporaryFile()

            pisa.CreatePDF(
                html.encode('utf-8'),
                dest=pdf_disaster_temp,
                encoding='utf-8'
            )
            attachment_created = timezone.localtime(timezone.now())
            pdf_disaster_filename = "{}__{}{}".format(
                attachment_created.strftime('%Y%m%d-%H%M'),
                disaster.code,
                '.pdf'
            )
            attachment = Attachment()
            attachment.report = obj
            attachment.created = attachment_created
            attachment.file.save(
                pdf_disaster_filename,
                File(pdf_disaster_temp),
                save=False
            )
            attachment.save()
            pdf_files.append(attachment.file)
        except:
            pass

    merger = PdfFileMerger()

    # loop through pdf_files to get pdf_file and append it
    for pdf_file in pdf_files:
        merger.append(PdfFileReader(pdf_file))

    pdf_join_temp = NamedTemporaryFile()
    merger.write(pdf_join_temp)

    attachment_created = timezone.localtime(timezone.now())
    pdf_join_filename = "{}__{}{}".format(
        attachment_created.strftime('%Y%m%d-%H%M'),
        'DAILY_REPORT',
        '.pdf'
    )
    attachment = Attachment()
    attachment.report = obj
    attachment.created = attachment_created
    attachment.file.save(
        pdf_join_filename,
        File(pdf_join_temp),
        save=False
    )
    attachment.save()
