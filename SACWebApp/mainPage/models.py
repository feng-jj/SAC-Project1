from django.db import models
from django.forms import ModelForm
from datetime import date

# abstract base class for clinical, advocacy, MAP, OV, and SAFE Clinic Teams
class CommonEntries(models.Model):
    entry_date = models.DateField(default = date.today)
    race_amerind = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - American Indian/Alaska Native", default = 0)
    race_asian = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Asian", default = 0)
    race_black = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Black/African American", default = 0)
    race_latinx = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Hispanic or Latino, Latina, and Latinx", default = 0)
    race_pacific = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Native Hawaiian and Other Pacific Islander", default = 0)
    race_white = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - White Non-Latino/Caucasian", default = 0)
    race_other = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Some Other Race", default = 0)
    race_multiple = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Multiple Races", default = 0)
    race_unreported = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Reported", default = 0)
    race_untracked = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Tracked", default = 0)
    gender_agender = models.PositiveIntegerField(verbose_name = "Gender Identity - Agender", default = 0)
    gender_man = models.PositiveIntegerField(verbose_name = "Gender Identity - Man", default = 0)
    gender_nonbin = models.PositiveIntegerField(verbose_name = "Gender Identity - Non-binary", default = 0)
    gender_woman = models.PositiveIntegerField(verbose_name = "Gender Identity - Woman", default = 0)
    gender_not_rep = models.PositiveIntegerField(verbose_name = "Gender Identity - Not Reported", default = 0)
    gender_other = models.PositiveIntegerField(verbose_name = "Gender Identity - Other", default = 0)
    gender_other_text = models.TextField(verbose_name = "Gender Identity - Other Text", default = "")
    sex_female = models.PositiveIntegerField(verbose_name = "Sex - Female", default = 0)
    sex_male = models.PositiveIntegerField(verbose_name = "Sex - Male", default = 0)
    sex_inter = models.PositiveIntegerField(verbose_name = "Sex - Intersex", default = 0)
    age_0_12 = models.PositiveIntegerField(verbose_name = "Age - 0-12", default = 0)
    age_13_17 = models.PositiveIntegerField(verbose_name = "Age - 13-17", default = 0)
    age_18_24 = models.PositiveIntegerField(verbose_name = "Age - 18-24", default = 0)
    age_25_59 = models.PositiveIntegerField(verbose_name = "Age - 25-59", default = 0)
    age_60_plus = models.PositiveIntegerField(verbose_name = "Age - 60 and older", default = 0)
    victim_adult_sa = models.PositiveIntegerField(verbose_name = "Victimization Types - Adult Sexual Assault", default = 0)
    victim_as_child = models.PositiveIntegerField(verbose_name = "Victimization Types - Adults Sexually Abused/Assaulted as Children", default = 0)
    victim_nonoff_caregiver = models.PositiveIntegerField(verbose_name = "Victimization Types - Non-offending Caregivers", default = 0)
    victim_child_porn = models.PositiveIntegerField(verbose_name = "Victimization Types - Child Pornography", default = 0)
    victim_child_sa = models.PositiveIntegerField(verbose_name = "Victimization Types - Child Sexual Abuse/Assault", default = 0)
    victim_human_traff = models.PositiveIntegerField(verbose_name = "Victimization Types - Human Sex Trafficking", default = 0)
    special_deaf = models.PositiveIntegerField(verbose_name = "Special Classification - Deaf/Hard of Hearing", default = 0)
    special_homeless = models.PositiveIntegerField(verbose_name = "Special Classification - Homeless", default = 0)
    special_immigrant = models.PositiveIntegerField(verbose_name = "Special Classification - Immigrants/Refugees/Asylum Seekers", default = 0)
    special_lgbtq = models.PositiveIntegerField(verbose_name = "Special Classification - LGBTQ", default = 0)
    special_non_monog = models.PositiveIntegerField(verbose_name = "Special Classification - Non-Monogamists", default = 0)
    special_sex_work = models.PositiveIntegerField(verbose_name = "Special Classification - Sex Work Professionals", default = 0)
    special_bdsm = models.PositiveIntegerField(verbose_name = "Special Classification - BDSM Practitioners", default = 0)
    special_vet = models.PositiveIntegerField(verbose_name = "Special Classification - Veterans", default = 0)
    special_disability = models.PositiveIntegerField(verbose_name = "Special Classification - Victims with Disabilities - Cognitive/Physical/Mental", default = 0)
    special_limited_eng = models.PositiveIntegerField(verbose_name = "Special Classification - Victims with Limited English Proficiency", default = 0)
    special_other = models.PositiveIntegerField(verbose_name = "Special Classification - Other", default = 0)
    special_other_text = models.TextField(verbose_name = "Special Classification - Other Text", default = "")
    special_deaf_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Deaf/Hard of Hearing", default = 0)
    special_homeless_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Homeless", default = 0)
    special_immigrant_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Immigrants/Refugees/Asylum Seekers", default = 0)
    special_lgbtq_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - LGBTQ", default = 0)
    special_non_monog_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Non-Monogamists", default = 0)
    special_sex_work_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Sex Work Professionals", default = 0)
    special_bdsm_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - BDSM Practitioners", default = 0)
    special_vet_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Veterans", default = 0)
    special_disability_sub= models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Victims with Disabilities - Cognitive/Physical/Mental", default = 0)
    special_limited_eng_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Victims with Limited English Proficiency", default = 0)
    special_other_sub = models.PositiveIntegerField(verbose_name = "Special Classification SUBSEQUENT VISIT - Other", default = 0)
    special_other_text_sub = models.TextField(verbose_name = "Special Classification SUBSEQUENT VISIT - Other Text", default = "")
    advocacy_med_forens = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Victim Advocacy/Accompaniment to Medical Forensic Exam", default = 0)
    advocacy_law_enforce = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Law Enforcement Interview Advocacy/Accompaniment", default = 0)
    advocacy_individ = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Individual Advocacy", default = 0)
    advocacy_immig_assist = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Immigration Assistance", default = 0)
    advocacy_intervention = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Intervention with Employer, Creditor, etc.", default = 0)
    aces_adults_0 = models.PositiveIntegerField(verbose_name = "ACES Scores Adults 0", default = 0)
    aces_adults_1 = models.PositiveIntegerField(verbose_name = "ACES Scores Adults 1", default = 0)
    aces_adults_2 = models.PositiveIntegerField(verbose_name = "ACES Scores Adults 2", default = 0)
    aces_adults_3 = models.PositiveIntegerField(verbose_name = "ACES Scores Adults 3", default = 0)
    aces_adults_4 = models.PositiveIntegerField(verbose_name = "ACES Scores Adults 4 or More", default = 0)
    aces_children_0 = models.PositiveIntegerField(verbose_name = "ACES Scores Children 0", default = 0)
    aces_children_1 = models.PositiveIntegerField(verbose_name = "ACES Scores Children 1", default = 0)
    aces_children_2 = models.PositiveIntegerField(verbose_name = "ACES Scores Children 2", default = 0)
    aces_children_3 = models.PositiveIntegerField(verbose_name = "ACES Scores Children 3", default = 0)
    aces_children_4 = models.PositiveIntegerField(verbose_name = "ACES Scores Children 4 or More", default = 0)


    class Meta:
        abstract = True

