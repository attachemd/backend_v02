from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import FinishedExerciseModel, ExerciseModel
from exercise.api.serializers import FinishedExerciseSerializer

FINISHED_EXERCISES_URL = reverse('exercise:finished_exercise_list')


def finished_exercises_url_pk(pk):
    return reverse('exercise:finished_exercise_create', kwargs={'pk': pk})


def sample_exercise():
    """Create a sample exercise"""
    return ExerciseModel.objects.create(
        name='exercise name',
        duration=10,
        calories=10
    )


class PublicFinishedExercisesApiTests(TestCase):
    """Test the publicly available finished exercises API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving finished exercises"""
        res = self.client.get(FINISHED_EXERCISES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateFinishedExercisesApiTests(TestCase):
    """Test the authorized user finished exercises API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'password'
        )
        token = RefreshToken.for_user(self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(token.access_token)
        )
        # self.client.force_authenticate(self.user)

    def test_retrieve_finished_exercises(self):
        """Test retrieving finished exercises"""
        FinishedExerciseModel.objects.create(
            user=self.user,
            name=sample_exercise(),
            # name='exercise name 01',
            duration=10,
            calories=10,
            state='cancelled'
        )
        FinishedExerciseModel.objects.create(
            user=self.user,
            name=sample_exercise(),
            # name='exercise name 02',
            duration=20,
            calories=20,
            state='completed'
        )

        res = self.client.get(FINISHED_EXERCISES_URL)

        finished_exercises = FinishedExerciseModel.objects.all().order_by('-name')
        serializer = FinishedExerciseSerializer(finished_exercises, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_finished_exercises_limited_to_user(self):
        """Test that finished exercises returned are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other@test.com',
            'testpass'
        )
        FinishedExerciseModel.objects.create(
            user=user2,
            name=sample_exercise(),
            # name='exercise name 01',
            duration=10,
            calories=10,
            state='cancelled'
        )
        finished_exercises = FinishedExerciseModel.objects.create(
            user=self.user,
            name=sample_exercise(),
            # name='exercise name 02',
            duration=20,
            calories=20,
            state='completed'
        )

        res = self.client.get(FINISHED_EXERCISES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], str(finished_exercises.name))

    def test_create_finished_exercises_successful(self):
        """Test creating a new finished exercises"""
        exercise = sample_exercise()
        payload = {
            'name': exercise,
            # 'name': 'exercise name 02',
            'duration': 20,
            'calories': 20,
            'state': 'completed'
        }

        res = self.client.post(
            finished_exercises_url_pk(exercise.pk),
            payload
        )

        exists = FinishedExerciseModel.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_create_finished_exercises_invalid(self):
        """Test creating a new finished_exercises with invalid payload"""
        exercise = sample_exercise()
        payload = {'state': ''}
        res = self.client.post(
            finished_exercises_url_pk(exercise.pk),
            payload
        )

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
