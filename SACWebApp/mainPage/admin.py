from django.contrib import admin
from .models import Clinical, Advocacy, MAP, OV, SAFE_Clinic, Crisis_Line

# Register your models here.
myModels = [Clinical, Advocacy, MAP, OV, SAFE_Clinic]
myModels += [Crisis_Line]
admin.site.register(myModels)