from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

from reports.forms import CommonEventForm
from .models import Location
from geolevels.models import Province, City, Subdistrict, Village, RW, RT


class LocationForm(CommonEventForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'city': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_city',
                forward=['province']
            ),
            'subdistrict': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_subdistrict',
                forward=['city']
            ),
            'village': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_village',
                forward=['subdistrict']
            ),
            'rw': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_rw',
                forward=['village']
            ),
            'rt': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_rt',
                forward=['rw']
            ),
        }


verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class SearchByLocationForm(forms.Form):
    province = forms.ModelChoiceField(
        label=verbose_province,
        required=False,
        queryset=Province.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_province')
    )
    city = forms.ModelChoiceField(
        label=verbose_city,
        required=False,
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_city', forward=['province']),
    )
    subdistrict = forms.ModelChoiceField(
        label=verbose_subdistrict,
        required=False,
        queryset=Subdistrict.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_subdistrict', forward=['city']),
    )
    village = forms.ModelChoiceField(
        label=verbose_village,
        required=False,
        queryset=Village.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_village', forward=['subdistrict']),
    )
    rw = forms.ModelChoiceField(
        label=verbose_rw,
        required=False,
        queryset=RW.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rw', forward=['village']),
    )
    rt = forms.ModelChoiceField(
        label=verbose_rt,
        required=False,
        queryset=RT.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rt', forward=['rw']),
    )

    def __init__(self, *args, **kwargs):
        super(SearchByLocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(Div(
                    'province',
                    'city',
                    'subdistrict',
                    css_class='col-md-6'
                ),
                Div(
                    'village',
                    'rw',
                    'rt',
                    css_class='col-md-6'
                ),
                css_class='row'
            ),
            Div(Div(
                    Submit('', _('Search')),
                    css_class='col-md-12 text-right'
                ),
                css_class='row'
            )
        )
