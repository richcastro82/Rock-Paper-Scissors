# RICHARD CASTRO
# DECEMBER 2021
# TERMINAL ONLY OUTPUT GAME
#
#
# 1. DISPLAY WELCOME MESSAGE ON TERMINAL WINDOW
# 2. ASK PLAYER FOR INPUT OPTION
# 3. SAVE PLAYER INPUT
# 4. CONSTANTS FOR THE ROCK, PAPER, SCISSORS
# 5. RANDONLY SELECT ONE OF THE CONSTANTS
# 6. GAME RULES APPLIED TO SEE WHO WON THE GAME
# 7. DISPLAY OUTCOME MESSAGE
# 8. PLAY AGAIN PROMPT


import random, os, sys
from random import randint
computer_option=randint(1,3)



print("""
######################################
######################################
## \ ----------------------------- / #
## |   Rock, Paper, Scissors Game |  #
## |------------------------------|  #
## /############################## \ #
######################################
""")


print("""
1. Rock
2. Paper
3. Scissors

Enter your selection to play the game:
""")

user_option=int(input())

if user_option==1:
    print('User picks ROCK')
if user_option==2:
    print('User picks PAPER')
if user_option==3:
    print('User picks SCISSORS')

if computer_option==1:
    print('Computer picks ROCK')
if computer_option==2:
    print('Computer picks PAPER')
if computer_option==3:
    print('Computer picks SCISSORS')


if user_option==computer_option:
    print('Tie Game')
