from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('advocacy-team-form/', views.get_name, name = 'advocacy-team-form'),
]
