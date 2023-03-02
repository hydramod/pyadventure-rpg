import cmd
import textwrap
import sys
import os
import time
import random

### Player Setup ###
class player:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.mana = 0
        self.player_class = ''
        self.status_effect = []
        self.location = 'home'
        self.game_over = False

my_player = player()

### Title Screen ###
def title_menu_select():
    options = {
        'play': start,
        'help': help_menu,
        'quit': SystemExit
    }
    
    while True:
        option = input("> ").lower()
        if option in options:
            options[option]()
            break
        print("Invalid command, Try again")

def title_screen():
    os.system('clear')
    print("*#" * 21)
    print("*#{:^39}#*".format("WELCOME TO PYADVENTURE RPG!"))
    print("*#" * 21)
    print("{:^43}".format("<- Play ->"))
    print("{:^43}".format("<- Help ->"))
    print("{:^43}".format("<- Quit ->"))
    print("{:^43}".format("Copyright 2023 Ali Saeid"))
    title_menu_select()

def help_menu():
    print("*#" * 21)
    print("*#{:^39}*#".format("HELP"))
    print("*#" * 21)
    print("{:^43}".format("<- Use UP, DOWN, LEFT, RIGHT to move ->"))
    print("{:^43}".format("<-   Type your commands to do them   ->"))
    print("{:^43}".format("<-  Use examine to inspect something ->"))
    print("{:^43}".format("<-      Have fun and good luck       ->"))
    title_menu_select()

