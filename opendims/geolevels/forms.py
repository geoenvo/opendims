from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete

from .models import Province, City, Subdistrict, Village, RW, RT


class GeolevelsForm(forms.ModelForm):
    class Media:
        js = (
            'geolevels/js/admin_geolevels.js',
        )

    def clean_id(self):
        id = self.cleaned_data.get('id', None)
        min_id_length = 0
        error = False
        if isinstance(self, CityForm):
            min_id_length = 4
        elif isinstance(self, SubdistrictForm):
            min_id_length = 7
        elif isinstance(self, VillageForm):
            min_id_length = 10
        elif isinstance(self, RWForm):
            min_id_length = 13
        elif isinstance(self, RTForm):
            min_id_length = 16
        if len(str(id)) < min_id_length:
            error = True
        if error:
            error_message = _("ID digit length must be at least")
            raise forms.ValidationError("{}: {}".format(error_message, min_id_length))


class ProvinceForm(GeolevelsForm):
    class Meta:
        model = Province
        fields = '__all__'


class CityForm(GeolevelsForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'province': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_province'
            )
        }


class SubdistrictForm(GeolevelsForm):
    class Meta:
        model = Subdistrict
        fields = '__all__'
        widgets = {
            'city': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_city'
            )
        }


class VillageForm(GeolevelsForm):
    class Meta:
        model = Village
        fields = '__all__'
        widgets = {
            'subdistrict': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_subdistrict'
            )
        }


class RWForm(GeolevelsForm):
    class Meta:
        model = RW
        fields = '__all__'
        widgets = {
            'village': autocomplete.ModelSelect2(
                url='geolevels:autocomplete_village'
            )
        }


class RTForm(GeolevelsForm):
    class Meta:
        model = RT
        fields = '__all__'
        widgets = {
            'rw': autocomplete.ModelSelect2(url='geolevels:autocomplete_rw')
        }
