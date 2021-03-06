from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from itertools import chain
from django.contrib.auth.forms import UserCreationForm
from tablib import Dataset

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

from .resources import *
from .helper import *
from datetime import date


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
    Creating the view for logout
'''
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/login')

'''
    Creating the view for the 5 teams w/ similar data
'''
class currentTeamView(TemplateView) :
    template_name = 'mainPage/index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        # database objects
        clinical = Clinical.objects.all()
        clinicalVoca = Clinical_VOCA.objects.all()
        clinicalTotal = list(chain(clinical, clinicalVoca))
        advocacy = Advocacy.objects.all()
        map_ = MAP.objects.all()
        ov = OV.objects.all()
        safeClinic = SAFE_Clinic.objects.all()
        # inputting Advocacy and Clinical team data
        # num  sessions
        clinicalS = numSP(clinical, "sessions")
        clinicalVocaS = numSP(clinicalVoca, "sessions")
        advocacyS = numSP(advocacy, "sessions")
        # num people new
        clinicalN = numSP(clinical, "new")
        clinicalVocaN = numSP(clinicalVoca, "new")
        advocacyN = numSP(advocacy, "new")
        # num people continue
        clinicalC = numSP(clinical, "continue")
        clinicalVocaC = numSP(clinicalVoca, "continue")
        advocacyC = numSP(advocacy, "continue")
        # inputting into the context
        context["clinicalS"] = clinicalS
        context["clinicalVocaS"] = clinicalVocaS
        context["advocacyS"] = advocacyS
        context["clinicalN"] = clinicalN
        context["clinicalVocaN"] = clinicalVocaN
        context["advocacyN"] = advocacyN
        context["clinicalC"] = clinicalC
        context["clinicalVocaC"] = clinicalVocaC
        context["advocacyC"] = advocacyC
        # SAFE clinic specific data
        context['safeClinic'] = getExam(safeClinic)
        # MAP and OV team data
        context['map_'] = getAcc(map_)
        context['ov'] = getOV(ov)
        #because we have that there will be two pie/doughnut charts, we have to ensure that they are properly
        #inputted as ages
        clinicalVocaAges = appendFieldAge(clinicalVoca)
        clinicalAges = appendFieldAge(clinical)
        advocacyAges = appendFieldAge(advocacy)
        safeClinicAges = appendFieldAge(safeClinic)
        mapAges = appendFieldAge(map_)
        ovAges = appendFieldAge(ov)
        context['clinicalAges'] = clinicalAges
        context['clinicalVocaAges'] = clinicalVocaAges
        context['advocacyAges'] = advocacyAges
        context['safeClinicAges'] = safeClinicAges
        context['mapAges'] = mapAges
        context['ovAges'] = ovAges
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
        how = appendHowSAC(crisisline)
        context['totalCalls'] = totalCall(crisisline)
        context['highCalls'] = highCall(crisisline)
        # context['numMinors'] = numMinors(crisisline)
        context['how'] = how
        return context

class preventionTeamView(TemplateView) :
    template_name = 'mainPage/prevention.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        prevention = Prevention.objects.all()
        overallNumTrainings = numTrainings(prevention)
        context['prevention'] = totalAtt(prevention);
        context['overallNumTrainings'] = overallNumTrainings
        return context

class trainingTeamView(TemplateView) :
    template_name = 'mainPage/training.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        training = Training.objects.all()
        overallNumTrainings = numTrainings(training)
        context['training'] = totalAtt(training);
        context['overallNumTrainings'] = overallNumTrainings
        return context

class developmentTeamView(TemplateView) :
    template_name = 'mainPage/development.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        development = Development.objects.all()
        dd = develop(development)
        context['development'] = development;
        context['recurringGiftAvg'] = dd[0]
        context['totalRaised'] = dd[1]
        context['percentGoal'] = dd[2]
        # line graph data
        context['donors'] = numDevelop(development, "donors")
        context['foundations'] = numDevelop(development, "foundations")
        context['gifts'] = numDevelop(development, "gifts")
        context['recurring'] = numDevelop(development, "recurring")
        return context

##################################################################################

def advocacy_form_view(request):
    if request.method == 'POST':
        form = AdvocacyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = AdvocacyForm()

    context = {
        'form': form
    }
    return render(request, "advocacy_form.html", context)

def clinical_form_view(request):
    if request.method == 'POST':
        form = ClinicalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = ClinicalForm()

    context = {
        'form': form
    }
    return render(request, "clinical_form.html", context)

def clinical_voca_form_view(request):
    if request.method == 'POST':
        form = ClinicalVOCAForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = ClinicalVOCAForm()

    context = {
        'form': form
    }
    return render(request, "clinical_voca_form.html", context)

def map_form_view(request):
    if request.method == 'POST':
        form = MAPForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = MAPForm()

    context = {
        'form': form
    }
    return render(request, "map_form.html", context)

def ov_form_view(request):
    if request.method == 'POST':
        form = OVForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = OVForm()

    context = {
        'form': form
    }
    return render(request, "ov_form.html", context)

def safe_clinic_form_view(request):
    if request.method == 'POST':
        form = SafeClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = SafeClinicForm()

    context = {
        'form': form
    }
    return render(request, "safe_clinic_form.html", context)

def crisis_line_form_view(request):
    if request.method == 'POST':
        form = CrisisLineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = CrisisLineForm()

    context = {
        'form': form
    }
    return render(request, "crisis_line_form.html", context)

def prevention_form_view(request):
    if request.method == 'POST':
        form = PreventionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = PreventionForm()

    context = {
        'form': form
    }
    return render(request, "prevention_form.html", context)

def training_form_view(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = TrainingForm()

    context = {
        'form': form
    }
    return render(request, "training_form.html", context)


def development_form_view(request):
    if request.method == 'POST':
        form = DevelopmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form-confirmation/')
    else:
        form = DevelopmentForm()

    context = {
        'form': form
    }
    return render(request, "development_form.html", context)

def clinical_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        clinical_resource = ClinicalResource()
        dataset = clinical_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="clincial_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="clinical_data.xls"'
            return response

    return render(request, 'clinical_export.html')

def advocacy_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        advocacy_resource = AdvocacyResource()
        dataset = advocacy_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="advocacy_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="advocacy_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="advocacy_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'advocacy_export.html')

def clinical_voca_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        clinical_voca_resource = ClinicalVOCAResource()
        dataset = clinical_voca_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_voca_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="clinical_voca_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="clinical_voca_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'clinical_voca_export.html')

def map_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        map_resource = MAPResource()
        dataset = map_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="map_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="map_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="map_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'map_export.html')

def ov_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        ov_resource = OVResource()
        dataset = ov_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="ov_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="ov_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="ov_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'ov_export.html')

def safe_clinic_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        safe_clinic_resource = SAFE_ClinicResource()
        dataset = safe_clinic_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="safe_clinic_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="safe_clinic_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="safe_clinic_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'safe_clinic_export.html')

def crisis_line_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        crisis_line_resource = Crisis_LineResource()
        dataset = crisis_line_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="crisis_line_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="crisis_line_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="crisis_line_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'crisis_line_export.html')

def prevention_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        prevention_resource = PreventionResource()
        dataset = prevention_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="prevention_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="prevention_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="prevention_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'prevention_export.html')

def training_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        training_resource = TrainingResource()
        dataset = training_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="training_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="training_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="training_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'training_export.html')

def development_export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        development_resource = DevelopmentResource()
        dataset = development_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="development_data_{}.csv"'.format(date.today())
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="development_data_{}.json"'.format(date.today())
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="development_data_{}.xls"'.format(date.today())
            return response

    return render(request, 'development_export.html')

def form_confirmation(request):
    return render(request, 'form_confirmation.html')
