'''
    helper.py
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
