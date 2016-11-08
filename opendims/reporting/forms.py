from __future__ import unicode_literals
from django.utils.timezone import datetime, timedelta

from django.utils.translation import gettext_lazy as _
from django import forms
from django.utils import timezone
from django.template.loader import get_template

from common.middleware import get_current_user
from waterlevel.models import WaterLevelReport
from weatherforecast.models import WeatherForecastReport
from reporting.models import Attachment, Report


label_replace_report_content = _('Replace report content with template?')


class ReportForm(forms.ModelForm):
    replace_report_content = forms.BooleanField(
        initial=True,
        required=False,
        label=label_replace_report_content
    )

    class Meta:
        model = Report
        fields = '__all__'


    def clean(self): 
        # replace_report_content is a non model form field
        replace_report_content = self.cleaned_data.get('replace_report_content', None)

        template = self.cleaned_data.get('template', None)
        date = self.cleaned_data.get('date', None)
        text_id = self.cleaned_data.get('text_id', None)
        text_title = self.cleaned_data.get('text_title', None)
        text_author = self.cleaned_data.get('text_author', None)
        user = get_current_user()
        nik = user.last_name  # tell user to set last_name become NIK
        yesterday = date + timedelta(days=-1)

        # get water level table and weather forecast table
        start = self.cleaned_data.get('start', None)
        end = self.cleaned_data.get('end', None)
        try:
            waterlevel_template = get_template('reporting/waterlevel.html')
            waterlevels = WaterLevelReport.objects.all()
            if start and not end:
                waterlevels = waterlevels.filter(created__date=start)
            elif start and end:
                waterlevels = waterlevels.filter(created__range=(start, end))

            waterlevel_table = waterlevel_template.render({'waterlevels': waterlevels})
        except:
            pass

        try:
            weatherforecast_template = get_template('reporting/weather_forecast.html')
            weatherforecasts = WeatherForecastReport.objects.all()

            if start and not end:
                weatherforecasts = weatherforecasts.filter(created__date=start)
            elif start and end:
                weatherforecasts = weatherforecasts.filter(created__range=(start, end))

            weather_table = weatherforecast_template.render({'weatherforecasts': weatherforecasts})
        except:
            pass

        # all disaster is attached
        disasters = template.disaster_attached.all()

        """
        If replace_report_content is checked, override the report content with the
        template content. If not then just output the saved report content.
        """
        if replace_report_content:
            report_content = template.content
            if date:
                report_content = report_content.replace('[[date]]', date.strftime('%A %-d %B %Y'))
            if yesterday:
                report_content = report_content.replace('[[yesterday]]', yesterday.strftime('%A %-d %B %Y'))
            if text_id:
                report_content = report_content.replace('[[id]]', text_id)
            if text_title:
                report_content = report_content.replace('[[title]]', text_title)
            if user:
                report_content = report_content.replace('[[author]]', str(user))
            if text_author:
                report_content = report_content.replace('[[author]]', text_author)
            if nik:
                report_content = report_content.replace('[[NIK]]', nik)
            if waterlevel_table:
                report_content = report_content.replace('[[waterlevel_table]]', waterlevel_table)
            if weather_table:
                report_content = report_content.replace('[[weather_table]]', weather_table)
            for disaster in disasters:
                """cek if disaster in attached or not"""

                if 'BJR' in disaster.code:
                    report_content = report_content.replace('[[bjr_rob_place_holder]]', "Terlampir")

                if 'GMP' in disaster.code:
                    report_content = report_content.replace('[[gmp_place_holder]]', "Terlampir")

                if 'CEK' in disaster.code:
                    report_content = report_content.replace('[[cek_place_holder]]', "Terlampir")

                if 'PHT' in disaster.code:
                    report_content = report_content.replace('[[pht_place_holder]]', "Terlampir")

                if 'SOS' in disaster.code:
                    report_content = report_content.replace('[[sos_place_holder]]', "Terlampir")

                if 'LAI' in disaster.code:
                    report_content = report_content.replace('[[lai_place_holder]]', "Terlampir")

                if 'KBK' in disaster.code:
                    report_content = report_content.replace('[[kbk_place_holder]]', "Terlampir")

                if 'KLB' in disaster.code:
                    report_content = report_content.replace('[[klb_place_holder]]', "Terlampir")

            self.cleaned_data['content'] = report_content

        return self.cleaned_data
