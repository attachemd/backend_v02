from rest_framework import serializers

from core.models import ExerciseModel


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = '__all__'
