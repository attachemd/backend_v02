from rest_framework import generics

from core.models import FullCalendarModel
from full_calendar.api.serializers import FullCalendarSerializer


class FullCalendarView(
    generics.ListAPIView
):
    queryset = FullCalendarModel.objects.all()
    serializer_class = FullCalendarSerializer
