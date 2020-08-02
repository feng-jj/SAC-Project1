from django.contrib import admin
from .models import Clinical, Advocacy, MAP, OV, SAFE_Clinic, Crisis_Line, Prevention, Development, Training

# Register your models here.
myModels = [Clinical, Advocacy, MAP, OV, SAFE_Clinic]
myModels += [Crisis_Line]
myModels += [Prevention]
myModels += [Development, Training]
admin.site.register(myModels)