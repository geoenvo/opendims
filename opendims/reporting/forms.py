from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django import forms

from .models import Report


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

        """
        If replace_report_content is checked, override the report content with the
        template content. If not then just output the saved report content.
        """
        if replace_report_content:
            report_content = template.content
            if date:
                report_content = report_content.replace('[[date]]', date.strftime('%-d %B %Y'))

            if text_id:
                report_content = report_content.replace('[[id]]', text_id)
            if text_title:
                report_content = report_content.replace('[[title]]', text_title)
            if text_author:
                report_content = report_content.replace('[[author]]', text_author)
            self.cleaned_data['content'] = report_content

        return self.cleaned_data
