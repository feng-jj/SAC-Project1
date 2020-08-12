from django.db import models
from datetime import date

# abstract base class for clinical, advocacy, MAP, OV, and SAFE Clinic Teams
class CommonEntries(models.Model):
    entry_date = models.DateField(default = date.today)
    total_ind = models.PositiveIntegerField(verbose_name = "Total Individuals")
    total_sess = models.PositiveIntegerField(verbose_name = "Total Sessions")
    race_amerind = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - American Indian/Alaska Native")
    race_asian = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Asian")
    race_black = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Black/African American")
    race_latinx = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Hispanic or Latino, Latina, and Latinx")
    race_pacific = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Native Hawaiian and Other Pacific Islander")
    race_white = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - White Non-Latino/Caucasian")
    race_other = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Some Other Race")
    race_multiple = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Multiple Races")
    race_unreported = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Reported")
    race_untracked = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Tracked")
    gender_agender = models.PositiveIntegerField(verbose_name = "Gender Identity - Agender")
    gender_man = models.PositiveIntegerField(verbose_name = "Gender Identity - Man")
    gender_nonbin = models.PositiveIntegerField(verbose_name = "Gender Identity - Non-binary")
    gender_woman = models.PositiveIntegerField(verbose_name = "Gender Identity - Woman")
    gender_not_rep = models.PositiveIntegerField(verbose_name = "Gender Identity - Not Reported")
    gender_other = models.PositiveIntegerField(verbose_name = "Gender Identity - Other")
    gender_other_text = models.TextField(verbose_name = "Gender Identity - Other Text")
    sex_female = models.PositiveIntegerField(verbose_name = "Sex - Female")
    sex_male = models.PositiveIntegerField(verbose_name = "Sex - Male")
    sex_inter = models.PositiveIntegerField(verbose_name = "Sex - Intersex")
    age_0_12 = models.PositiveIntegerField(verbose_name = "Age - 0-12")
    age_13_17 = models.PositiveIntegerField(verbose_name = "Age - 13-17")
    age_18_24 = models.PositiveIntegerField(verbose_name = "Age - 18-24")
    age_25_59 = models.PositiveIntegerField(verbose_name = "Age - 25-59")
    age_60_plus = models.PositiveIntegerField(verbose_name = "Age - 60 and older")
    victim_adult_sa = models.PositiveIntegerField(verbose_name = "Victimization Types - Adult Sexual Assault")
    victim_as_child = models.PositiveIntegerField(verbose_name = "Victimization Types - Adults Sexually Abused/Assaulted as Children")
    victim_nonoff_caregiver = models.PositiveIntegerField(verbose_name = "Victimization Types - Non-offending Caregivers")
    victim_child_porn = models.PositiveIntegerField(verbose_name = "Victimization Types - Child Pornography")
    victim_child_sa = models.PositiveIntegerField(verbose_name = "Victimization Types - Child Sexual Abuse/Assault")
    victim_human_traff = models.PositiveIntegerField(verbose_name = "Victimization Types - Human Sex Trafficking")
    special_deaf = models.PositiveIntegerField(verbose_name = "Special Classification - Deaf/Hard of Hearing")
    special_homeless = models.PositiveIntegerField(verbose_name = "Special Classification - Homeless")
    special_immigrant = models.PositiveIntegerField(verbose_name = "Special Classification - Immigrants/Refugees/Asylum Seekers")
    special_lgbtq = models.PositiveIntegerField(verbose_name = "Special Classification - LGBTQ")
    special_non_monog = models.PositiveIntegerField(verbose_name = "Special Classification - Non-Monogamists")
    special_sex_work = models.PositiveIntegerField(verbose_name = "Special Classification - Sex Work Professionals")
    special_bdsm = models.PositiveIntegerField(verbose_name = "Special Classification - BDSM Practitioners")
    special_vet = models.PositiveIntegerField(verbose_name = "Special Classification - Veterans")
    special_disability = models.PositiveIntegerField(verbose_name = "Special Classification - Victims with Disabilities - Cognitive/Physical/Mental")
    special_limited_eng = models.PositiveIntegerField(verbose_name = "Special Classification - Victims with Limited English Proficiency")
    special_other = models.PositiveIntegerField(verbose_name = "Special Classification - Other")
    special_other_text = models.TextField(verbose_name = "Special Classification - Other Text")
    advocacy_med_forens = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Victim Advocacy/Accompaniment to Medical Forensic Exam")
    advocacy_law_enforce = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Law Enforcement Interview Advocacy/Accompaniment")
    advocacy_individ = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Individual Advocacy")
    advocacy_immig_assist = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Immigration Assistance")
    advocacy_intervention = models.PositiveIntegerField(verbose_name = "Personal Advocacy/Achievement - Intervention with Employer, Creditor, etc.")

    class Meta:
        abstract = True
    
