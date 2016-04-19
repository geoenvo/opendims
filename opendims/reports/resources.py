from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from import_export import resources, fields, widgets

from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from .models import Disaster, Event


class EventResource(resources.ModelResource):
    province = fields.Field(
        column_name='province',
        attribute='province',
        widget=widgets.ForeignKeyWidget(Province, 'name')
    )
    city = fields.Field(
        column_name='city',
        attribute='city',
        widget=widgets.ForeignKeyWidget(City, 'name')
    )
    subdistrict = fields.Field(
        column_name='subdistrict',
        attribute='subdistrict',
        widget=widgets.ForeignKeyWidget(Subdistrict, 'name')
    )
    village = fields.Field(
        column_name='village',
        attribute='village',
        widget=widgets.ForeignKeyWidget(Village, 'name')
    )
    rw = fields.Field(
        column_name='rw',
        attribute='rw',
        widget=widgets.ForeignKeyWidget(RW, 'name')
    )
    rt = fields.Field(
        column_name='rt',
        attribute='rt',
        widget=widgets.ForeignKeyWidget(RT, 'name')
    )

    def before_import(self, dataset, dry_run, **kwargs):
        """Overrides Django-Import-Export method.
        It is necessary to modify the tablib dataset before the real import
        process, to translate from a human friendly input format like this:
        id|disaster|province|city|subdistrict|village|rw |rt|height
        --|--------|--------|----|-----------|-------|---|--|
          |BJR     |        |    |           |ANCOL  |005|  |
          |BJR     |        |    |           |ANCOL  |001|  |
        then in order to match the Event model definition, query the Village-RW
        and RW-RT relation to produce to this:
        id|disaster|province|city|subdistrict|village|rw              |rt|height
        --|--------|--------|----|-----------|-------|----------------|--|
          |BJR     |        |    |           |ANCOL  |3175020003005000|  |
          |BJR     |        |    |           |ANCOL  |3175020003001000|  |
        Also checks whether the row's Geolevels relation is valid, if not
        the row is not imported.
        """
        # print 'DEBUG BEFORE'
        # print dataset

        # Get request object for sending error messages
        request = kwargs.pop('request', None)
        i = 0
        row_count = i + 2
        last = dataset.height - 1
        while i <= last:
            # Get the top row
            row = dataset[0]
            """
            Get the row contents, by default named Geolevels are uppercase
            in the database
            """
            id = row[0]
            disaster = row[1].upper()
            province = row[2].upper()
            city = row[3].upper()
            subdistrict = row[4].upper()
            village = row[5].upper()
            rw = row[6]
            rt = row[7]
            # Pad single digit RT/RW with zeros
            if rw and len(rw) < 3:
                diff = 3 - len(rw)
                for i in range(diff):
                    rw = '0' + rw
            if rt and len(rt) < 3:
                diff = 3 - len(rt)
                for i in range(diff):
                    rt = '0' + rt
            height = row[8]
            # Validate Geolevels relations
            valid_geolevels = True
            if rw and not village:
                valid_geolevels = False
            if rt and not rw:
                valid_geolevels = False
            if disaster and valid_geolevels:
                try:
                    Disaster.objects.get(pk=disaster)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Invalid disaster code. Skipping this row for import.')))
            if province and valid_geolevels:
                try:
                    province_instance = Province.objects.get(name=province)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Province not found. Skipping this row for import.')))
            if city and valid_geolevels:
                try:
                    city_instance = City.objects.get(name=city)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('City not found. Skipping this row for import.')))
            if subdistrict and valid_geolevels:
                try:
                    subdistrict_instance = Subdistrict.objects.get(
                        name=subdistrict)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Subdistrict not found. Skipping this row for import.')))
            if village and valid_geolevels:
                try:
                    village_instance = Village.objects.get(name=village)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Village not found. Skipping this row for import.')))
            if city_instance and province_instance and valid_geolevels:
                try:
                    City.objects.get(
                        name=city_instance.name,
                        province__name=province_instance.name
                    )
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('City not found in the province. Skipping this row for import.')))
            if subdistrict_instance and city_instance and valid_geolevels:
                try:
                    Subdistrict.objects.get(
                        name=subdistrict_instance.name,
                        city__name=city_instance.name
                    )
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Subdistrict not found in the city. Skipping this row for import.')))
            if village_instance and subdistrict_instance and valid_geolevels:
                try:
                    Village.objects.get(
                        name=village_instance.name,
                        subdistrict__name=subdistrict_instance.name
                    )
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Village not found in the subdistrict. Skipping this row for import.')))
            if rw and village_instance and valid_geolevels:
                try:
                    rw_instance = RW.objects.get(
                        name=rw,
                        village__name=village_instance.name
                    )
                    rw = unicode(rw_instance.pk)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('RW not found in the village. Skipping this row for import.')))
            if rt and rw and valid_geolevels:
                try:
                    rt_instance = RT.objects.get(name=rt, rw=rw_instance)
                    rt = unicode(rt_instance.pk)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('RT not found. Skipping this row for import.')))
            new_row = (
                id,
                disaster,
                province,
                city,
                subdistrict,
                village,
                rw,
                rt,
                height
            )
            """
            If relations are invalid don't push row to the dataset so it
            doesn't get imported
            """
            if valid_geolevels:
                dataset.rpush(new_row)
            dataset.lpop()
            i = i + 1
            row_count = i + 2
        # print 'DEBUG AFTER'
        # print dataset
        for field in self.get_fields():
            # print field.attribute, field.column_name, field.widget
            """
            Since the dataset now contains the PK of RW/RT, update the
            ForeignKeyWidget to query for PK instead of name column.
            """
            if field.attribute == 'rw' or field.attribute == 'rt':
                # print field.widget.model, field.widget.field
                # print field.widget.field
                field.widget.field = 'pk'

    class Meta:
        model = Event
        fields = (
            'id',
            'disaster',
            'province',
            'city',
            'subdistrict',
            'village',
            'rw',
            'rt',
            'height'
        )
        export_order = fields
