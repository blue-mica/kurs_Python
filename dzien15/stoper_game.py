################################################################
###                                                          ###
###       Game "Stopwatch" by frank.gdansk@gmail.com         ###
###                                                          ###
###   An Introduction to Interactive Programming in Python   ###
###             Coursera class 2012, Assignment 3            ###
################################################################

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
time_val = 0  # variable to hold value of time
time_formated = ''  # string with time_val changes into formated str
game_running = False  # True or False - depending if watch is running
score = 0  # keep player score
attempt = 0  # keep number of tries


# changing number into formatted string
def format_timer(t):
    """ int -> (str)
    Changes given integer into formatted string A:BC.D
    Where A -> min, BC -> sec, D -> tenth of sec
    """

    # changing number into string to be able to use slices of this string
    time_str = str(t)

    # tenth of seconds - using last character from string
    tenth_sec = time_str[-1]

    # seconds - use before-last and third to last character from str
    # less than 1 sec
    if time_val < 10:
        seconds = '00.'

    # 1.0 to 9.9 sec
    elif 10 <= time_val < 100:
        seconds = '0' + time_str[-2] + '.'

    # 10.0 to 59.9
    else:
        up_sixty = time_val % 600  # make sure that seconds will be up to 60 (59 incl.)

        # making sure that seconds have always two digits
        if up_sixty < 10:
            seconds = '00.'

        elif 10 <= up_sixty < 100:
            seconds = '0' + str(up_sixty)[0:-1] + '.'

        else:
            seconds = str(up_sixty)[-3:-1] + '.'

    # minutes
    if time_val < 600:
        minutes = '0:'

    else:
        minutes = str(time_val // 600) + ':'

    # update formated string to global variable time_formated
    global time_formated
    time_formated = minutes + seconds + tenth_sec


# define event handlers for buttons; "Start", "Stop", "Reset"
# start
def start():
    """Sets game into running state. Starts watch."""

    global game_running
    game_running = True  # set watch state to running
    timer.start()


# stop
def stop():
    """
    Stops watch, adds attempts' count and score if stopped on even second.
    Sets game into non running state.
    """
    # todo
    pass


# reset
def reset():
    """Resets game. Clears all counters."""
    # todo
    pass


# define event handler for timer with 0.1 sec interval
def stoper():
    """Add 1 to time_val every 0.1 sec"""
    # todo
    pass


# define handler for drawing time on canvas
def display(canvas):
    """Displays watch, scores and instructions"""

    # watch
    format_timer(time_val)
    canvas.draw_text(time_formated, [75, 120], 40, "Red")

    # scores
    your_score = 'Your score: ' + str(score) + '     Tries: ' + str(attempt)
    canvas.draw_text(your_score, [15, 30], 20, "Yellow")

    # instructions
    instructions = 'Try to Stop on even seconds to get point.'
    canvas.draw_text(instructions, [5, 195], 12, "Aqua")


# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200)
frame.set_canvas_background("Green")

# register event handlers
frame.set_draw_handler(display)
timer = simplegui.create_timer(100, stoper)
button_start = frame.add_button('Start', start, 100)
button_stop = frame.add_button('Stop', stop, 100)
button_reset = frame.add_button('Reset', reset, 100)

# start timer and frame
frame.start()

# seems working!
