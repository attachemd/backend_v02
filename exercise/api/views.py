from rest_framework import viewsets, generics

from core.models import ExerciseModel
from exercise.api.serializers import ExerciseSerializer


# class ExerciseView(viewsets.ModelViewSet):
#     queryset = ExerciseModel.objects.all()
#     serializer_class = ExerciseSerializer


class ExerciseView(
    generics.ListAPIView
):
    queryset = ExerciseModel.objects.all()
    serializer_class = ExerciseSerializer
