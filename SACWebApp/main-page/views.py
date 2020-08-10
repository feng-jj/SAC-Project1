from django.shortcuts import render
from django.http import HttpResponse
from .models import AdvocacyForm
# Create your views here.


def home(request) :
    return render(request, 'main-page/index.html')

def get_name(request) :
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AdvocacyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AdvocacyForm()

    return render(request, 'advocacy_form.html', {'form': form})