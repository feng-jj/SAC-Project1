from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import TemplateView
from itertools import chain
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


'''
    Creating the view for the login / register page
'''

def login_form_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "login-form.html", context)

def register_form_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, "register-form.html", context)

'''
    Creating the view for the 5 teams w/ similar data
'''
class currentTeamView(TemplateView) :
    template_name = 'mainPage/index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        clinical = Clinical.objects.all()
        clinicalVoca = Clinical_VOCA.objects.all();
        clinicalTotal = list(chain(clinical, clinicalVoca))
        advocacy = Advocacy.objects.all()
        map_ = MAP.objects.all()
        ov  = OV.objects.all()
        safeClinic = SAFE_Clinic.objects.all()
        everything = list(
            chain(clinical, advocacy, map_, ov, safeClinic, clinicalVoca)
        )
        context["qs"] = everything
        context["safeClinic"] = safeClinic
        context["clinical"] = clinicalTotal
        context["advocacy"] = advocacy
        context["map_"] = map_
        context["ov"] = ov
        user = None
        # todo: figure out how to display user name
        if self.request.user.is_authenticated:
            user = self.request.user
        context['user'] = user
        return context

'''
    Safe Clinic Data
'''
class safeClinicTeamView(currentTeamView, TemplateView) :
    template_name = 'mainPage/safe_clinic.html'

'''
    Clinical Data
'''
class clinicalTeamView(currentTeamView, TemplateView) :
    template_name = 'mainPage/clinical.html'

'''
    Advocacy Data
'''
class advocacyTeamView(currentTeamView, TemplateView) :
    template_name = 'mainPage/advocacy.html'

'''
    MAP Data
'''
class mapTeamView(currentTeamView, TemplateView) :
    template_name = 'mainPage/map_link.html'

'''
    OV Data
'''
class ovTeamView(currentTeamView, TemplateView) :
    template_name = 'mainPage/ov_link.html'

'''
    Crisis Line Team View
'''
class crisisLineTeamView(TemplateView) :
    template_name = 'mainPage/crisis_line.html'

    def get_context_data(self,   **kwargs) :
        context = super().get_context_data(**kwargs)
        crisisline = Crisis_Line.objects.all()
        context['qs'] = crisisline
        return context

class preventionTeamView(TemplateView) :
    template_name = 'mainPage/prevention.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        prevention = Prevention.objects.all()
        context['prevention'] = prevention;
        return context


class trainingTeamView(TemplateView) :
    template_name = 'mainPage/training.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        training = training.objects.all()
        context['training'] = training;
        return context

class developmentTeamView(TemplateView) :
    template_name = 'mainPage/development.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        development = Development.objects.all()
        context['development'] = development;
        return context


def advocacy_form_view(request):
    context = {}
    form = AdvocacyForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "advocacy_form.html", context)

def clinical_form_view(request):
    context = {}
    form = ClinicalForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "clinical_form.html", context)

def clinical_voca_form_view(request):
    context = {}
    form = ClinicalVOCAForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "clinical_voca_form.html", context)

def map_form_view(request):
    context = {}
    form = MAPForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "map_form.html", context)

def ov_form_view(request):
    context = {}
    form = OVForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "ov_form.html", context)

def safe_clinic_form_view(request):
    context = {}
    form = AdvocacyForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "advocacy_form.html", context)

def crisis_line_form_view(request):
    context = {}
    form = CrisisLineForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "crisis_line_form.html", context)

def prevention_form_view(request):
    context = {}
    form = PreventionForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "prevention_form.html", context)

def training_form_view(request):
    context = {}
    form = TrainingForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "training_form.html", context)

def development_form_view(request):
    context = {}
    form = DevelopmentForm(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "development_form.html", context)
