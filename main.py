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

options=["rock", "paper", "scissors"]

computer_option=""

print("""
######################################
######################################
###\_______________________________/##
## |   Rock, Paper, Scissors Game | ##
## |______________________________| ##
## /############################## \ #
######################################
""")
user_option=input('Pick your poison: ')
print("""
--------------------------
Player1 has selected: """
+user_option+"""
--------------------------
Player2 has selected: """)


if user_option==computer_option:
    print('tie game')
elif user_option=1 and computer_option=2:
    print('')
elif user_option=2 and computer_option=1:
    print('')
elif user_option=3 and computer_option=1:
    print('')
