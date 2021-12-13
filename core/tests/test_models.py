from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_exercise():
    """Create a sample exercise"""
    return models.ExerciseModel.objects.create(
        name='exercise name',
        duration=10,
        calories=10
    )


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_exercise_str(self):
        """Test the exercise string representation"""
        exercise = models.ExerciseModel.objects.create(
            name='exercise name',
            duration=10,
            calories=10
        )
        self.assertEqual(str(exercise), exercise.name)

    def test_finished_exercise_str(self):
        """Test the finished exercise string representation"""
        finished_exercise = models.FinishedExerciseModel.objects.create(
            user=sample_user(),
            name=sample_exercise(),
            # name='exercise name',
            duration=10,
            calories=10,
            state='cancelled'
        )
        # self.assertEqual(str(finished_exercise), "FinishedExerciseModel")
        self.assertEqual(str(finished_exercise), str(finished_exercise.name))