"""
MAP
     a   b   c   d   e
1  +---+---+---+---+---+
   | a1| b1| c1| d1| e1|
2  +---+---+---+---+---+
   | a2| b2| c2| d2| e2|
3  +---+---+---+---+---+
   | a3| b3| c3| d3| e3|
4  +---+---+---+---+---+
   | a4| b4| c4| d4| e4|
5  +---+---+---+---+---+
   | a5| b5| c5| d5| e5|
   +---+---+---+---+---+

"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMNIATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'b1': False, 'c1': False, 'd1': False, 'e1': False,
                'a2': False, 'b2': False, 'c2': False, 'd2': False, 'e2': False,
                'a3': False, 'b3': False, 'c3': False, 'd3': False, 'e3': False,
                'a4': False, 'b4': False, 'c4':False, 'd4': False, 'e4': False,
                'a5': False, 'b5': False, 'c5': False, 'd5': False, 'e5': False}

zonemap = {
    'a1': {
        ZONENAME : 'inn',
        DESCRIPTION : "The Rusty Dragon Inn, a cozy tavern filled with boisterous patrons and warm hearth, welcomes you for a night's rest",
        EXAMNIATION : "As you survey the dimly lit room, your gaze falls upon a solitary figure shrouded in a hood. Drawing nearer, you take a seat at his table, engaging him in brief conversation. Through his veiled words, you learn of an enigmatic artifact hidden deep within a cursed cave. Your mission: to brave the ruins and reclaim this long-lost treasure.",
        SOLVED : False,
        UP : '',
        DOWN : 'a2',
        LEFT : '',
        RIGHT : 'b1',
    },
    'b1': {
        ZONENAME : 'town gaurd',
        DESCRIPTION : 'Guard post at the town gate, manned by vigilant knights and armed with crossbows, stands as the first line of defense against invaders and bandits',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'c1',
    },
    'c1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'd1',
    },
    'd1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'd2',
        LEFT : 'c1',
        RIGHT : 'e1',
    },
    'e1': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : '',
        DOWN : 'e2',
        LEFT : 'd1',
        RIGHT : '',
    },
    'a2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'a3',
        LEFT : '',
        RIGHT : 'b2',
    },
    'b2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'b1',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'c2',
    },
    'c2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'c1',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'd2',
    },
    'd2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'd1',
        DOWN : 'd3',
        LEFT : 'c2',
        RIGHT : 'e2',
    },
    'e2': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'e1',
        DOWN : 'e3',
        LEFT : 'd2',
        RIGHT : '',
    },
    'a3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'a4',
        LEFT : '',
        RIGHT : 'b3',
    },
    'b3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'b2',
        DOWN : 'b4',
        LEFT : 'a3',
        RIGHT : 'c3',
    },
    'c3': {
        ZONENAME : 'home',
        DESCRIPTION : 'A modest thatched-roof cottage with wooden beams and a dirt floor, situated in a rural village.',
        EXAMNIATION : 'A central hearth for cooking and warmth, with sparse furnishings such as a rough-hewn table and stools, and a straw mattress in the corner.',
        SOLVED : False,
        UP : 'c2',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'd3'
    },
    'd3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'd2',
        DOWN : 'd4',
        LEFT : 'c3',
        RIGHT : 'e3',
    },
    'e3': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'e2',
        DOWN : 'e4',
        LEFT : 'd3',
        RIGHT : '',
    },
    'a4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'a5',
        LEFT : '',
        RIGHT : 'b4',
    },
    'b4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'b5',
        LEFT : 'a4',
        RIGHT : 'c4',
    },
    'c4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'c3',
        DOWN : 'c5',
        LEFT : 'b4',
        RIGHT : 'd4',
    },
    'd4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'd3',
        DOWN : 'd5',
        LEFT : 'c4',
        RIGHT : 'e4',
    },
    'e4': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'e3',
        DOWN : 'e5',
        LEFT : 'd4',
        RIGHT : '',
    },
    'a5': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'a4',
        DOWN : '',
        LEFT : '',
        RIGHT : 'b5',
    },
    'b5': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'b4',
        DOWN : '',
        LEFT : 'a5',
        RIGHT : 'c5',
    },
    'c5': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'c4',
        DOWN : '',
        LEFT : 'b5',
        RIGHT : 'd5',
    },
    'd5': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'd4',
        DOWN : '',
        LEFT : 'c5',
        RIGHT : 'e5',
    },
    'e5': {
        ZONENAME : '',
        DESCRIPTION : 'description',
        EXAMNIATION : 'examine',
        SOLVED : False,
        UP : 'e4',
        DOWN : '',
        LEFT : 'd5',
        RIGHT : '',
    }

}

def location():
    """
    Display current location
    """
    print("*#" * 21)
    print("*#{:^39}*#".format(my_player.location.upper()))
    print("*#{:^39}*#".format(zonemap[my_player.location][DESCRIPTION]))
    print("*#" * 21)

def user_input():
    print("*#" * 21)
    print("*#{:^39}*#".format("What would you like to do?"))
    print("*#" * 21)
    while True:
        action = input("> ").lower()
        acceptable_actions = {'move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look'}
        if action in acceptable_actions:
            break
        print("Invalid action, try again.\n")
    if action == 'quit':
        sys.exit()
    elif action in {'move', 'go', 'travel', 'walk'}:
        player_move(action)
    else:
        player.examine(action)

def player_move(action):
    ask_user = "Where do you want to move to?\n"
    user_dest = input(ask_user)
    print("*#" * 21)
    print("*#{:^39}*#".format(ask_user))
    print("*#{:^39}*#".format(user_dest))
    print("*#" * 21)
    if user_dest in ['up', 'north']:
        destination = zonemap[my_player.location][UP]
        movement_handler(destination)
    elif user_dest in ['down', 'south']:
        destination = zonemap[my_player.location][DOWN]
        movement_handler(destination)
    elif user_dest in ['left', 'west']:
        destination = zonemap[my_player.location][LEFT]
        movement_handler(destination)
    elif user_dest in ['right', 'east']:
        destination = zonemap[my_player.location][RIGHT]
        movement_handler(destination)

def movement_handler(destination):
    print("*#" * 21)
    print("*#{:^39}*#".format("You have moved to the " + destination + "."))
    print("*#" * 21)
    my_player.location = destination
    location()

def player_examine(action):
    if zonemap[my_player.location][SOLVED]:
        print("*#" * 21)
        print("*#{:^39}*#".format("There is nothing left to see here."))
        print("*#" * 21)
    else:
        print("trigger event")

def start():
    return

def game_loop():
    while my_player.game_over is False:
        user_input()

def game_setup():
    """
    Set up game, get player details
    """
    os.system('clear')

    question1 = "Hello, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    my_player.name = player_name

    question2 = f"Hi {player_name}, choose your class: warrior, mage, or rogue?\n"
    valid_classes = {"warrior": {"health": 120, "mana": 20},
                 "mage": {"health": 60, "mana": 120},
                 "rogue": {"health": 70, "mana": 50}}

    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    while True:
        player_class = input("> ").lower()
        if player_class in valid_classes:
            my_player.player_class = player_class
            my_player.health = valid_classes[player_class]["health"]
            my_player.mana = valid_classes[player_class]["mana"]
            print(f"Good choice {player_name}, you are now a {player_class}\n")
            break
        else:
            print("Invalid class choice. Please try again.")
        time.sleep(0.05)

    question3 = f"Welcome {player_name} the {player_class}\nHere is where you new pyadventure begins"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system('clear')
    print("*#" * 21)
    print("*#{:^38}*#".format("Let your pyadventure unfold!"))
    print("*#" * 21)
    game_loop()

def main():
    title_screen()
    game_setup()

main()