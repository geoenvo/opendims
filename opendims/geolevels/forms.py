from django import forms

from dal import autocomplete

from .models import Province, City, Subdistrict, Village, RW, RT


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'province': autocomplete.ModelSelect2(url='geolevels:autocomplete_province')
        }


class SubdistrictForm(forms.ModelForm):
    class Meta:
        model = Subdistrict
        fields = '__all__'
        widgets = {
            'city': autocomplete.ModelSelect2(url='geolevels:autocomplete_city')
        }


class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        widgets = {
            'subdistrict': autocomplete.ModelSelect2(url='geolevels:autocomplete_subdistrict')
        }


class RWForm(forms.ModelForm):
    class Meta:
        model = RW
        fields = '__all__'
        widgets = {
            'village': autocomplete.ModelSelect2(url='geolevels:autocomplete_village')
        }

class RTform(forms.ModelForm):
    class Meta:
        model = RT
        fields = '__all__'
        widgets = {
            'rw': autocomplete.ModelSelect2(url='geolevels:autocomplete_rw')
        }
