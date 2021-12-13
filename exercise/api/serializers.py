from rest_framework import serializers

from core.models import ExerciseModel, FinishedExerciseModel


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseModel
        fields = '__all__'


class FinishedExerciseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FinishedExerciseModel
        # exclude = ('exercise',)
        fields = '__all__'