# child classes of CommonEntries
class Clinical(CommonEntries):
    total_new = models.PositiveIntegerField(verbose_name = "Total New Clients", default = 0)
    total_continue = models.PositiveIntegerField(verbose_name = "Total Continuing Clients", default = 0)
    total_sess = models.PositiveIntegerField(verbose_name = "Total Sessions", default = 0)
    referral_criminal = models.PositiveIntegerField(verbose_name = "Referred Information About Criminal Justice Process", default = 0)
    referral_victim_rights = models.PositiveIntegerField(verbose_name = "Referred Information About Victim Rights, How to Obtain Nofitications, etc.", default = 0)
    referral_other_victim = models.PositiveIntegerField(verbose_name = "Referred to Other Victim Service Programs", default = 0)
    referral_other_service = models.PositiveIntegerField(verbose_name = "Referred to Other Services, Supports, and Resources", default = 0)
    emotional_crisis_interv = models.PositiveIntegerField(verbose_name = "Crisis Intervention", default = 0)
    emotional_hotline_counseling = models.PositiveIntegerField(verbose_name = "Hotline/Crisis Line Counseling", default = 0)
    emotional_therapy_counseling = models.PositiveIntegerField(verbose_name = "Therapy/Individual Counseling", default = 0)
    notif_criminal_justice = models.PositiveIntegerField(verbose_name = "Notification of Criminal Justice Events", default = 0)
    victim_impact_assist = models.PositiveIntegerField(verbose_name = "Victim Impact Statement Assistance", default = 0)
    emergency_justice_assist = models.PositiveIntegerField(verbose_name = "Emergency Justice-related Assistance", default = 0)
    civil_legal_protection = models.PositiveIntegerField(verbose_name = "Civil legal attorney assistance in obtaining protection or restraining order", default = 0)
    civil_legal_family_law = models.PositiveIntegerField(verbose_name = "Civil Legal Attorney Assistance with Family Law Issues", default = 0)
    other_civil_legal = models.PositiveIntegerField(verbose_name = "Other Civil Legal Attorney Assistance", default = 0)
    immigration_attorney = models.PositiveIntegerField(verbose_name = "Immigration Attorney Assistance", default = 0)
    prosecution_interview_advocacy = models.PositiveIntegerField(verbose_name = "Prosecution Interview Advocacy/Accompaniment", default = 0)
    criminal_advocacy = models.PositiveIntegerField(verbose_name = "Criminal Advocacy/Accompaniment", default = 0)
    civil_advocacy = models.PositiveIntegerField(verbose_name = "Civil Advocacy/Accompaniment", default = 0)
    assist_complete_app = models.PositiveIntegerField(verbose_name = "Assistance Completing Application", default = 0)
    assist_appeal_compensation = models.PositiveIntegerField(verbose_name = "Assistance Appealing Compensation Award", default = 0)
    followup_outreach_to_all = models.PositiveIntegerField(verbose_name = "Followup Outreach to All Clients", default = 0)
    followup_outreach_to_current = models.PositiveIntegerField(verbose_name = "Followup Outreach to Current Monthly Clients ", default = 0)


    class Meta:
        verbose_name = "Clinical Team Entry"
        verbose_name_plural = "Clinical Team Entries"
    pass

