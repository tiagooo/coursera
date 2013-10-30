# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code

comp_num=0
range_num=100
remaining_guesses=7

# helper function to start and restart the game
def new_game():
    global comp_num
    global range_num
    global remaining_guesses
    comp_num=random.randrange(0, range_num)
    if range_num==100:
        remaining_guesses = 7
    elif range_num==1000:
        remaining_guesses = 10
    print "NEW GAME. Range is from 0 to", range_num
    print "Number of remaining guesses",str(remaining_guesses)
    print ""
    return


# define event handlers for control panel
def range100():
    global range_num
    range_num=100
    new_game()
    return

def range1000():
    global range_num
    range_num=1000
    new_game()
    return
    
def input_guess(guess):
    global comp_num
    global remaining_guesses
    guess_num=int(guess)
    print "Guess was",guess_num
    if guess_num==comp_num:
        print "Congratulations you won!"
        print ""
        new_game()
    elif guess_num>comp_num:
        remaining_guesses=remaining_guesses-1
        print "Lower!"
        print "Number of remaining guesses",str(remaining_guesses)
        print ""
    else:
        remaining_guesses=remaining_guesses-1
        print "Higher!"
        print "Number of remaining guesses",str(remaining_guesses)
        print ""
    if  remaining_guesses<=0:
        print "You lost!"
        print "The computer number was:",comp_num
        print ""
        new_game()
    return
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements
range_100 = frame.add_button("Range 0-100", range100, 150)
range_1000 = frame.add_button("Range 0-1000", range1000, 150)
guess = frame.add_input("Enter a guess", input_guess, 150)

# call new_game and start frame
frame.start()
new_game()