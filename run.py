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
        self.status_effect = []
        self.location = 'home'

new_player = player()

### Title Screen ###
def title_menu_select():
    options = {
        'play': start,
        'help': help_menu,
        'quit': system.exit
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

def help_menu_select():
    print("*#" * 21)
    print("*#{:^39}*#".format("HELP"))
    print("*#" * 21)
    print("{:^43}".format("<- Use UP, DOWN, LEFT, RIGHT to move ->"))
    print("{:^43}".format("<-   Type your commands to do them   ->"))
    print("{:^43}".format("<-  Use examine to inspect something ->"))
    print("{:^43}".format("<-      Have fun and good luck       ->"))
    title_menu_select()

def start_game():

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
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'c1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'd1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'e1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'c2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'd2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'e2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'c3': {
        ZONENAME = 'Home'
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'd3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'e3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'c4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'd4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'e4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'a5': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'b5': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'c5': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'd5': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    },
    'e5': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMNIATION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right', 'east'
    }

}