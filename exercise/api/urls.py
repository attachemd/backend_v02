from django.urls import path

from exercise.api import views

urlpatterns = [
    path(
        'exercises/',
        views.ExerciseView.as_view(),
        name='exercise_list'
    ),
]
