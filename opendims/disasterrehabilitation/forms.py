from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django import forms

from dal import autocomplete

from .models import Location


class CommonLocationForm(forms.ModelForm):
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
        # For holding attribute validation error messages
        validation_errors = {}
        error = False
        # Check whether the selected Geolevels have valid relations
        if rw and not village:
            error_message = _("Please select a Village.")
            validation_errors['village'] = [error_message, ]
            error = True
        if rt and not rw:
            error_message = _("Please select a RW.")
            validation_errors['rw'] = [error_message, ]
            error = True
        if (rt and rw) and (rt.rw != rw):
            error_message = _("The selected RT is not found in the selected "
                              "RW.")
            validation_errors['rt'] = [error_message, ]
            error = True
        if (rw and village) and (rw.village != village):
            error_message = _("The selected RW is not found in the selected "
                              "village.")
            validation_errors['rw'] = [error_message, ]
            error = True
        if (village and subdistrict) and (village.subdistrict != subdistrict):
            error_message = _("The selected village is not found in the "
                              "selected subdistrict.")
            validation_errors['village'] = [error_message, ]
            error = True
        if (subdistrict and city) and (subdistrict.city != city):
            error_message = _("The selected subdistrict is not found in the "
                              "selected city.")
            validation_errors['subdistrict'] = [error_message, ]
            error = True
        if (city and province) and (city.province != province):
            error_message = _("The selected city is not found in the "
                              "selected province.")
            validation_errors['city'] = [error_message, ]
            error = True
        # Finally return error, if any
        if error:
            raise forms.ValidationError(validation_errors)
        return self.cleaned_data


class LocationForm(CommonLocationForm):
    class Media:
        js = (
            'reports/js/admin_event.js',
        )

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