class Clinical_VOCA(CommonEntries):
    total_new = models.PositiveIntegerField(verbose_name = "Total New Clients", default = 0)
    total_continue = models.PositiveIntegerField(verbose_name = "Total Continuing Clients", default = 0)
    total_sess = models.PositiveIntegerField(verbose_name = "Total Sessions", default = 0)
    referral_criminal = models.PositiveIntegerField(verbose_name = "Referred Information About Criminal Justice Process", default = 0)
    referral_victim_rights = models.PositiveIntegerField(verbose_name = "Referred Information About Victim Rights, How to Obtain Nofitications, etc.", default = 0)
    referral_other_victim = models.PositiveIntegerField(verbose_name = "Referred to Other Victim Service Programs", default = 0)
    referral_other_service = models.PositiveIntegerField(verbose_name = "Referred to Other Services, Supports, and Resources", default = 0)
    emotional_crisis_interv = models.PositiveIntegerField(verbose_name = "Crisis Intervention", default = 0)
    emotional_hotline_counseling = models.PositiveIntegerField(verbose_name = "Hotline/Crisis Line Counseling", default = 0)
    emotional_therapy_counseling = models.PositiveIntegerField(verbose_name = "Therapy/Individual Counseling", default = 0)
    notif_criminal_justice = models.PositiveIntegerField(verbose_name = "Notification of Criminal Justice Events", default = 0)
    victim_impact_assist = models.PositiveIntegerField(verbose_name = "Victim Impact Statement Assistance", default = 0)
    emergency_justice_assist = models.PositiveIntegerField(verbose_name = "Emergency Justice-related Assistance", default = 0)
    civil_legal_protection = models.PositiveIntegerField(verbose_name = "Civil legal attorney assistance in obtaining protection or restraining order", default = 0)
    civil_legal_family_law = models.PositiveIntegerField(verbose_name = "Civil Legal Attorney Assistance with Family Law Issues", default = 0)
    other_civil_legal = models.PositiveIntegerField(verbose_name = "Other Civil Legal Attorney Assistance", default = 0)
    immigration_attorney = models.PositiveIntegerField(verbose_name = "Immigration Attorney Assistance", default = 0)
    prosecution_interview_advocacy = models.PositiveIntegerField(verbose_name = "Prosecution Interview Advocacy/Accompaniment", default = 0)
    criminal_advocacy = models.PositiveIntegerField(verbose_name = "Criminal Advocacy/Accompaniment", default = 0)
    civil_advocacy = models.PositiveIntegerField(verbose_name = "Civil Advocacy/Accompaniment", default = 0)
    assist_complete_app = models.PositiveIntegerField(verbose_name = "Assistance Completing Application", default = 0)
    assist_appeal_compensation = models.PositiveIntegerField(verbose_name = "Assistance Appealing Compensation Award", default = 0)
    followup_outreach_to_all = models.PositiveIntegerField(verbose_name = "Followup Outreach to All Clients", default = 0)
    followup_outreach_to_current = models.PositiveIntegerField(verbose_name = "Followup Outreach to Current Monthly Clients ", default = 0)


    class Meta:
        verbose_name = "Clinical VOCA Team Entry"
        verbose_name_plural = "Clinical VOCA Team Entries"
    pass

