from django.db import models


class ExerciseModel(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField(default=5)
    calories = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class FinishedExerciseModel(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField(default=5)
    calories = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.name
