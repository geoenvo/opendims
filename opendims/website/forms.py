from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PostSearchForm(forms.Form):
    q = forms.CharField(label=_('Keyword'))

    def __init__(self, *args, **kwargs):
        super(PostSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'q',
            Submit('', _('Search')),
        )
