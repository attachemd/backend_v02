from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import ExerciseModel
from exercise.api.serializers import ExerciseSerializer

EXERCISES_URL = reverse('exercise:exercise_list')


class MoviesApiTests(TestCase):
    """Test the authorized user Exercises API"""

    def setUp(self):
        self.client = APIClient()
        self.valid_exercise = {
            'name': 'exercise name',
            'duration': 20,
            'calories': 20,
        }

        self.invalid_exercise = {
            'name': '',
        }

    def test_retrieve_exercises(self):
        """Test retrieving exercises"""
        ExerciseModel.objects.create(
            name='exercise name 01',
            duration=10,
            calories=10,
        )
        ExerciseModel.objects.create(
            name='exercise name 02',
            duration=20,
            calories=20,
        )
        res = self.client.get(EXERCISES_URL)

        exercise = ExerciseModel.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
