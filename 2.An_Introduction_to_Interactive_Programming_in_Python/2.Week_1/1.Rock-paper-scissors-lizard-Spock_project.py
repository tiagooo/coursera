# Rock-paper-scissors-lizard-Spock Game

import math
import random

# helper functions

def number_to_name(number):
  
    if number == 0:
        comp_name = 'rock'
    elif number == 1:
        comp_name = 'spock'
    elif number == 2:
        comp_name = 'paper'
    elif number == 3:
        comp_name = 'lizard'
    elif number == 4:
        comp_name = 'scissors'
    else:
        print "No correct input number!"
    return comp_name
    
def name_to_number(name):
    
    if name == 'rock':
        player_number = 0
    elif name == 'Spock':
        player_number = 1
    elif name == 'paper':
        player_number = 2
    elif name == 'lizard':
        player_number = 3
    elif name == 'scissors':
        player_number = 4
    else:
        print "No correct input name!"
    return player_number

def rpsls(name): 
    
    player_number = name_to_number(name)
    
    comp_number = random.randrange(0, 5, 1)
    
    if (comp_number-player_number)%5 >= 3:
        print "Player chooses",str(name)
        print "Computer chooses",str(number_to_name(comp_number))
        print "Player wins!"
        print ""
    elif (comp_number-player_number)%5 <=2 and (comp_number-player_number)%5>0:
        print "Player chooses",str(name)
        print "Computer chooses",str(number_to_name(comp_number))
        print "Computer wins!"
        print ""
    elif (comp_number-player_number)%5 == 0:
        print "Player chooses",str(name)
        print "Computer chooses",str(number_to_name(comp_number))
        print "Player and computer tie!"
        print ""
    else:
        print "No correct input!"    
    return
    
# Code testing

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")