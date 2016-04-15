from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django import forms

from dal import autocomplete

from .models import Event, EventImpact


class EventForm(forms.ModelForm):
    class Media:
        js = (
            'js/admin_event.js',
        )

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
            error_message = "Please select a Village."
            validation_errors['village'] = [_(error_message), ]
            error = True
        if rt and not rw:
            error_message = "Please select a RW."
            validation_errors['rw'] = [_(error_message), ]
            error = True
        if (rt and rw) and (rt.rw != rw):
            error_message = ("The selected RT does not exist in the selected "
                             "RW.")
            validation_errors['rt'] = [_(error_message), ]
            error = True
        if (rw and village) and (rw.village != village):
            error_message = ("The selected RW does not exist in the selected "
                             "Village.")
            validation_errors['rw'] = [_(error_message), ]
            error = True
        if (village and subdistrict) and (village.subdistrict != subdistrict):
            error_message = ("The selected Village does not exist in the "
                             "selected Subdistrict.")
            validation_errors['village'] = [_(error_message), ]
            error = True
        if (subdistrict and city) and (subdistrict.city != city):
            error_message = ("The selected Subdistrict does not exist in the "
                             "selected City.")
            validation_errors['subdistrict'] = [_(error_message), ]
            error = True
        if (city and province) and (city.province != province):
            error_message = ("The selected City does not exist in the "
                             "selected Province.")
            validation_errors['city'] = [_(error_message), ]
            error = True
        # Finally return error, if any
        if error:
            raise forms.ValidationError(validation_errors)
        return self.cleaned_data

    class Meta:
        model = Event
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


class EventImpactForm(forms.ModelForm):
    class Media:
        js = (
            'js/admin_event.js',
        )

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
            error_message = "Please select a Village."
            validation_errors['village'] = [_(error_message), ]
            error = True
        if rt and not rw:
            error_message = "Please select a RW."
            validation_errors['rw'] = [_(error_message), ]
            error = True
        if (rt and rw) and (rt.rw != rw):
            error_message = ("The selected RT does not exist in the selected "
                             "RW.")
            validation_errors['rt'] = [_(error_message), ]
            error = True
        if (rw and village) and (rw.village != village):
            error_message = ("The selected RW does not exist in the selected "
                             "Village.")
            validation_errors['rw'] = [_(error_message), ]
            error = True
        if (village and subdistrict) and (village.subdistrict != subdistrict):
            error_message = ("The selected Village does not exist in the "
                             "selected Subdistrict.")
            validation_errors['village'] = [_(error_message), ]
            error = True
        if (subdistrict and city) and (subdistrict.city != city):
            error_message = ("The selected Subdistrict does not exist in the "
                             "selected City.")
            validation_errors['subdistrict'] = [_(error_message), ]
            error = True
        if (city and province) and (city.province != province):
            error_message = ("The selected City does not exist in the "
                             "selected Province.")
            validation_errors['city'] = [_(error_message), ]
            error = True
        # Finally return error, if any
        if error:
            raise forms.ValidationError(validation_errors)
        return self.cleaned_data

    class Meta:
        model = EventImpact
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
