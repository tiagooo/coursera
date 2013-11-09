# Stopwatch: The Game"

import simplegui

# define global variables

time=0
click_counter=0
right_click_counter=0
running=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (t%600) < 100:
        mili = t%10
        sec= (t%600)/10
        minu = t/600
        text_formated = str(minu)+":"+"0"+str(sec)+"."+str(mili)
    else:
        mili = t%10
        sec= (t%600)/10
        minu = t/600
        text_formated = str(minu)+":"+str(sec)+"."+str(mili)
    return text_formated
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start_handler():
    global running
    running = True
    timer.start()
    return

def button_stop_handler():
    global click_counter
    global time
    global right_click_counter
    global running
    if running==True:
        running=False
        timer.stop()
        click_counter= click_counter+1
        diference= time%10
        if diference == 0:
            right_click_counter=right_click_counter+1
            
def button_reset_handler():
    global click_counter
    global time
    global right_click_counter
    time = 0
    click_counter = 0
    right_click_counter = 0
    timer.stop()
    return

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1
    return

# define draw handler
def draw_handler(canvas):
    global time
    canvas.draw_text(format(time), [75, 170], 60, "White")
    canvas.draw_text(str(right_click_counter)+"/"+str(click_counter), [230, 50], 40, "Green")
    return

# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", button_start_handler, 200)
frame.add_button("Stop", button_stop_handler, 200)
frame.add_button("Reset", button_reset_handler, 200)

# start frame
frame.start()