class Advocacy(CommonEntries):
    total_new = models.PositiveIntegerField(verbose_name = "Total New Clients", default = 0)
    total_continue = models.PositiveIntegerField(verbose_name = "Total Continuing Clients", default = 0)
    total_sess = models.PositiveIntegerField(verbose_name = "Total Sessions", default = 0)
    referral_criminal = models.PositiveIntegerField(verbose_name = "Referred Information About Criminal Justice Process", default = 0)
    referral_victim_rights = models.PositiveIntegerField(verbose_name = "Referred Information About Victim Rights, How to Obtain Nofitications, etc.", default = 0)
    referral_other_victim = models.PositiveIntegerField(verbose_name = "Referred to Other Victim Service Programs", default = 0)
    referral_other_service = models.PositiveIntegerField(verbose_name = "Referred to Other Services, Supports, and Resources", default = 0)
    emotional_crisis_interv = models.PositiveIntegerField(verbose_name = "Crisis Intervention", default = 0)
    emotional_hotline_counseling = models.PositiveIntegerField(verbose_name = "Hotline/Crisis Line Counseling", default = 0)
    emotional_therapy_counseling = models.PositiveIntegerField(verbose_name = "Therapy/Individual Counseling", default = 0)
    notif_criminal_justice = models.PositiveIntegerField(verbose_name = "Notification of Criminal Justice Events", default = 0)
    victim_impact_assist = models.PositiveIntegerField(verbose_name = "Victim Impact Statement Assistance", default = 0)
    emergency_justice_assist = models.PositiveIntegerField(verbose_name = "Emergency Justice-related Assistance", default = 0)
    civil_legal_protection = models.PositiveIntegerField(verbose_name = "Civil legal attorney assistance in obtaining protection or restraining order", default = 0)
    civil_legal_family_law = models.PositiveIntegerField(verbose_name = "Civil Legal Attorney Assistance with Family Law Issues", default = 0)
    other_civil_legal = models.PositiveIntegerField(verbose_name = "Other Civil Legal Attorney Assistance", default = 0)
    immigration_attorney = models.PositiveIntegerField(verbose_name = "Immigration Attorney Assistance", default = 0)
    prosecution_interview_advocacy = models.PositiveIntegerField(verbose_name = "Prosecution Interview Advocacy/Accompaniment", default = 0)
    criminal_advocacy = models.PositiveIntegerField(verbose_name = "Criminal Advocacy/Accompaniment", default = 0)
    civil_advocacy = models.PositiveIntegerField(verbose_name = "Civil Advocacy/Accompaniment", default = 0)
    assist_complete_app = models.PositiveIntegerField(verbose_name = "Assistance Completing Application", default = 0)
    assist_appeal_compensation = models.PositiveIntegerField(verbose_name = "Assistance Appealing Compensation Award", default = 0)
    followup_outreach_to_all = models.PositiveIntegerField(verbose_name = "Followup Outreach to All Clients", default = 0)
    followup_outreach_to_current = models.PositiveIntegerField(verbose_name = "Followup Outreach to Current Monthly Clients ", default = 0)

    class Meta:
        verbose_name = "Advocacy Team Entry"
        verbose_name_plural = "Advocacy Team Entries"
    pass

class MAP(CommonEntries):
    total_accompaniments = models.PositiveIntegerField(verbose_name = "Total Accompaniments", default = 0)
    class Meta:
        verbose_name = "MAP Team Entry"
        verbose_name_plural = "MAP Team Entries"
    pass

