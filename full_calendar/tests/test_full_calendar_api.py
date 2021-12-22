from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import FullCalendarModel
from full_calendar.api.serializers import FullCalendarSerializer

FULL_CALENDAR_URL = reverse('full_calendar:full_calendar')


class MoviesApiTests(TestCase):
    """Test the authorized user full calendar API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_exercises(self):
        """Test retrieving full calendar"""
        FullCalendarModel.objects.create(
            title="Event name 01",
            start="2021-12-07",
        )
        FullCalendarModel.objects.create(
            title="Event name 02",
            start="2021-11-07",
        )
        res = self.client.get(FULL_CALENDAR_URL)

        full_calendar = FullCalendarModel.objects.all()
        serializer = FullCalendarSerializer(full_calendar, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
