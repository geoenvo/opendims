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
    province_name = serializers.SerializerMethodField()

    def get_province_name(self, obj):
        return obj.province.name

    class Meta:
        model = City
        geo_field = 'polygon'
        fields = (
                'id',
                'province_name',
                'province',
                'name',
                'note',
                )


class SubdistrictSerializer(gis_serializers.GeoFeatureModelSerializer):
    city_name = serializers.SerializerMethodField()

    def get_city_name(self, obj):
        return obj.city.name

    class Meta:
        model = Subdistrict
        geo_field = 'polygon'
        fields = (
                'id',
                'city_name',
                'city',
                'name',
                'note',
                )


class VillageSerializer(gis_serializers.GeoFeatureModelSerializer):
    subdistrict_name = serializers.SerializerMethodField()

    def get_subdistrict_name(self, obj):
        return obj.subdistrict.name

    class Meta:
        model = Village
        geo_field = 'polygon'
        fields = (
                'id',
                'subdistrict_name',
                'subdistrict',
                'name',
                'note',
                )


class RWSerializer(gis_serializers.GeoFeatureModelSerializer):
    village_name = serializers.SerializerMethodField()

    def get_village_name(self, obj):
        return obj.village.name

    class Meta:
        model = RW
        geo_field = 'polygon'
        fields = (
                'id',
                'village_name',
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
