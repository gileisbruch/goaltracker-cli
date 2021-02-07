import json

goalsFilePath = 'C:\\Users\\gilei\\Projects\\goaltracker-cli\\goaltracker\\data\\goals.json'

def setup():
    done = False
    try:
        goalsFile = open(goalsFilePath)
        goals = json.load(goalsFile)
    except:
        print("let's get you set up")
        goals = []
    if(len(goals) != 0):
        print("your current goals: ")
        print(*goals, sep=", ")
    else:
        print("you have no current goals.")
    while not done:
        action = input("would you like to add ('a') or remove('r') goals? ")
        if action in ['a', 'A', 'add', 'Add']:
            goal = input("enter a goal name: ")
            print("Great! I will keep track of " + goal)
            goals.append(goal)
            print(*goals, sep=", ")
        elif action in ['r', 'R', 'remove', 'Remove']:
            goal = input("enter a goal to remove: ")
            if goal in goals:
                goals.remove(goal)
                print(*goals, sep=", ")
            else:
                print("not in list")
        else:
            print ("goodbye!")
            saveGoals(goals)
            done = True

def saveGoals(goals):
    with open(goalsFilePath, 'w') as outfile:
        json.dump(goals, outfile)
    