from django.urls import path

from exercise.api import views

urlpatterns = [
    path(
        'exercises/',
        views.ExerciseView.as_view(),
        name='exercise_list'
    ),
    path(
        'fexercises/',
        views.FinishedExerciseView.as_view(),
        name='finished_exercise_list'
    ),
]
