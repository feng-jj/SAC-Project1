'''
    Helper functions to help process the data for graphical representation
'''

'''
    Helper method to properly append the age into a list based on field type
'''
def appendFieldAge(queryObject) :
    Ages = []
    age_0_12 = 0
    age_13_17 = 0
    age_18_24 = 0
    age_25_59 = 0
    age_60_plus = 0
    for item in queryObject:
        age_0_12 += item.age_0_12
        age_13_17 += item.age_13_17
        age_18_24 += item.age_18_24
        age_25_59 += item.age_25_59
        age_60_plus += item.age_60_plus
    Ages.append(age_0_12)
    Ages.append(age_13_17)
    Ages.append(age_18_24)
    Ages.append(age_25_59)
    Ages.append(age_60_plus)
    return Ages

'''
    Helper method to append the ways which the client heard about SAC into doughnut chart.
    Used for the Crisis Line dashboard
'''
def appendHowSAC(queryObject) :
    how = []
    heard_TV = 0;
    heard_radio = 0;
    heard_website = 0;
    heard_social = 0;
    heard_friend_fam = 0;
    heard_medical = 0;
    heard_other = 0;
    for item in queryObject:
        heard_TV += item.heard_TV
        heard_radio += item.heard_radio
        heard_website += item.heard_website
        heard_social += item.heard_social
        heard_friend_fam = item.heard_friend_fam
        heard_medical = item.heard_medical
        heard_other = item.heard_other
    how.append(heard_TV)
    how.append(heard_radio)
    how.append(heard_website)
    how.append(heard_social)
    how.append(heard_friend_fam)
    how.append(heard_medical)
    how.append(heard_other)
    return how

'''
    Helper method to get the number of trainings for both the Prevention and Training
    teams
'''
def numTrainings(queryObject):
    numTrainings = 0;
    for item in queryObject:
        numTrainings += 1
    return numTrainings

'''
    Helper method for development
'''
def develop(queryObject) :
    recurring_gift_avg = 0
    total_raised = 0
    percent_goal_met = 0
    for item in queryObject:
        recurring_gift_avg += item.recurring_gift_avg
        total_raised += item.total_raised
        percent_goal_met += item.percent_goal_met
    return [recurring_gift_avg, total_raised, percent_goal_met]



# def combineIndividuals(q1, q2):

# #for the pie chart on sex
# clinicalSex = appendSex(clinical)
# advocacySex = appendSex(advocacy)
# safeClinicSex = appendSex(safeClinic)
# mapSex = appendSex(map_)
# ovSex = appendSex(ov)
# context['clinicalSex'] = clinicalSex
# context['advocacySex'] = advocacySex
# context['safeClinicSex'] = safeClinicSex
# context['mapSex'] = mapSex
# context['ovSex'] = ovSex
#
# #for the pie chart on aces Scores
# clinicalAdult = acesAdult(clinical)
# advocacyAdult = acesAdult(advocacy)
# safeClinicAdult = acesAdult(safeClinic)
# mapAdult= acesAdult(map_)
# ovAdult = acesAdult(ov)
# context['clinicalAdult'] = clinicalAdult
# context['advocacyAdult'] = advocacyAdult
# context['safeClinicAdult'] = safeClinicAdult
# context['mapAdult'] = mapAdult
# context['ovAdult'] = ovAdult
#


# Below are archived helper methods, as graphs are no longer needed for these fields

# '''
#     Helper method to properly append the entries for the sex of the individual to a list in pie chart rendering
# '''
# def appendSex(queryObject) :
#     sex = []
#     female = 0
#     intersex = 0
#     male = 0
#     for item in queryObject :
#         female = item.sex_female
#         intersex = item.sex_intersex
#         male = item.sex_male
#     sex.append(female)
#     sex.append(intersex)
#     sex.append(male)
#     return sex
#
# '''
#     Helper method for the ACES scores
# '''
# def acesAdult(queryObject) :
#     acesAdult = []
#     acesChild = []
#     adult0 = 0
#     adult1 = 0
#     adult2 = 0
#     adult3 = 0
#     adult4 = 0
#     child0 = 0
#     child1 = 0
#     child2 = 0
#     child3 = 0
#     child4 = 0
#     for item in queryObject:
#         adult0 += item.aces_adults_0
#         adult1 += item.aces_adults_1
#         adult2 += item.aces_adults_2
#         adult3 += item.aces_adults_3
#         adult4 += item.aces_adults_4
#         child0 += item.aces_children_0
#         child1 += item.aces_children_1
#         child2 += item.aces_children_2
#         child3 += item.aces_children_3
#         child4 += item.aces_children_4
#     acesAdult.append(adult0)
#     acesAdult.append(adult1)
#     acesAdult.append(adult2)
#     acesAdult.append(adult3)
#     acesAdult.append(adult4)
#     return acesAdult
#
# def acesChild(queryObject):
#     child0 = 0
#     child1 = 0
#     child2 = 0
#     child3 = 0
#     child4 = 0
#     acesChild = []
#     for item in queryObject:
#         child0 += item.aces_children_0
#         child1 += item.aces_children_1
#         child2 += item.aces_children_2
#         child3 += item.aces_children_3
#         child4 += item.aces_children_4
#     acesChild.append(child0)
#     acesChild.append(child1)
#     acesChild.append(child2)
#     acesChild.append(child3)
#     acesChild.append(child4)
