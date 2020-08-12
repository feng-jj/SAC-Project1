from django.shortcuts import render
from .models import Clinical
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


# def home(request) :
#     numberInd= Clinical.total_ind
#     dates = Clinical.entry_date
#     everything = Clinical.objects.all()[:5]
#     #numberInd = []
#     #dates = []
#     #for num in everything :
#         # if num == 'total_ind' :
#         #     numberInd.append(num)
#         # if num == 'entry_date' :
#             #dates.append(num)
#     context = {'numberInd' : numberInd, 'dates' : dates, 'everything' : everything}
#     return render(request, 'main-page/index.html', context)

class currentTeamView(TemplateView) :
    template_name = 'templates/main-page/index.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["qs"] = Clinical.objects.all()
        return context
