# Mini-project #6 - BLACKJACK

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = True
outcome = ""
msgplayerhandvl = ""
msgdealerhandvl = ""
score = 0
first_time = 1

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# Hand class
class Hand:
    def __init__(self):
        self.handcards=[]
        # create Hand object

    def __str__(self):
        handstr = ""
        for i in range(len(self.handcards)):
            handstr += " "+str(self.handcards[i])
        handstrfinal="Hand contains"+handstr
        return handstrfinal
        # return a string representation of a hand

    def add_card(self, card):
        self.handcards.append(card)
        # add a card object to a hand

    def get_value(self):
        self.value=0
        acesvalue=False
        for i in range(len(self.handcards)):
            j=self.handcards[i]
            self.value= self.value + VALUES[j.get_rank()]
            if j.get_rank()=="A":
                acesvalue = True
        if acesvalue==True:
            if self.value+10 <= 21:
                self.value=self.value+10
        return self.value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        newpos= []
        for i in range(len(self.handcards)):
            newpos = [pos[0]+CARD_SIZE[1]*i,pos[1]+0]
            self.handcards[i].draw(canvas,newpos)
                       
        # draw a hand on the canvas, use the draw method for cards        

#Deck class
class Deck:
    def __init__(self):
        self.deckcards=[]
        for i in SUITS:
            for j in RANKS:
                self.deckcards.append(Card(i, j))        
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deckcards)
        # shuffle the deck 

    def deal_card(self):
        dealedcard=self.deckcards[-1]
        self.deckcards.pop()
        return dealedcard
        # deal a card object from the deck
    
    def __str__(self):
        deckstr = ""
        for i in range(len(self.deckcards)):
            deckstr += " "+str(self.deckcards[i])
        deckstrfinal="Deck contains"+deckstr
        return deckstrfinal
        # return a string representing the deck
        
#Event handlers for buttons
def deal():
    global outcome, in_play, globaldeck, playerhand, dealerhand,score,first_time
    outcome =""
    if first_time==1:
        globaldeck = Deck()
        globaldeck.shuffle()
        playerhand = Hand()
        dealerhand = Hand()
        for i in range(1,3):
            playerhand.add_card(globaldeck.deal_card())
            dealerhand.add_card(globaldeck.deal_card())
        in_play = True
        first_time=0
        outcome= "Hit or stand?"
    elif in_play==False:
        globaldeck = Deck()
        globaldeck.shuffle()
        playerhand = Hand()
        dealerhand = Hand()
        for i in range(1,3):
            playerhand.add_card(globaldeck.deal_card())
            dealerhand.add_card(globaldeck.deal_card())
        in_play = True
        outcome= "Hit or stand?"
    else:
        outcome = "You have lost the round!"
        score -=1
        globaldeck = Deck()
        globaldeck.shuffle()
        playerhand = Hand()
        dealerhand = Hand()
        for i in range(1,3):
            playerhand.add_card(globaldeck.deal_card())
            dealerhand.add_card(globaldeck.deal_card())
        in_play = True
        
def hit():
    global outcome, playehand, dealerhand, in_play,score
    if in_play == True:
        if playerhand.get_value() <21:
            playerhand.add_card(globaldeck.deal_card())
            outcome= "Hit or stand?"
        elif playerhand.get_value() >21:
            outcome ="You have busted! New deal?"
            in_play= False
            score -=1
        elif playerhand.get_value() == 21:     
            outcome ="You should stand, you have exactly 21!"
            
def stand():
    global outcome, playehand, dealerhand, in_play,score
    if in_play == True:
        if playerhand.get_value() >21:
            outcome= "You have busted! New deal?"
            score -=1
        elif dealerhand.get_value() <=17:
            while dealerhand.get_value()<=17:
                dealerhand.add_card(globaldeck.deal_card())
            if dealerhand.get_value() >21:
                outcome= "Dealer busted! New deal?"
                score +=1
            elif (playerhand.get_value()-dealerhand.get_value())>0:
                outcome= "Player Wins! New deal?"
                score +=1
            else:
                outcome= "Dealer Wins! New deal?"
                score -=1
        elif (playerhand.get_value()-dealerhand.get_value())>0:
            outcome="Player Wins! New deal?"
            score +=1
        else:
            outcome= "Dealer Wins! New deal?"
            score -=1
        in_play=False

#draw handler    
def draw(canvas):
    global outcome, playerhand, dealerhand, in_play,card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, score
    #Title/outcome
    canvas.draw_text("BlackJack", (240, 35), 40, 'black')
    canvas.draw_text(outcome, (40, 320), 30, 'white')
    playerhand.draw(canvas, [18, 80])
    dealerhand.draw(canvas, [18, 480])
    #Score counter
    canvas.draw_text("score is: "+str(score), (460, 380), 24, 'white')
    #Card Labels
    canvas.draw_text("Player Cards", (20, 60), 24, 'white')
    canvas.draw_text("Dealer Cards", (20, 460), 24, 'white')
    #Final messages
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [54,481+(CARD_BACK_SIZE[1]/2)], CARD_BACK_SIZE)
    else:
        valuep="Player hand="+str(playerhand.get_value())
        valued="Dealer hand="+str(dealerhand.get_value())
        canvas.draw_text(valuep, (460, 300), 16, 'white')
        canvas.draw_text(valued, (460, 340), 16, 'white')
        
#initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#Buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

#initialization
deal()
frame.start()