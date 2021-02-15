import json
import datetime
import os

def track():
    days = fetchDays()   
    goals = fetchGoals() 
    recent = mostRecent(days)

    today = f"{datetime.datetime.now():%Y-%m-%d}"
    yesterday = f"{(datetime.datetime.now() - datetime.timedelta(1)):%Y-%m-%d}"

    print("today is " + today)
    print("yesterday was " + yesterday)
    if recent == None:
        print("this appears to be the first time you've tracked your goals")
    else:
        print("The most recent data we have is from " + recent)
    day = input("what date would you like to report on? ")
    if day.lower() in ["today", "t"]:
        day = today
    elif day.lower() in ["yesterday", "y"]:
        day = yesterday
    

    dailyGoals = promptByDay(day, goals)
    
    days[day] = dailyGoals
    saveData(days)

def promptByDay(day, goals):
    print("ok, answer these questions about " + day)
    dailyGoals = {}
    for goal in goals:
        answer = input("did you " + goal + " today? 'Y' or 'N' ")
        if answer.lower() in ["y", "yes", "yup"]:
            dailyGoals[goal] = True
        elif answer.lower() in ["n", "no"]:
            dailyGoals[goal] = False
        else:
            print("sorry, not valid. you may need to resubmit for this day")
    return dailyGoals

def fetchGoals():
    try:
        goalsFile = open(goalsFilePath())
        goals = json.load(goalsFile)
    except:
        print("you don't have any goals set up")
        return []

    return goals


def fetchDays():
    try: 
        daysFile = open(daysFilePath())
        days = json.load(daysFile)
    except:
        days = {}
    
    return days

def mostRecent(data):
    
    try:
        return(sorted(list(data))[-1])
    except:
        return None

def saveData(data):
    with open(daysFilePath(), 'w') as outfile:
        json.dump(data, outfile, indent=4)


def goalsFilePath():
    returnee = os.path.join(os.path.dirname(__file__), 'data','goals.json')
    print(returnee)
    return returnee

def daysFilePath():
    returnee = os.path.join(os.path.dirname(__file__), 'data','days.json')
    print(returnee)
    return returnee