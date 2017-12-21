import random
from day15.PongAG.pads import PAD_WIDTH, HALF_PAD_WIDTH, HALF_PAD_HEIGHT, update_pads_pos, draw_pads


CANVA_WIDTH = 600
CANVA_HEIGHT = 400
BALL_RADIUS = 20
score1 = 0
score2 = 0
ball_pos = [CANVA_WIDTH / 2, CANVA_HEIGHT / 2]
ball_vel = [random.randrange(1, 5), random.randrange(1, 4)]
ball_to_right = True
paddle1_pos = [HALF_PAD_WIDTH, CANVA_HEIGHT / 2]
paddle2_pos = [CANVA_WIDTH - HALF_PAD_WIDTH, CANVA_HEIGHT / 2]


def init():
    """Initializes game"""
    global paddle1_pos, paddle2_pos, score1, score2
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, CANVA_HEIGHT / 2]
    paddle2_pos = [CANVA_WIDTH - HALF_PAD_WIDTH, CANVA_HEIGHT / 2]
    ball_init(ball_to_right)


def draw(c):
    """Redraws all elements during game"""
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global ball_to_right

    # update paddle's vertical position, keep paddle on the screen
    update_pads_pos(paddle1_pos, paddle2_pos, CANVA_HEIGHT)

    # draw mid line and gutters
    draw_field(c)

    # draw paddles
    draw_pads(c, paddle1_pos, paddle2_pos)

    # update ball
    update_game_state(ball_pos, ball_vel, paddle1_pos, paddle2_pos)

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score1), [250, 50], 30, 'White')
    c.draw_text(str(score2), [320, 50], 30, 'White')


def draw_field(c):
    """Draws game field"""
    c.draw_line([CANVA_WIDTH / 2, 0], [CANVA_WIDTH / 2, CANVA_HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, CANVA_HEIGHT], 1, "White")
    c.draw_line([CANVA_WIDTH - PAD_WIDTH, 0], [CANVA_WIDTH - PAD_WIDTH, CANVA_HEIGHT], 1, "White")


def ball_init(right):
    """Initializes ball movement in right or left direction"""

    global ball_pos, ball_vel
    ball_pos = [CANVA_WIDTH / 2, CANVA_HEIGHT / 2]
    if right:
        ball_vel = [- random.randrange(1, 5), random.randrange(1, 4)]
    else:
        ball_vel = [random.randrange(1, 5), random.randrange(1, 4)]


def update_game_state(ball_pos, ball_vel, paddle1_pos, paddle2_pos):
    """
    Updates game state
    :param ball_pos: current ball position
    :param ball_vel: ball velocity
    :param paddle1_pos: position of paddle 1
    :param paddle2_pos: postition of paddle 2
    :return: None
    """
    global score1, score2,  ball_to_right
    ball_pos[0] -= ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (CANVA_HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]  # up, down bounce
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1  # pad bounce and ball speed up
        else:
            score2 += 1  # gutter hit
            ball_to_right = True
            ball_init(ball_to_right)
    elif ball_pos[0] >= CANVA_WIDTH - BALL_RADIUS - PAD_WIDTH:
        if paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score1 += 1
            ball_to_right = False
            ball_init(ball_to_right)
