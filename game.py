import random

import arcade

from raptor import Raptor
from settings import *


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        Initilizes game window
        :param width: game window width
        :param height: game window height
        :param title: game title
        """
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.title = title

        # setup game elements
        self.enemies = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        arcade.set_background_color(COLORS['BLACK_LIGHT'])

        self.set_raptor()
        self.all_sprites.append(self.raptor.sprite)

        arcade.schedule(self.create_enemy, 5)

    def set_raptor(self):
        self.raptor = Raptor(self.width / 2,
                             AIRCRAFT_DIAMETER,
                             RAPTOR_ALTITUDE,
                             RAPTOR_SPEED,
                             0,
                             SPRITES['raptor'],
                             RAPTOR_HEALTH,
                             RAPTOR_SHIELD)
        print(f'Raptor dimensions: {self.raptor.sprite.width}x{self.raptor.sprite.height}')

    def on_draw(self):
        arcade.start_render()
        self.raptor.draw()

    def on_update(self, delta_time: float):
        pass

    # Game events

    def on_key_press(self, symbol: int, modifiers: int):
        print(f'Key {symbol} is pressed')

    def on_key_release(self, symbol: int, modifiers: int):
        print(f'key {symbol} released')

    # Game top-level functions

    def create_enemy(self, delta_time: float):
        enemy = arcade.Sprite(SPRITES['enemy1'], SCALING)
        enemy.left = random.randint(AIRCRAFT_DIAMETER, self.width - AIRCRAFT_DIAMETER)
        enemy.top = 0