class OV(CommonEntries):
    total_OV = models.PositiveIntegerField(verbose_name = "Total OVs", default = 0)
    class Meta:
        verbose_name = "OV Team Entry"
        verbose_name_plural = "OV Team Entries"
    pass

class SAFE_Clinic(CommonEntries):
    total_exams = models.PositiveIntegerField(verbose_name = "Total Rape Exams", default = 0)
    class Meta:
        verbose_name = "SAFE Clinic Team Entry"
        verbose_name_plural = "SAFE Clinic Team Entries"
    pass

class ClinicalForm(ModelForm):
    class Meta:
        model = Clinical
        fields = '__all__'

class ClinicalVOCAForm(ModelForm):
    class Meta:
        model = Clinical_VOCA
        fields = '__all__'

class AdvocacyForm(ModelForm):
    class Meta:
        model = Advocacy
        fields = '__all__'

class MAPForm(ModelForm):
    class Meta:
        model = MAP
        fields = '__all__'

class OVForm(ModelForm):
    class Meta:
        model = OV
        fields = '__all__'



##################################################################################################

class Crisis_Line(models.Model):
    entry_date = models.DateField(default = date.today)
    total_calls = models.PositiveIntegerField(verbose_name = "Total Calls", default = 0)
    total_chats = models.PositiveIntegerField(verbose_name = "Total Chats", default = 0)
    highest_calls = models.PositiveIntegerField(verbose_name = "Highest # Calls in 1 Day", default = 0)
    avg_length = models.FloatField(verbose_name = "Average Length (Minutes)", default = 0)
    avg_wait = models.FloatField(verbose_name = "Average Wait Time (Minutes)", default = 0)
    reason_self_crisis = models.PositiveIntegerField(verbose_name = "Reason - Self in Crisis", default = 0)
    reason_triggered = models.PositiveIntegerField(verbose_name = "Reason - Triggered", default = 0)
    reason_support_other = models.PositiveIntegerField(verbose_name = "Reason - Support for Someone Else", default = 0)
    reason_concern_child = models.PositiveIntegerField(verbose_name = "Reason - Concerned for a Child", default = 0)
    reason_other = models.PositiveIntegerField(verbose_name = "Reason - Other", default = 0)
    reason_other_text = models.TextField(verbose_name = "Reason - Other Text", default = "")
    resource_advocacy = models.PositiveIntegerField(verbose_name = "Resource Referral - Advocacy Services", default = 0)
    resource_mental_health = models.PositiveIntegerField(verbose_name = "Resource Referral - Mental Health/Therapy", default = 0)
    resource_shelter = models.PositiveIntegerField(verbose_name = "Resource Referral - Shelter Services", default = 0)
    resource_social = models.PositiveIntegerField(verbose_name = "Resource Referral - Social Services", default = 0)
    resource_housing = models.PositiveIntegerField(verbose_name = "Resource Referral - Housing Resources", default = 0)
    resource_support_group = models.PositiveIntegerField(verbose_name = "Resource Referral - Support Group", default = 0)
    resource_legal = models.PositiveIntegerField(verbose_name = "Resource Referral - Legal Services", default = 0)
    resource_addiction = models.PositiveIntegerField(verbose_name = "Resource Referral - Addiction Services", default = 0)
    resource_bilingual = models.PositiveIntegerField(verbose_name = "Resource Referral - Bilingual Services", default = 0)
    resource_hospital = models.PositiveIntegerField(verbose_name = "Resource Referral - Hospital Services", default = 0)
    resource_survivor = models.PositiveIntegerField(verbose_name = "Resource Referral - Survivor Resources", default = 0)
    resource_food = models.PositiveIntegerField(verbose_name = "Resource Referral - Food Access", default = 0)
    resource_disability = models.PositiveIntegerField(verbose_name = "Resource Referral - Disability Resources", default = 0)
    resource_financial = models.PositiveIntegerField(verbose_name = "Resource Referral - Financial Resources", default = 0)
    resource_veteran = models.PositiveIntegerField(verbose_name = "Resource Referral - Veterans Resources", default = 0)
    resource_other = models.PositiveIntegerField(verbose_name = "Resource Referral - Other", default = 0)
    info_legal_def = models.PositiveIntegerField(verbose_name = "Information Referral - Legal Definitions", default = 0)
    info_police_codes = models.PositiveIntegerField(verbose_name = "Information Referral - Police Codes/Reporting Process", default = 0)
    info_healthy_relationship = models.PositiveIntegerField(verbose_name = "Information Referral - Healthy Relationships", default = 0)
    info_mandatory_report = models.PositiveIntegerField(verbose_name = "Information Referral - Mandatory Reporting Process", default = 0)
    info_workplace_harass = models.PositiveIntegerField(verbose_name = "Information Referral - Workplace Harassment", default = 0)
    info_stalking = models.PositiveIntegerField(verbose_name = "Information Referral - Stalking/Harassment", default = 0)
    info_mental_health = models.PositiveIntegerField(verbose_name = "Information Referral - General Mental Health", default = 0)
    info_survivor = models.PositiveIntegerField(verbose_name = "Information Referral - Survivor Support", default = 0)
    info_nop = models.PositiveIntegerField(verbose_name = "Information Referral - NoP Support", default = 0)
    info_contraceptives = models.PositiveIntegerField(verbose_name = "Information Referral - Access to Contraceptives", default = 0)
    info_teen_dating_violence = models.PositiveIntegerField(verbose_name = "Information Referral - Teen Dating Violence", default = 0)
    info_trauma_response = models.PositiveIntegerField(verbose_name = "Information Referral - Trauma Response/Impact", default = 0)
    info_firearm_safety = models.PositiveIntegerField(verbose_name = "Information Referral - Firearm Safety", default = 0)
    info_sex_ed = models.PositiveIntegerField(verbose_name = "Information Referral - Sex Education", default = 0)
    info_sac_info = models.PositiveIntegerField(verbose_name = "Information Referral - General SAC Info", default = 0)
    info_rape_crisis_info = models.PositiveIntegerField(verbose_name = "Information Referral -  General Rape Crisis Center Info", default = 0)
    gender_agender = models.PositiveIntegerField(verbose_name = "Gender Identity - Agender", default = 0)
    gender_man = models.PositiveIntegerField(verbose_name = "Gender Identity - Man", default = 0)
    gender_nonbin = models.PositiveIntegerField(verbose_name = "Gender Identity - Non-binary", default = 0)
    gender_woman = models.PositiveIntegerField(verbose_name = "Gender Identity - Woman", default = 0)
    gender_not_rep = models.PositiveIntegerField(verbose_name = "Gender Identity - Not Reported", default = 0)
    gender_other = models.PositiveIntegerField(verbose_name = "Gender Identity - Other", default = 0)
    gender_other_text = models.TextField(verbose_name = "Gender Identity - Other Text", default = "")
    race_amerind = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - American Indian/Alaska Native", default = 0)
    race_asian = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Asian", default = 0)
    race_black = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Black/African American", default = 0)
    race_latinx = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Hispanic or Latino, Latina, and Latinx", default = 0)
    race_pacific = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Native Hawaiian and Other Pacific Islander", default = 0)
    race_white = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - White Non-Latino/Caucasian", default = 0)
    race_other = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Some Other Race", default = 0)
    race_multiple = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Multiple Races", default = 0)
    race_unreported = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Reported", default = 0)
    race_untracked = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Tracked", default = 0)
    lang_english = models.PositiveIntegerField(verbose_name = "Preferred Language - English", default = 0)
    lang_spanish = models.PositiveIntegerField(verbose_name = "Preferred Language - Spanish", default = 0)
    lang_other = models.PositiveIntegerField(verbose_name = "Preferred Language - Other", default = 0)
    lang_other_text = models.TextField(verbose_name = "Preferred Language - Other Text", default = "")
    heard_TV = models.PositiveIntegerField(verbose_name = "Heard Through TV", default = 0)
    heard_radio = models.PositiveIntegerField(verbose_name = "Heard Through Radio", default = 0)
    heard_website = models.PositiveIntegerField(verbose_name = "Heard Through Website", default = 0)
    heard_social = models.PositiveIntegerField(verbose_name = "Heard Through Social Media", default = 0)
    heard_friend_fam = models.PositiveIntegerField(verbose_name = "Heard Through Friend or Family", default = 0)
    heard_medical = models.PositiveIntegerField(verbose_name = "Heard Through Medical Professional", default = 0)
    heard_other = models.PositiveIntegerField(verbose_name = "Heard Through Other Source", default = 0)
    heard_other_text = models.TextField(verbose_name = "Heard Through Other Source - Text", default = "")

    class Meta:
        verbose_name = "Crisis Line Team Entry"
        verbose_name_plural = "Crisis Line Team Entries"


