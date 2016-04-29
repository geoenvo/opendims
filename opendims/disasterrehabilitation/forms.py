from __future__ import unicode_literals

from dal import autocomplete

from reports.forms import CommonEventForm
from .models import Location


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
