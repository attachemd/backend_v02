from django.urls import path

from full_calendar.api import views

app_name = 'full_calendar'

urlpatterns = [
    path(
        'full_calendar/',
        views.FullCalendarView.as_view(),
        name='full_calendar'
    ),
]
