from django.contrib import admin
from .models import *

# Register your models here.
myModels = [Clinical, Clinical_VOCA, Advocacy, MAP, OV, SAFE_Clinic, Prevention, Training, Development]
myModels += [Crisis_Line]
admin.site.register(myModels)