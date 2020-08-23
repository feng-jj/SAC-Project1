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
        map = MAP.objects.all()
        ov  = OV.objects.all()
        safeClinic = SAFE_Clinic.objects.all()
        everything = list(
            chain(clinical, advocacy, map, ov, safeClinic)
        )
        context["qs"] = everything
        user = None
        # todo: figure out how to display user name
        if self.request.user.is_authenticated:
            user = self.request.user
        context['user'] = user
        return context
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
