from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

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


class SearchByLocationForm(forms.Form):
    province = forms.ModelChoiceField(
        required=False,
        queryset=Province.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_province')
    )
    city = forms.ModelChoiceField(
        required=False,
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_city', forward=['province']),
    )
    subdistrict = forms.ModelChoiceField(
        required=False,
        queryset=Subdistrict.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_subdistrict', forward=['city']),
    )
    village = forms.ModelChoiceField(
        required=False,
        queryset=Village.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_village', forward=['subdistrict']),
    )
    rw = forms.ModelChoiceField(
        required=False,
        queryset=RW.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rw', forward=['village']),
    )
    rt = forms.ModelChoiceField(
        required=False,
        queryset=RT.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rt', forward=['rw']),
    )

    def __init__(self, *args, **kwargs):
        super(SearchByLocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'province',
            'city',
            'subdistrict',
            'village',
            'rw',
            'rt',
            Submit('', _('Search')),
        )
