"""SACWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mainPage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainPage.urls')),

    path('safe_clinic/', safeClinicTeamView.as_view(), name='safe_clinic'),
    path('clinical/', clinicalTeamView.as_view(), name='clinical'),
    path('advocacy/', advocacyTeamView.as_view(), name='advocacy'),
    path('ov/', ovTeamView.as_view(), name='ov'),
    path('map/', mapTeamView.as_view(), name='map'),

    path('crisis_line/', crisisLineTeamView.as_view(), name='crisis_line'),
    path('prevention/', preventionTeamView.as_view(), name='prevention'),
    path('training/', trainingTeamView.as_view(), name='training'),
    path('development/', developmentTeamView.as_view(), name='development'),
]


urlpatterns += staticfiles_urlpatterns()
