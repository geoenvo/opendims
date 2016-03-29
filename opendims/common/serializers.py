from rest_framework import serializers
from django.utils import timezone


class DateTimeFieldTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldTZ, self).to_representation(value)
