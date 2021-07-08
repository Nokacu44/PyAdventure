from Game.Items import *
from Game.Player import *

from os import system,name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


f = open("Game\Databases\Players.json","r")
data = json.loads(f.read())

player = None

def Menu():
    done = 0
    while done == 0:
        clear()
        print("Welcome to PyAdventure !")
        print("[1] I already have an hero\n[2] Create a new hero")
        _input = int(input("-->"))
        if _input == 1:
            Join()
        elif _input == 2:
            print("xd")
        elif _input == 3:
            done = 1
        else:
            _input = 0

def Join():
    print("Please enter your name")
    _name = input()
    while _name not in data:
        print("Hai sbagliato nome utente!")
        _input = int(input())
        if _input == 1:
            return
    else:
        global player 
        player = data[_name]

if __name__ == "__main__":
    Menu()