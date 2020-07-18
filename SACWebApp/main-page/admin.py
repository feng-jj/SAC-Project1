from django.contrib import admin
from .models import Clinical, Advocacy, MAP, OV, SAFE_Clinic

# Register your models here.
myModels = [Clinical, Advocacy, MAP, OV, SAFE_Clinic]
admin.site.register(myModels)