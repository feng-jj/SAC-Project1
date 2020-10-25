from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import TemplateView
from itertools import chain
# Create your views here.

'''
    Creating the view for the 5 teams w/ similar data
'''
class currentTeamView(TemplateView) :
    template_name = 'mainPage/index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        clinical = Clinical.objects.all()
        advocacy = Advocacy.objects.all()
        map_ = MAP.objects.all()
        ov  = OV.objects.all()
        safeClinic = SAFE_Clinic.objects.all()
        everything = list(
            chain(clinical, advocacy, map_, ov, safeClinic)
        )
        context["qs"] = everything
        context["safeClinic"] = safeClinic
        context["clinical"] = clinical
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

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        crisisline = Crisis_Line.objects.all()
        context['qs'] = crisisline
        return context

class preventionTeamView(TemplateView) :
    template_name = 'mainPage/prevention.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        return context


class trainingTeamView(TemplateView) :
    template_name = 'mainPage/training.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        return context

class developmentTeamView(TemplateView) :
    template_name = 'mainPage/development.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
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