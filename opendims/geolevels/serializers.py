from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Province, City, Subdistrict, Village, RW, RT


class ProvinceSerializer(gis_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = Province
        geo_field = 'polygon'
        fields = (
                'id',
                'name',
                'note',
                )


class CitySerializer(gis_serializers.GeoFeatureModelSerializer):
    province = serializers.SerializerMethodField()

    def get_province(self, obj):
        return obj.province.name

    class Meta:
        model = City
        geo_field = 'polygon'
        fields = (
                'id',
                'province',
                'name',
                'note',
                )


class SubdistrictSerializer(gis_serializers.GeoFeatureModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        return obj.city.name

    class Meta:
        model = Subdistrict
        geo_field = 'polygon'
        fields = (
                'id',
                'city',
                'name',
                'note',
                )


class VillageSerializer(gis_serializers.GeoFeatureModelSerializer):
    subdistrict = serializers.SerializerMethodField()

    def get_subdistrict(self, obj):
        return obj.subdistrict.name

    class Meta:
        model = Village
        geo_field = 'polygon'
        fields = (
                'id',
                'subdistrict',
                'name',
                'note',
                )


class RWSerializer(gis_serializers.GeoFeatureModelSerializer):
    village = serializers.SerializerMethodField()

    def get_village(self, obj):
        return obj.village.name

    class Meta:
        model = RW
        geo_field = 'polygon'
        fields = (
                'id',
                'village',
                'name',
                'note',
                )


class RTSerializer(gis_serializers.GeoFeatureModelSerializer):

    class Meta:
        model = RT
        geo_field = 'polygon'
        fields = (
                'id',
                'rw',
                'name',
                'note',
                )
