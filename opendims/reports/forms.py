from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django import forms

from dal import autocomplete

from geolevels.models import RW, RT
from .models import Event


class EventForm(forms.ModelForm):
    def clean(self):
        """Method for validating the EventForm.
        
        Verify that the selected Geolevels relations are valid.
        """
        province = self.cleaned_data.get('province', None)
        city = self.cleaned_data.get('city', None)
        subdistrict = self.cleaned_data.get('subdistrict', None)
        village = self.cleaned_data.get('village', None)
        rw = self.cleaned_data.get('rw', None)
        rt = self.cleaned_data.get('rt', None)
        validation_errors = {} # For holding attribute validation error messages
        error = False
        # Check whether the selected Geolevels have valid relations
        if rw and not village:
            validation_errors['village'] = [_("Please select a Village."),]
            error = True
        if rt and not rw:
            validation_errors['rw'] = [_("Please select a RW."),]
            error = True
        if (rt and rw) and rt.rw != rw:
            validation_errors['rt'] = [_("The selected RT does not exist in the selected RW."),]
            error = True
        if (rw and village) and rw.village != village:
            validation_errors['rw'] = [_("The selected RW does not exist in the selected Village."),]
            error = True
        if (village and subdistrict) and village.subdistrict != subdistrict:
            validation_errors['village'] = [_("The selected Vilage does not exist in the selected Subdistrict."),]
            error = True
        if (subdistrict and city) and subdistrict.city != city:
            validation_errors['subdistrict'] = [_("The selected Subdistrict does not exist in the selected City."),]
            error = True
        if (city and province) and city.province != province:
            validation_errors['city'] = [_("The selected City does not exist in the selected Province."),]
            error = True
        # Finally return error, if any
        if error:
            raise forms.ValidationError(validation_errors)
        return self.cleaned_data
    
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'city': autocomplete.ModelSelect2(url='geolevels:autocomplete_city', forward=['province']),
            'subdistrict': autocomplete.ModelSelect2(url='geolevels:autocomplete_subdistrict', forward=['city']),
            'village': autocomplete.ModelSelect2(url='geolevels:autocomplete_village', forward=['subdistrict']),
            'rw': autocomplete.ModelSelect2(url='geolevels:autocomplete_rw', forward=['village']),
            'rt': autocomplete.ModelSelect2(url='geolevels:autocomplete_rt', forward=['rw']),
        }
