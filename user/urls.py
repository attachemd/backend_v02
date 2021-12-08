from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    # path('create/', views.CreateUserView.as_view(), name='create'),
    path('create/', views.registration_view, name='create'),
    path('access/', views.MyTokenObtainPairView.as_view(), name='access'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
