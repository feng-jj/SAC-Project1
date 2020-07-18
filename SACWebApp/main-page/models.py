from django.db import models

# abstract base class for clinical, advocacy, MAP, OV, and SAFE Clinic Teams
class CommonEntries(models.Model):
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
