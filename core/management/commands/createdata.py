import random

import faker.providers
from django.core.management import BaseCommand
from faker import Faker

from core.models import ExerciseModel, FinishedExerciseModel, User, FullCalendarModel

fakegen = Faker()

EXERCISES = [
    "Lunges",
    "Pushups",
    "Squats",
    "Standing overhead dumbbell presses",
    "Dumbbell rows",
    "Single-leg deadlifts",
    "Burpees",
    "Side planks",
    "Planks",
    "Glute bridge"
]


class Provider(faker.providers.BaseProvider):
    def exercise(self):
        return self.random_element(EXERCISES)


fakegen.add_provider(Provider)


def create_super_user():
    user = User.objects.create_superuser(
        email="attachemd@gmail.com",
        password="1234"
    )
    user.save()
    return user


def create_full_calendar():
    full_calendar = FullCalendarModel.objects.get_or_create(
        title="Event name",
        start="2021-12-07",
    )[0]


def populate_user(n=5):
    for _ in range(n):
        name = fakegen.name()
        first_name = name.split(' ')[0]
        last_name = ' '.join(name.split(' ')[-1:])
        username = first_name[0].lower() + last_name.lower().replace(' ', '')
        email = username + "@" + last_name.lower() + ".com"
        user = User.objects.create_user(email, password=username)
        user.name = username
        user.is_superuser = False
        user.is_staff = False
        user.save()


def populate(N=5):
    user = create_super_user()
    # test_exercise = ExerciseModel.objects.get_or_create(
    #     name='battache',
    #     duration=2,
    #     calories=4,
    # )[0]

    for _ in range(10):
        # create new movie entry
        exercise = ExerciseModel.objects.get_or_create(
            name=fakegen.unique.exercise(),
            duration=random.randint(1, 10),
            calories=random.randint(1, 100),
        )[0]

    state_list = ["completed", "cancelled"]

    for _ in range(40):
        # create new movie entry
        exercise_id = random.randint(1, 10)
        exercise = ExerciseModel.objects.filter(
            id=exercise_id
        )[0]
        finishedExercise = FinishedExerciseModel.objects.get_or_create(
            user=user,
            name=exercise,
            # name=fakegen.company(),
            duration=random.randint(1, 10),
            calories=random.randint(1, 100),
            state=random.choice(state_list)
        )[0]


class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        print('populating script')
        populate_user()
        populate(20)
        create_full_calendar()
        print('populating complete')
