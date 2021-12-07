import random

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from core.models import ExerciseModel, FinishedExerciseModel

fakegen = Faker()


def create_super_user():
    user = User.objects.create_superuser(
        username="me",
        password="1234",
        email="me@example.com"
    )
    user.save()


def populate(N=5):
    test_exercise = ExerciseModel.objects.get_or_create(
        name='battache',
        duration=2,
        calories=4,
    )[0]

    for _ in range(20):
        # create new movie entry
        exercise = ExerciseModel.objects.get_or_create(
            name=fakegen.company(),
            duration=random.randint(5, 120),
            calories=random.randint(1, 140),
        )[0]

    state_list = ["completed", "cancelled"]

    for _ in range(40):
        # create new movie entry
        finishedExercise = FinishedExerciseModel.objects.get_or_create(
            name=fakegen.company(),
            duration=random.randint(5, 120),
            calories=random.randint(1, 140),
            state=random.choice(state_list)
        )[0]


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        print('populating script')
        create_super_user()
        populate(20)
        print('populating complete')
