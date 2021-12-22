from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from backend_v02 import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class ExerciseModel(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField(default=5)
    calories = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class FinishedExerciseModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    name = models.ForeignKey(
        ExerciseModel,
        on_delete=models.CASCADE,
        related_name='finished_exercise'
    )

    # name = models.CharField(max_length=30)
    duration = models.IntegerField(default=5)
    calories = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=30)

    def __str__(self):
        # return "FinishedExerciseModel"
        return str(self.name)


class FullCalendarModel(models.Model):
    title = models.CharField(max_length=30)
    start = models.CharField(max_length=30)

    def __str__(self):
        return self.title
