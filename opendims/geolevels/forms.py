from django.forms import ModelForm

from dal import autocomplete
from leaflet.forms.widgets import LeafletWidget

from .models import Province, City, Subdistrict, Village, RW, RT


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'province': autocomplete.ModelSelect2(url='geolevels:autocomplete_province')
        }


class SubdistrictForm(ModelForm):
    class Meta:
        model = Subdistrict
        fields = '__all__'
        widgets = {
            'city': autocomplete.ModelSelect2(url='geolevels:autocomplete_city')
        }


class VillageForm(ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        widgets = {
            'subdistrict': autocomplete.ModelSelect2(url='geolevels:autocomplete_subdistrict')
        }


class RWForm(ModelForm):
    class Meta:
        model = RW
        fields = '__all__'
        widgets = {
            'village': autocomplete.ModelSelect2(url='geolevels:autocomplete_village')
        }
