import json
import datetime
import os

def track():
    days = fetchDays()   
    goals = fetchGoals() 
    recent = mostRecent(days)

    today = f"{datetime.datetime.now():%Y-%m-%d}"

    print("today is " + today + ". The most recent data we have is from " + recent)
    day = input("what date would you like to report on? ")
    if day.lower() in ["", "today", "t"]:
        day = today
    

    dailyGoals = promptByDay(day, goals)
    
    days[day] = dailyGoals
    saveData(days)

def promptByDay(day, goals):
    dailyGoals = {}
    for goal in goals:
        answer = input("did you " + goal + " today? 'Y' or 'N' ")
        if answer in ["Y", "y", "yes", "Yes"]:
            dailyGoals[goal] = True
        elif answer in ["N", "n", "no", "No"]:
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