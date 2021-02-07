import sys
import os
from .setgoals import setup
from .tracker import track

def main():
    if len(sys.argv) == 1:
        print("Welcome to goalTracker! try 'goaltracker setup' or 'goaltracker track'")
    elif(sys.argv[1] == "setup"):
        print("taking you to setup")
        setup()
    elif(sys.argv[1] == "track"):
        track()
    elif(sys.argv[1] in ["v","-v","version"]):
        print("goaltracker version 1.0")

if __name__ == '__main__':
    maini()