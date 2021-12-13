from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
    generics.ListAPIView
):
    queryset = FinishedExerciseModel.objects.all()
    serializer_class = FinishedExerciseSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = FinishedExerciseModel.objects.all()
        return queryset.filter(
            user=self.request.user
        ).order_by('-name')


class FinishedExerciseCreateView(
    generics.CreateAPIView
):
    # queryset = FinishedExerciseModel.objects.all()
    serializer_class = FinishedExerciseSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FinishedExerciseModel.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        exercise = ExerciseModel.objects.get(pk=pk)
        user = self.request.user
        serializer.save(user=user, name=exercise)
