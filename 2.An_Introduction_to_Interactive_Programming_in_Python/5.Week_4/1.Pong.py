# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle oftable
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0,0]
    if direction == "RIGHT":
        ball_vel[0]=random.randrange(2,4)
        ball_vel[1]=-random.randrange(1,3)
    elif direction == "LEFT":
        ball_vel[0]=-random.randrange(2,4)
        ball_vel[1]=-random.randrange(1,3)
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = 200
    paddle2_pos = 200
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball("LEFT")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddle1_vel-3
    elif key == simplegui.KEY_MAP["S"]:
        paddle1_vel = paddle1_vel+3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = paddle2_vel-3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle2_vel+3
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, current_key, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #Colision control
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= (HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] <= (BALL_RADIUS+PAD_WIDTH):
        if abs(ball_pos[1]-paddle1_pos) <= 40:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]*1.1
        else:
            score2 = score2 + 1 
            spawn_ball("RIGHT")
    elif ball_pos[0] >= (WIDTH-(BALL_RADIUS+PAD_WIDTH)):
        if abs(ball_pos[1]-paddle2_pos) <= 40:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]*1.1
        else:
            score1 = score1 + 1 
            spawn_ball("LEFT")
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos+paddle1_vel) >= HALF_PAD_HEIGHT and (paddle1_pos+paddle1_vel) <= (400-HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos+paddle2_vel) >= HALF_PAD_HEIGHT and (paddle2_pos+paddle2_vel) <= (400-HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
        
    # draw paddles
    c.draw_line((HALF_PAD_WIDTH,(paddle1_pos-HALF_PAD_HEIGHT)),(HALF_PAD_WIDTH,(paddle1_pos+HALF_PAD_HEIGHT)), PAD_WIDTH, 'white')
    c.draw_line((WIDTH-HALF_PAD_WIDTH,(paddle2_pos-HALF_PAD_HEIGHT)),(WIDTH-HALF_PAD_WIDTH,(paddle2_pos+HALF_PAD_HEIGHT)), PAD_WIDTH, 'white')
    
    # draw scores
    c.draw_text(str(score1), (240, 50), 50, 'White')
    c.draw_text(str(score2), (340, 50), 50, 'White')
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game,100)

# start frame
new_game()
frame.start()