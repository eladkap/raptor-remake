import random

import arcade

from aircraft import Aircraft
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

    # Setup functions #

    def setup(self):
        arcade.set_background_color(COLORS['BLACK_LIGHT'])
        self.set_raptor()
        self.set_enemies()

    def set_raptor(self):
        self.raptor = Raptor(self.width / 2,
                             AIRCRAFT_DIAMETER,
                             RAPTOR_ALTITUDE,
                             RAPTOR_VELOCITY,
                             0,
                             SPRITES['raptor'],
                             RAPTOR_HEALTH,
                             RAPTOR_SHIELD)
        self.all_sprites.append(self.raptor)
        print(f'Raptor dimensions: {self.raptor.width}x{self.raptor.height}')

    def set_enemies(self):
        arcade.schedule(self.create_enemy, 3)

    # Draw functions #

    def draw_elements(self):
        self.all_sprites.draw()
        # for element in self.all_sprites:
        #     element.draw()

    def on_draw(self):
        arcade.start_render()
        self.draw_elements()

    # Update functions #

    def update_elements(self):
        self.all_sprites.update()
        # for enemy in self.enemies:
        #     enemy.update()

    def on_update(self, delta_time: float):
        self.update_elements()

    # Game events

    def on_key_press(self, symbol: int, modifiers: int):
        print(f'Key {symbol} is pressed')

    def on_key_release(self, symbol: int, modifiers: int):
        print(f'key {symbol} released')

    # Game top-level functions

    def create_enemy(self, delta_time: float):
        x = random.randint(AIRCRAFT_DIAMETER, self.width - AIRCRAFT_DIAMETER)
        y = self.height + AIRCRAFT_DIAMETER
        altitude = 1000
        velocity = ENEMY_VELOCITY
        heading = 0
        sprite_img = SPRITES['enemy1']
        health = 200

        enemy = Aircraft(x, y, altitude, velocity, heading, sprite_img, health)

        self.enemies.append(enemy)
        self.all_sprites.append(enemy)

        # enemy = arcade.Sprite(SPRITES['enemy1'], SCALING)
        # enemy.left = random.randint(AIRCRAFT_DIAMETER, self.width - AIRCRAFT_DIAMETER)
        # enemy.top = 0
