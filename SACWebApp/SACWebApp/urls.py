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
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_form_view, name='login_form'),
    path('home/', include('mainPage.urls')),

    path('login/', login_form_view, name='login_form'),
    path('register/', register_form_view, name='register_form'),

    path('advocacy-team-form/', advocacy_form_view, name = 'advocacy_form'),
    path('clinical-team-form/', clinical_form_view, name = 'clinical_form'),
    path('clinical-voca-team-form/', clinical_voca_form_view, name = 'clinical_voca_form'),
    path('MAP-team-form/', map_form_view, name = 'map_form'),
    path('OV-team-form/', ov_form_view, name = 'ov_form'),
    path('SAFE-Clinic-team-form/', safe_clinic_form_view, name = 'safe_form'),
    path('Crisis-Line-team-form/', crisis_line_form_view, name = 'crisis_line_form'),
    path('prevention-team-form/', prevention_form_view, name = 'prevention_form'),
    path('training-team-form/', training_form_view, name = 'training_form'),
    path('development-team-form/', development_form_view, name = 'development_form'),

    path('safe_clinic/', safeClinicTeamView.as_view(), name='safe_clinic'),
    path('clinical/', clinicalTeamView.as_view(), name='clinical'),
    path('advocacy/', advocacyTeamView.as_view(), name='advocacy'),
    path('ov/', ovTeamView.as_view(), name='ov'),
    path('map/', mapTeamView.as_view(), name='map'),

    path('crisis_line/', crisisLineTeamView.as_view(), name='crisis_line'),
    path('prevention/', preventionTeamView.as_view(), name='prevention'),
    path('training/', trainingTeamView.as_view(), name='training'),
    path('development/', developmentTeamView.as_view(), name='development'),

    path('clinical-export/', clinical_export, name = 'clinical_export'),
    path('advocacy-export/', advocacy_export, name = 'advocacy_export'),
    path('clinical-voca-export/', clinical_voca_export, name = 'clinical_voca_export'),
    path('map-export/', map_export, name = 'map_export'),
    path('ov-export/', ov_export, name = 'ov_export'),
    path('safe-clinic-export/', safe_clinic_export, name = 'safe_clinic_export'),
    path('crisis-line-export/', crisis_line_export, name = 'crisis_line_export'),
    path('prevention-export/', prevention_export, name = 'prevention_export'),
    path('training-export/', training_export, name = 'training_export'),
    path('development-export/', development_export, name = 'development_export'),

    path('form-confirmation/', form_confirmation, name = 'form_confirmation'),

    path('logout/', logout_request, name="logout"),

    #reset password urls
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="mainPage/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="mainPage/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="mainPage/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="mainPage/password_reset_done.html"),
         name="password_reset_complete"),
]


urlpatterns += staticfiles_urlpatterns()

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
