from Game.Items import *
from Game.Player import *
from Game.Classes import *

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
        print("[1] I already have an hero\n[2] Create a new hero\n[3] Exit")
        _input = input("-->")
        if _input == "1":
            join()
        elif _input == "2":
            create_character()
        elif _input == "3":
            done = 1
        else:
            _input = "0"

def join():
    print("Please enter your name")
    _name = input()
    while _name not in data:
        print("Hai sbagliato nome utente!")
        _input = input()
        if _input == "1":
            return
    else:
        global player 
        player = Player(_name,data[_name]["hp"],data[_name]["ap"],data[_name]["dp"],data[_name]["dx_weapon"],data[_name]["sx_weapon"],data[_name]["coins"])
        print(player)
        input()

def create_character():
    clear()
    _input = "0"
    global player

    _name = input("Insert your name -> ")

    print("Please select one class or choose to create one...")
    print("[1] Warrior\n[2] Archer\n[3] Mage\n[4] Create a class")
    while _input == "0":
        _input = input("--> ")    
        if _input == "1":
            player =  Player(_name,WARRIOR.hp,WARRIOR.dp,WARRIOR.ap,WARRIOR.dx_weapon,WARRIOR.sx_weapon,WARRIOR.coins)
        elif _input == "2":
            print("archer")
        elif _input == "3":
            print("mage")
        elif _input == "4":
            print("Create new class")
        else:
            _input == "0"
    print(player.sx_weapon)
    input()


if __name__ == "__main__":
    Menu()
