from django.urls import path
from .views import *

urlpatterns = [
    path('', currentTeamView.as_view(), name='home-page'),
]