class CrisisLineForm(ModelForm):
    class Meta:
        model = Crisis_Line
        fields = '__all__'

#####################################################################################################

class Prevention(models.Model):
    TYPE_ORG = [
        ('church', 'church'),
        ('college/university', 'college/university'),
        ('high school', 'high school'),
        ('elementary school', 'elementary school'),
        ('middle school', 'middle school'),
        ('non-profit', 'non-profit'),
        ('corporation', 'corporation'),
        ('bar/restaurant', 'bar/restaurant'),
        ('other', 'other'),
    ]

    TOPIC = [
        ('stewards of children', 'stewards of children'),
        ('safe bar', 'safe bar'),
        ('other', 'other'),
    ]

    entry_date = models.DateField(default = date.today)
    type_org = models.CharField(max_length = 30, verbose_name = "Type of Organization", blank = True, choices = TYPE_ORG)
    num_attendees = models.PositiveIntegerField(verbose_name = "Number of Attendees", default = 0)
    duration = models.PositiveIntegerField(verbose_name = "Training Duration", default = 0)
    topic = models.CharField(max_length = 30, verbose_name = "Topic of Training", blank = True, choices = TOPIC)
    topic_other = models.TextField(verbose_name = "Other Topic", default = "")

    class Meta:
        verbose_name = "Prevention Team Entry"
        verbose_name_plural = "Prevention Team Entries"

