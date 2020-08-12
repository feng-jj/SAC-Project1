from django.urls import path
from . import views



urlpatterns = [
    path('', currentTeamView.as_view(), name='home-page'),
]
