from django.urls import path
from .views import *

urlpatterns = [
    path('', currentTeamView.as_view(), name='home-page'),
    path('', crisisLineTeamView.as_view(), name='crisis_line'),
    path('', preventionTeamView.as_view(), name='prevention'),
    path('', trainingTeamView.as_view(), name='training'),
    path('', developmentTeamView.as_view(), name='development'),
]
