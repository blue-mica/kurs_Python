from SimpleGUICS2Pygame import simpleguics2pygame as simplegui

# from PyGames.PongAG.settings import CANVA_HEIGHT

PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
pad_speed = 2
paddle1_vel = 0
paddle2_vel = 0


def update_pads_pos(paddle1_pos, paddle2_pos, canva_height):
    global paddle1_vel, paddle2_vel
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    if paddle1_pos[1] <= HALF_PAD_HEIGHT or paddle1_pos[1] >= canva_height - HALF_PAD_HEIGHT:
        paddle1_vel = 0
    elif paddle2_pos[1] <= HALF_PAD_HEIGHT or paddle2_pos[1] >= canva_height - HALF_PAD_HEIGHT:
        paddle2_vel = 0


def keyup(key):
    global paddle1_vel, paddle2_vel

    # ball_to_right pad control
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

    # left pad control
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


def keydown(key):
    global paddle1_vel, paddle2_vel, pad_speed

    if key == simplegui.KEY_MAP["up"]:  # ball_to_right pad
        paddle2_vel -= pad_speed
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += pad_speed

    if key == simplegui.KEY_MAP["w"]:  # left pad
        paddle1_vel -= pad_speed
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += pad_speed


def draw_pads(c, paddle1_pos, paddle2_pos):
    c.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],  # left
                [paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, "White")
    c.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],  # ball_to_right
                [paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT],
                PAD_WIDTH, "White")