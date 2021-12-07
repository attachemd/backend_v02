from django.contrib import admin

from core.models import ExerciseModel, FinishedExerciseModel

admin.site.register(ExerciseModel)
admin.site.register(FinishedExerciseModel)
