from django.contrib import admin
from .models import Clinical, Advocacy, MAP, OV, SAFE_Clinic, Crisis_Line, Prevention, Training, Development

# Register your models here.
myModels = [Clinical, Advocacy, MAP, OV, SAFE_Clinic, Prevention, Training, Development]
myModels += [Crisis_Line]
admin.site.register(myModels)