# Implementation of classic arcade game Pong
# game usues SimpleGUICS2Pygame package
# https://simpleguics2pygame.readthedocs.io/en/latest/index.html
# Author: ArkadioG
# License: MIT

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from day15.PongAG.settings import CANVA_WIDTH, CANVA_HEIGHT, init, draw
from day15.PongAG.pads import keyup, keydown


def main():
    pass
    # create frame
    frame = simplegui.create_frame("Pong", CANVA_WIDTH, CANVA_HEIGHT)
    # register event handlers
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.set_keyup_handler(keyup)
    # add restart button
    frame.add_button("Restart", init, 100)
    # start frame
    frame.start()


if __name__ == '__main__':
    main()