class PreventionForm(ModelForm):
    class Meta:
        model = Prevention
        fields = '__all__'


class Training(models.Model):
    OCCUPATION = [
        ('advocacy org staff', 'advocacy org staff'),
        ('attorneys/law students (not prosecutor)', 'attorneys/law students'),
        ('batterer intervention program staff', 'batterer intervention program staff'),
        ('corrections personnel', 'corrections personnel'),
        ('court personnel', 'court personnel'),
        ('disability org staff', 'disability org staff'),
        ('educators', 'educators'),
        ('elder org staff', 'elder org staff'),
        ('faith-based org staff', 'faith-based org staff'),
        ('government agency staff','gov agency staff'),
        ('health professionals', 'health professionals'),
        ('immigrant org staff', 'immigrant org staff'),
        ('law enforcement officers', 'law enforcement officers'),
        ('legal services staff (not attorney)', 'legal services staff'),
        ('mental health professionals', 'mpyental health professionals'),
        ('prosecutors', 'prosecutors'),
        ('sex offender treatment providers', 'sex offender treatment providers'),
        ('sexual assault nurse/forensic examiners', 'sexual assault nurse/forensic examiners'),
        ('social service org staff (non government)', 'social service org staff'),
        ('substance abuse org staff', 'substance abuse org staff'),
        ('supervised visitation and exchange center staff', 'supervised vistation and exchange center'),
        ('translators/interpreters', 'translators/interpreters'),
        ('tribal government/tribal government agency staff', 'tribal government/tribal government agency staff'),
        ('victim advocates (non-government)', 'victim advocates'),
        ('victim assistants (government)', 'victim assistants'),
        ('volunteers', 'volunteers'),
        ('other', 'other'),
    ]
    TOPIC = [
        ('advocate response', 'advocate response'),
        ('child witnesses', 'child witnesses'),
        ('confidentiality', 'confidentiality'),
        ('dating violence overview, dynamics, and services','dating violence overview, dynamics, and services'),
        ('mandatory reporting requirements', 'mandatory reporting requirements'),
        ('response to victims/survivors who have been trafficked', 'response to victims/survivors who have been trafficked'),
        ('safety planning for victims/survivors', 'safety planning for victims/survivors'),
        ('sexual assault overview, dynamics, and services','sexual assault overview, dynamics, and services'),
        ('stalking overview, dynamics, and services', 'stalking overview, dynamics, and services'),
        ('supervised visitation and exchange', 'supervised visitation and exchange'),
        ('civil court procedures', 'civil court procedures'),
        ('criminal court procedures', 'criminal court procedures'),
        ('domestic violence committed by law enforcement personnel', 'domestic violence committed by law enforcement personnel'),
        ('domestic violence statutes/codes', 'domestic violence statutes/codes'),
        ('firearms and domestic violence','firearms and domestic violence'),
        ('homicide prevention','homicide prevention'),
        ('identification and arrest of predominant aggressor','identification and arrest of predominant aggressor'),
        ('immigration','immigration'),
        ('judicial response','judicial response'),
        ('law enforcement response','law enforcement response'),
        ('pro-arrest policies','pro-arrest policies'),
        ('probation response','probation response'),
        ('prosecution response','prosecution response'),
        ('protection orders','protection orders'),
        ('sexual assault evidence collection kits','sexual assault evidence collection kits'),
        ('sexual assault statues/codes','sexual assault statues/codes'),
        ('sexual assault forensic examination','sexual assault forensic examination'),
        ('stalking statues/codes','stalking statues/codes'),
        ('tribal jurisdiction and public law 280', 'tribal jurisdiction and public law 280'),
        ('are American Indian or Alaska Native','are American Indian or Alaska Native'),
        ('are Asian','are Asian'),
        ('are Black or African American','are Black or African American'),
        ('are Deaf or hard of hearing','are Deaf or hard of hearing'),
        ('are elderly','are elderly'),
        ('are Hispanice or Latino','are Hispanice or Latino'),
        ('are homeless or living in poverty','are homeless or living in poverty'),
        ('are immigrants, refugees, or asylum seekers','are immigrants, refugees, or asylum seekers'),
        ('are in correctional settings','are in correctional settings'),
        ('are lesbian, gay, bisexual, transgender, or intersex','are lesbian, gay, bisexual, transgender, or intersex'),
        ('are Native Hawaiian or other Pacific Islander','are Native Hawaiian or other Pacific Islander'),
        ('have disabilities','have disabilities'),
        ('have limited English proficiency','have limited English proficiency'),
        ('have mental health issues','have mental health issues'),
        ('have substance abuse issues','have substance abuse issues'),
        ('live in rural areas','live in rural areas'),
        ('Community response to sexual assault','Community response to sexual assault'),
        ('Coordinated community response','Coordinated community response'),
        ('Response teams (DART, DVRT, SART)','Response teams (DART, DVRT, SART)'),
        ('Technology','Technology')
    ]
    TYPE = [
        ('training', 'training'),
        ('wellness retreat', 'wellness retreat'),
        ('peer support collaborative', 'peer support collaborative'),
        ('other','other'),
    ]

    entry_date = models.DateField(default = date.today)
    occupation = models.CharField(max_length = 50, verbose_name = "Occupation of Trainees", blank = True, choices = OCCUPATION)
    num_attendees = models.PositiveIntegerField(verbose_name = "Number of Attendees", default = 0)
    duration = models.PositiveIntegerField(verbose_name = "Training Duration (min)", default = 0)
    training_type = models.CharField(max_length = 50, verbose_name = "Type of Training", blank = True, choices = TYPE)
    training_type_other = models.TextField(verbose_name = "Type of Training - Other Text", default = "")

    class Meta:
        verbose_name = "Training Team Entry"
        verbose_name_plural = "Training Team Entries"

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

class Development(models.Model):
    entry_date = models.DateField(default = date.today)
    new_donors = models.PositiveIntegerField(verbose_name = "New Donors", default = 0)
    new_foundations = models.PositiveIntegerField(verbose_name = "New Foundations/Grants", default = 0 )
    over_1000 = models.PositiveIntegerField(verbose_name = "Gifts over $1000", default = 0)
    recurring_donors = models.PositiveIntegerField(verbose_name = "Recurring Donors", default = 0)
    recurring_gift_avg = models.PositiveIntegerField(verbose_name = "Recurring Gift Average", default = 0)
    total_raised = models.PositiveIntegerField(verbose_name = "Total Amount Raised", default = 0)
    percent_goal_met = models.PositiveIntegerField(verbose_name = "Percentage of Monthly Goal Met", default = 0)

    class Meta:
        verbose_name = "Development Team Entry"
        verbose_name_plural = "Development Team Entries"

class DevelopmentForm(ModelForm):
    class Meta:
        model = Development
        fields = '__all__'
