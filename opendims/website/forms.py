from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings

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


class SiteHeaderForm(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get('image', None)
        if image:
            from django.core.files.images import get_image_dimensions
            w, h = get_image_dimensions(image)
            if w > settings.MAX_WIDTH_SITEHEADER_IMAGE:
                raise forms.ValidationError("{}: {}{}".format(_('Maximum image width is'), settings.MAX_WIDTH_SITEHEADER_IMAGE, 'px'))
            if h > settings.MAX_HEIGHT_SITEHEADER_IMAGE:
                raise forms.ValidationError("{}: {}{}".format(_('Maximum image height is'), settings.MAX_HEIGHT_SITEHEADER_IMAGE, 'px'))
        return image
