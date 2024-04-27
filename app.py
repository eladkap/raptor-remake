import arcade

from settings import *
from game import Game

if __name__ == '__main__':
    app = Game(SCREEN_RES[0], SCREEN_RES[1], SCREEN_TITLE)
    arcade.run()
