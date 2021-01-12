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
    # this counter here tells us how many entries there are in the past 12 months
    counter = 0
    dates = dict()
    # going through each month and year, and appending them to a dictionary where
    # we can access how many entries there are for each month over the recent 12 months
    for item in reversed(queryObject):
        currDate = item.month + " " + str(item.year)
        if currDate in dates:
            dates[currDate] += 1
        else :
            dates.update({currDate : 1})
    counter1 = 12
    if dates:
        for item in dates :
            if counter1 == 0 :
                break
            else :
                counter += dates[item]
                counter1 -= 1
    # now we know how many entries there are to go through and add up to for the
    # data in the recent 12 months
    for item in reversed(queryObject):
        if counter > 0:
            age_0_12 += item.age_0_12
            age_13_17 += item.age_13_17
            age_18_24 += item.age_18_24
            age_25_59 += item.age_25_59
            age_60_plus += item.age_60_plus
            counter -= 1
        else:
            break
    Ages.append(age_0_12)
    Ages.append(age_13_17)
    Ages.append(age_18_24)
    Ages.append(age_25_59)
    Ages.append(age_60_plus)
    return Ages

'''
    SAFE team specific data processing
'''
def getExam(queryObject):
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.total_exams + currNum
        else :
            new_dict.update({currDate : item.total_exams})
    return new_dict

'''
    MAP team specific data processing
'''
def getAcc(queryObject):
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.total_accompaniments + currNum
        else :
            new_dict.update({currDate : item.total_accompaniments})
    return new_dict


'''
    OV team specific data processing
'''
def getOV(queryObject) :
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.total_OV + currNum
        else :
            new_dict.update({currDate : item.total_OV})
    return new_dict

'''
    Helper methods for the Prevention and Training teams
'''

# Helper method to get the number of trainings for both the Prevention and Training teams
def numTrainings(queryObject):
    numTrainings = 0;
    # this counter here tells us how many entries there are in the past 12 months
    counter = 0
    dates = dict()
    # going through each month and year, and appending them to a dictionary where
    # we can access how many entries there are for each month over the recent 12 months
    for item in reversed(queryObject):
        currDate = item.month + " " + str(item.year)
        if currDate in dates:
            dates[currDate] += 1
        else :
            dates.update({currDate : 1})
    counter1 = 12
    if dates:
        for item in dates :
            if counter1 == 0 :
                break
            else :
                counter += dates[item]
                counter1 -= 1
    for item in queryObject.reverse():
        if counter > 0:
            numTrainings += 1
        else:
            break
    return numTrainings

# Get the total number of attendees from both teams
def totalAtt(queryObject) :
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.num_attendees + currNum
        else :
            new_dict.update({currDate : item.num_attendees})
    return new_dict

'''
    Helper methods for the Crisis Line team
'''
def totalCall(queryObject) :
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.total_calls + currNum
        else :
            new_dict.update({currDate : item.total_calls})
    return new_dict

def highCall(queryObject) :
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict:
            currNum = new_dict[currDate]
            new_dict[currDate] = item.highest_calls + currNum
        else :
            new_dict.update({currDate : item.highest_calls})
    return new_dict

def numMinors(queryObject) :
    new_dict = dict()
    for item in queryObject:
        currMonth = item.month
        currYear = str(item.year)
        currDate = currMonth + " " + currYear
        if currDate in new_dict :
            currNum = new_dict[currDate]
            new_dict[currDate] = item.demographic_minors + currNum
        else :
            new_dict.update({currDate : item.demographic_minors})
    return new_dict


# Helper method to append the ways which the client heard about SAC into doughnut chart.
def appendHowSAC(queryObject) :
    how = []
    heard_TV = 0;
    heard_radio = 0;
    heard_website = 0;
    heard_social = 0;
    heard_friend_fam = 0;
    heard_medical = 0;
    heard_other = 0;
    # this counter here tells us how many entries there are in the past 12 months
    counter = 0
    dates = dict()
    # going through each month and year, and appending them to a dictionary where
    # we can access how many entries there are for each month over the recent 12 months
    for item in reversed(queryObject):
        currDate = item.month + " " + str(item.year)
        if currDate in dates:
            dates[currDate] += 1
        else :
            dates.update({currDate : 1})
    counter1 = 12
    # appending now from data from the recent 12 months
    if dates:
        for item in dates :
            if counter1 == 0 :
                break
            else :
                counter += dates[item]
                counter1 -= 1
    for item in reversed(queryObject):
        if counter > 0:
            heard_TV += item.heard_TV
            heard_radio += item.heard_radio
            heard_website += item.heard_website
            heard_social += item.heard_social
            heard_friend_fam = item.heard_friend_fam
            heard_medical = item.heard_medical
            heard_other = item.heard_other
        else :
            break
    how.append(heard_TV)
    how.append(heard_radio)
    how.append(heard_website)
    how.append(heard_social)
    how.append(heard_friend_fam)
    how.append(heard_medical)
    how.append(heard_other)
    return how

'''
    Helper method to parse the # of sessions/new individuals/old individuals into
    a dictionary. Second parameter is either sessions, new, or continue to indicate
    which data field is currently being processed. Mainly used for the advocacy, and
    clinical team data. Usage: read from dictionary so anyone can contribute to a month's data
'''
def numSP(queryObject, string):
    new_dict = dict()
    if string ==  "sessions" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.total_sess + currNum
            else :
                new_dict.update({currDate : item.total_sess})
        return new_dict
    elif string == "new" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.total_new + currNum
            else :
                new_dict.update({currDate : item.total_new})
        return new_dict
    elif string == "continue" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.total_continue + currNum
            else :
                new_dict.update({currDate : item.total_continue})
        return new_dict
    else :
        print("Not a valid query")

'''
    Helper methods for development
'''
def develop(queryObject) :
    recurring_gift_avg = 0
    total_raised = 0
    percent_goal_met = 0
    # this counter here tells us how many entries there are in the past 12 months
    counter = 0
    dates = dict()
    # going through each month and year, and appending them to a dictionary where
    # we can access how many entries there are for each month over the recent 12 months
    for item in reversed(queryObject):
        currDate = item.month + " " + str(item.year)
        if currDate in dates:
            dates[currDate] += 1
        else :
            dates.update({currDate : 1})
    counter1 = 12
    if dates:
        for item in dates :
            if counter1 == 0 :
                break
            else :
                counter += dates[item]
                counter1 -= 1
    for item in queryObject:
        if counter > 0:
            recurring_gift_avg += item.recurring_gift_avg
            total_raised += item.total_raised
            percent_goal_met += item.percent_goal_met
        else :
            break
    return [recurring_gift_avg, total_raised, percent_goal_met]

def numDevelop(queryObject, string):
    new_dict = dict()
    if string ==  "donors" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.new_donors + currNum
            else :
                new_dict.update({currDate : item.new_donors})
        return new_dict
    elif string == "foundations" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.new_foundations + currNum
            else :
                new_dict.update({currDate : item.new_foundations})
        return new_dict
    elif string == "gifts" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.over_1000 + currNum
            else :
                new_dict.update({currDate : item.over_1000})
        return new_dict
    elif string == "recurring" :
        for item in queryObject:
            currMonth = item.month
            currYear = str(item.year)
            currDate = currMonth + " " + currYear
            if currDate in new_dict :
                currNum = new_dict[currDate]
                new_dict[currDate] = item.recurring_donors + currNum
            else :
                new_dict.update({currDate : item.recurring_donors})
        return new_dict
    else :
        print("Not a valid query")
