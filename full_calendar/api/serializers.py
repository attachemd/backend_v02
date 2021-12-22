from rest_framework import serializers

from core.models import FullCalendarModel


class FullCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullCalendarModel
        fields = '__all__'
