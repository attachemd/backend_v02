from rest_framework import viewsets, generics

from core.models import ExerciseModel, FinishedExerciseModel
from exercise.api.serializers import ExerciseSerializer, FinishedExerciseSerializer


# class ExerciseView(viewsets.ModelViewSet):
#     queryset = ExerciseModel.objects.all()
#     serializer_class = ExerciseSerializer


class ExerciseView(
    generics.ListAPIView
):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer


class FinishedExerciseView(
    generics.ListCreateAPIView
):
    queryset = FinishedExerciseModel.objects.all()
    serializer_class = FinishedExerciseSerializer
