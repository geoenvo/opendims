from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django import forms

from dal import autocomplete

from geolevels.models import RW, RT
from .models import Event


verbose_rw = _('RW')
verbose_rt = _('RT')


class EventForm(forms.ModelForm):
    rw = forms.ModelChoiceField(
        required=False,
        queryset=RW.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rw', forward=['village']),
        label=verbose_rw
    )
    
    rt = forms.ModelChoiceField(
        required=False,
        queryset=RT.objects.all(),
        widget=autocomplete.ModelSelect2(url='geolevels:autocomplete_rt', forward=['rw']),
        label=verbose_rt
    )
    
    def clean(self):
        """Method for validating the EventForm.
        
        Verify that the selected Geolevels are related and the CharField (RW + RT) attributes are valid.
        """
        # When editing, set RW and RT in cleaned_data to avoid IntegrityError
        if self.instance.rw:
            self.cleaned_data['rw'] = self.instance.rw
        if self.instance.rt:
            self.cleaned_data['rt'] = self.instance.rt
        province = self.cleaned_data.get('province', None)
        city = self.cleaned_data.get('city', None)
        subdistrict = self.cleaned_data.get('subdistrict', None)
        village = self.cleaned_data.get('village', None)
        rw = self.cleaned_data.get('rw', None)
        rt = self.cleaned_data.get('rt', None)
        # If RW or RT not set, set to empty string to avoid IntegrityError
        if not rw:
            self.cleaned_data['rw'] = ''
        if not rt:
            self.cleaned_data['rt'] = ''
        validation_errors = {} # For holding attribute validation error messages
        error = False
        # Since RW and RT are actually CharFields, query their proper instances first
        if isinstance(rw, basestring) and rw and village:
            rw = RW.objects.filter(name=rw, village=village).first()
        if isinstance(rt, basestring) and rt and rw:
            rt = RT.objects.filter(name=rt, rw=rw).first()
        # Check whether the selected Geolevels have valid relations
        if (rw or rt) and not village:
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
        }
