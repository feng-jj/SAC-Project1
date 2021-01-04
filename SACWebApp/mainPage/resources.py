from import_export import resources
from .models import Clinical, Clinical_VOCA, Advocacy, MAP, OV, SAFE_Clinic, Crisis_Line, Prevention, Training, Development

class ClinicalResource(resources.ModelResource):
    class Meta:
        model = Clinical

class ClinicalVOCAResource(resources.ModelResource):
    class Meta:
        model = Clinical_VOCA

class AdvocacyResource(resources.ModelResource):
    class Meta:
        model = Advocacy

class MAPResource(resources.ModelResource):
    class Meta:
        model = MAP

class OVResource(resources.ModelResource):
    class Meta:
        model = OV

class SAFE_ClinicResource(resources.ModelResource):
    class Meta:
        model = SAFE_Clinic

class Crisis_LineResource(resources.ModelResource):
    class Meta:
        model = Crisis_Line

class PreventionResource(resources.ModelResource):
    class Meta:
        model = Prevention

class TrainingResource(resources.ModelResource):
    class Meta:
        model = Training

class DevelopmentResource(resources.ModelResource):
    class Meta:
        model = Development