# child classes of CommonEntries
class Clinical(CommonEntries):  
    class Meta:
        verbose_name = "Clinical Team Entry"
        verbose_name_plural = "Clinical Team Entries"
    pass

class Advocacy(CommonEntries):
    class Meta:
        verbose_name = "Advocacy Team Entry"
        verbose_name_plural = "Advocacy Team Entries"
    pass

class MAP(CommonEntries):
    class Meta:
        verbose_name = "MAP Team Entry"
        verbose_name_plural = "MAP Team Entries"
    pass

class OV(CommonEntries):
    class Meta:
        verbose_name = "OV Team Entry"
        verbose_name_plural = "OV Team Entries"
    pass

class SAFE_Clinic(CommonEntries):
    class Meta:
        verbose_name = "SAFE Clinic Team Entry"
        verbose_name_plural = "SAFE Clinic Team Entries"
    pass

##################################################################################################

class Crisis_Line(models.Model):
    entry_date = models.DateField(default = date.today)
    total_calls = models.PositiveIntegerField(verbose_name = "Total Calls")
    highest_calls = models.PositiveIntegerField(verbose_name = "Highest # Calls in 1 Day")
    avg_length = models.FloatField(verbose_name = "Average Length (Minutes)")
    avg_wait = models.FloatField(verbose_name = "Average Wait Time (Minutes)")
    reason_self_crisis = models.PositiveIntegerField(verbose_name = "Reason - Self in Crisis")
    reason_triggered = models.PositiveIntegerField(verbose_name = "Reason - Triggered")
    reason_support_other = models.PositiveIntegerField(verbose_name = "Reason - Support for Someone Else")
    reason_concern_child = models.PositiveIntegerField(verbose_name = "Reason - Concerned for a Child")
    reason_other = models.PositiveIntegerField(verbose_name = "Reason - Other")
    reason_other_text = models.TextField(verbose_name = "Reason - Other Text")
    resource_advocacy = models.PositiveIntegerField(verbose_name = "Resource Referral - Advocacy Services")
    resource_mental_health = models.PositiveIntegerField(verbose_name = "Resource Referral - Mental Health/Therapy")
    resource_shelter = models.PositiveIntegerField(verbose_name = "Resource Referral - Shelter Services")
    resource_social = models.PositiveIntegerField(verbose_name = "Resource Referral - Social Services")
    resource_housing = models.PositiveIntegerField(verbose_name = "Resource Referral - Housing Resources")
    resource_support_group = models.PositiveIntegerField(verbose_name = "Resource Referral - Support Group")
    resource_legal = models.PositiveIntegerField(verbose_name = "Resource Referral - Legal Services")
    resource_addiction = models.PositiveIntegerField(verbose_name = "Resource Referral - Addiction Services")
    resource_bilingual = models.PositiveIntegerField(verbose_name = "Resource Referral - Bilingual Services")
    resource_hospital = models.PositiveIntegerField(verbose_name = "Resource Referral - Hospital Services")
    resource_survivor = models.PositiveIntegerField(verbose_name = "Resource Referral - Survivor Resources")
    resource_food = models.PositiveIntegerField(verbose_name = "Resource Referral - Food Access")
    resource_disability = models.PositiveIntegerField(verbose_name = "Resource Referral - Disability Resources")
    resource_financial = models.PositiveIntegerField(verbose_name = "Resource Referral - Financial Resources")
    resource_veteran = models.PositiveIntegerField(verbose_name = "Resource Referral - Veterans Resources")
    resource_other = models.PositiveIntegerField(verbose_name = "Resource Referral - Other")
    info_legal_def = models.PositiveIntegerField(verbose_name = "Information Referral - Legal Definitions")
    info_police_codes = models.PositiveIntegerField(verbose_name = "Information Referral - Police Codes/Reporting Process")
    info_healthy_relationship = models.PositiveIntegerField(verbose_name = "Information Referral - Healthy Relationships")
    info_mandatory_report = models.PositiveIntegerField(verbose_name = "Information Referral - Mandatory Reporting Process")
    info_workplace_harass = models.PositiveIntegerField(verbose_name = "Information Referral - Workplace Harassment")
    info_stalking = models.PositiveIntegerField(verbose_name = "Information Referral - Stalking/Harassment")
    info_mental_health = models.PositiveIntegerField(verbose_name = "Information Referral - General Mental Health")
    info_survivor = models.PositiveIntegerField(verbose_name = "Information Referral - Survivor Support")
    info_nop = models.PositiveIntegerField(verbose_name = "Information Referral - NoP Support")
    info_contraceptives = models.PositiveIntegerField(verbose_name = "Information Referral - Access to Contraceptives")
    info_teen_dating_violence = models.PositiveIntegerField(verbose_name = "Information Referral - Teen Dating Violence")
    info_trauma_response = models.PositiveIntegerField(verbose_name = "Information Referral - Trauma Response/Impact")
    info_firearm_safety = models.PositiveIntegerField(verbose_name = "Information Referral - Firearm Safety")
    info_sex_ed = models.PositiveIntegerField(verbose_name = "Information Referral - Sex Education")
    info_sac_info = models.PositiveIntegerField(verbose_name = "Information Referral - General SAC Info")
    info_rape_crisis_info = models.PositiveIntegerField(verbose_name = "Information Referral -  General Rape Crisis Center Info")
    demographic_minors = models.PositiveIntegerField(verbose_name = "Number of Minors")
    gender_agender = models.PositiveIntegerField(verbose_name = "Gender Identity - Agender")
    gender_man = models.PositiveIntegerField(verbose_name = "Gender Identity - Man")
    gender_nonbin = models.PositiveIntegerField(verbose_name = "Gender Identity - Non-binary")
    gender_woman = models.PositiveIntegerField(verbose_name = "Gender Identity - Woman")
    gender_not_rep = models.PositiveIntegerField(verbose_name = "Gender Identity - Not Reported")
    gender_other = models.PositiveIntegerField(verbose_name = "Gender Identity - Other")
    gender_other_text = models.TextField(verbose_name = "Gender Identity - Other Text")
    race_amerind = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - American Indian/Alaska Native")
    race_asian = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Asian")
    race_black = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Black/African American")
    race_latinx = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Hispanic or Latino, Latina, and Latinx")
    race_pacific = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Native Hawaiian and Other Pacific Islander")
    race_white = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - White Non-Latino/Caucasian")
    race_other = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Some Other Race")
    race_multiple = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Multiple Races")
    race_unreported = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Reported")
    race_untracked = models.PositiveIntegerField(verbose_name = "Race/Ethnicity - Not Tracked")
    demo_veterans = models.PositiveIntegerField(verbose_name = "Number of Veterans")
    lang_english = models.PositiveIntegerField(verbose_name = "Preferred Language - English")
    lang_spanish = models.PositiveIntegerField(verbose_name = "Preferred Language - Spanish")
    lang_other = models.PositiveIntegerField(verbose_name = "Preferred Language - Other")
    lang_other_text = models.TextField(verbose_name = "Preferred Language - Other Text")
    client_current = models.PositiveIntegerField(verbose_name = "Current Clients")
    client_new = models.PositiveIntegerField(verbose_name = "New Clients")
    heard_TV = models.PositiveIntegerField(verbose_name = "Heard Through TV")
    heard_radio = models.PositiveIntegerField(verbose_name = "Heard Through Radio")
    heard_website = models.PositiveIntegerField(verbose_name = "Heard Through Website")
    heard_social = models.PositiveIntegerField(verbose_name = "Heard Through Social Media")
    heard_friend_fam = models.PositiveIntegerField(verbose_name = "Heard Through Friend or Family")
    heard_medical = models.PositiveIntegerField(verbose_name = "Heard Through Medical Professional")
    heard_other = models.PositiveIntegerField(verbose_name = "Heard Through Other Source")
    heard_other_text = models.TextField(verbose_name = "Heard Through Other Source - Text")
    covid_mentioned = models.PositiveIntegerField(verbose_name = "COVID-19 Mentioned")

    class Meta:
        verbose_name = "Crisis Line Team Entry"
        verbose_name_plural = "Crisis Line Team Entries"
    