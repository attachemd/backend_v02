from rest_framework import serializers

from core.models import ExerciseModel, FinishedExerciseModel


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = '__all__'


class FinishedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedExerciseModel
        fields = '__all__'
